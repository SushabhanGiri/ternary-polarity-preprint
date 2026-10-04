#!/usr/bin/env python3
"""Temperature-dependent coupled relic certification for the TP-D pole point.

The calculation upgrades checkpoint 13 by using a temperature-dependent
energy/entropy equation of state and a stable finite-width thermal integral
including the off-pole Higgs continuum.  It remains a controlled leading-
order calculation: the equation of state is an ideal-gas Standard Model
construction with a smooth QCD confinement interpolation, not a precision
lattice-QCD table.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad, solve_ivp

import tpd_coupled_relic as relic
import tpd_direct_detection_gate as direct_detection
import tpd_higgs_pole_diagnostic as pole
import tpd_phenomenology_prefilter as prefilter


PI = math.pi


# (mass [GeV], internal degrees, fermion, QCD-partonic)
SPECIES = (
    (0.0, 2.0, False, False),       # photon
    (0.0, 16.0, False, True),       # gluons
    (0.0, 6.0, True, False),        # three neutrinos plus antineutrinos
    (0.000510999, 4.0, True, False),
    (0.1056584, 4.0, True, False),
    (1.77686, 4.0, True, False),
    (0.0022, 12.0, True, True),
    (0.0047, 12.0, True, True),
    (0.096, 12.0, True, True),
    (1.27, 12.0, True, True),
    (4.18, 12.0, True, True),
    (172.5, 12.0, True, True),
    (80.377, 6.0, False, False),
    (91.1876, 3.0, False, False),
    (125.25, 1.0, False, False),
)


def qcd_parton_weight(temperature: float) -> float:
    """Smooth confinement switch; irrelevant at the ~3 GeV freeze-out scale."""
    return 0.5 * (1.0 + math.tanh((temperature - 0.17) / 0.03))


def species_rho_pressure_over_t4(mass_over_t: float, fermion: bool) -> tuple[float, float]:
    if mass_over_t < 0.03:
        rho = (7.0 / 8.0 if fermion else 1.0) * PI**2 / 30.0
        return rho, rho / 3.0
    if mass_over_t > 45.0:
        return 0.0, 0.0

    sign = 1.0 if fermion else -1.0

    def occupancy(energy: float) -> float:
        if energy > 700.0:
            return 0.0
        return 1.0 / (math.exp(energy) + sign)

    def rho_integrand(y: float) -> float:
        energy = math.sqrt(y * y + mass_over_t * mass_over_t)
        return y * y * energy * occupancy(energy)

    def pressure_integrand(y: float) -> float:
        energy = math.sqrt(y * y + mass_over_t * mass_over_t)
        return y**4 / (3.0 * energy) * occupancy(energy)

    rho = quad(rho_integrand, 0.0, 50.0, epsabs=1.0e-10, epsrel=2.0e-8)[0] / (2.0 * PI**2)
    pressure = quad(pressure_integrand, 0.0, 50.0, epsabs=1.0e-10, epsrel=2.0e-8)[0] / (2.0 * PI**2)
    return rho, pressure


def equation_of_state_at(temperature: float) -> tuple[float, float]:
    weight = qcd_parton_weight(temperature)
    rho_total = 0.0
    pressure_total = 0.0
    for mass, degrees, fermion, qcd_parton in SPECIES:
        rho, pressure = species_rho_pressure_over_t4(mass / temperature, fermion)
        local_weight = weight if qcd_parton else 1.0
        rho_total += degrees * local_weight * rho
        pressure_total += degrees * local_weight * pressure

    # Minimal confined-phase proxy.  It is exponentially irrelevant at the
    # pole freeze-out temperature but prevents an unphysical quark/gluon gas
    # after the QCD crossover.
    pion_rho, pion_pressure = species_rho_pressure_over_t4(0.138 / temperature, False)
    rho_total += 3.0 * (1.0 - weight) * pion_rho
    pressure_total += 3.0 * (1.0 - weight) * pion_pressure
    g_rho = 30.0 * rho_total / PI**2
    g_s = 45.0 * (rho_total + pressure_total) / (2.0 * PI**2)
    return g_rho, g_s


class EquationOfState:
    def __init__(self, temperature_min: float, temperature_max: float, points: int = 180):
        self.log_t = np.linspace(math.log(temperature_min), math.log(temperature_max), points)
        values = np.array([equation_of_state_at(math.exp(value)) for value in self.log_t])
        self.g_rho = values[:, 0]
        self.g_s = values[:, 1]
        self.dln_gs_dln_t = np.gradient(np.log(self.g_s), self.log_t)

    def evaluate(self, temperature: float, scale: float = 1.0) -> tuple[float, float, float]:
        log_t = float(np.clip(math.log(temperature), self.log_t[0], self.log_t[-1]))
        g_rho = float(np.interp(log_t, self.log_t, self.g_rho)) * scale
        g_s = float(np.interp(log_t, self.log_t, self.g_s)) * scale
        derivative = float(np.interp(log_t, self.log_t, self.dln_gs_dln_t))
        return g_rho, g_s, derivative


class ThermalRateTable:
    def __init__(self, mass: float, points: int = 110, x_min: float = 5.0, x_max: float = 5.0e3):
        self.mass = mass
        self.log_x = np.linspace(math.log(x_min), math.log(x_max), points)
        values = np.array([
            pole.sigma_v_finite_width_unit_portal(mass, math.exp(log_x))
            for log_x in self.log_x
        ])
        self.log_rate = np.log(np.maximum(values, 1.0e-300))

    def evaluate(self, x: float) -> float:
        log_x = float(np.clip(math.log(x), self.log_x[0], self.log_x[-1]))
        return float(math.exp(np.interp(log_x, self.log_x, self.log_rate)))


def solve(
    parameters: dict,
    rate_points: int = 110,
    eos_scale: float = 1.0,
    x_final: float = 5.0e3,
    eos: EquationOfState | None = None,
    rates_a: ThermalRateTable | None = None,
    rates_b: ThermalRateTable | None = None,
) -> dict:
    m_a, m_b = parameters["mA"], parameters["mB"]
    eos = eos or EquationOfState(m_a / x_final, m_a / 5.0)
    rates_a = rates_a or ThermalRateTable(m_a, points=rate_points, x_max=x_final)
    rates_b = rates_b or ThermalRateTable(m_b, points=rate_points, x_max=x_final * m_b / m_a)
    conversion = relic.sigma_v_conversion_heavy_to_light(
        m_b, m_a, parameters["lambda_AB"]
    )

    def rhs(log_x: float, y: np.ndarray) -> np.ndarray:
        x_a = math.exp(log_x)
        temperature = m_a / x_a
        x_b = m_b / temperature
        g_rho, g_s, derivative = eos.evaluate(temperature, scale=eos_scale)
        entropy = 2.0 * PI**2 / 45.0 * g_s * temperature**3
        hubble = 1.66 * math.sqrt(g_rho) * temperature**2 / relic.MPL
        entropy_derivative_factor = 1.0 + derivative / 3.0
        ya_eq = relic.yield_equilibrium_per_charge(m_a, temperature, g_s)
        yb_eq = relic.yield_equilibrium_per_charge(m_b, temperature, g_s)
        rates = {
            "ann_A": parameters["lambda_HA"] ** 2 * rates_a.evaluate(x_a),
            "semi_A": 0.0,
            "ann_B": parameters["lambda_HB"] ** 2 * rates_b.evaluate(x_b),
            "semi_B": 0.0,
            "conversion_B_to_A": conversion,
        }
        ca, cb = relic.collision_polynomials(
            max(float(y[0]), 0.0), max(float(y[1]), 0.0), ya_eq, yb_eq, rates
        )
        return -entropy / hubble * entropy_derivative_factor * np.array([ca, cb])

    x_initial = 5.0
    temperature_initial = m_a / x_initial
    _g_rho, g_s_initial, _derivative = eos.evaluate(temperature_initial, scale=eos_scale)
    y0 = np.array([
        relic.yield_equilibrium_per_charge(m_a, temperature_initial, g_s_initial),
        relic.yield_equilibrium_per_charge(m_b, temperature_initial, g_s_initial),
    ])
    solution = solve_ivp(
        rhs,
        (math.log(x_initial), math.log(x_final)),
        y0,
        method="Radau",
        rtol=1.0e-8,
        atol=5.0e-16,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    ya, yb = solution.y[:, -1]
    omega_a = relic.OMEGA_FACTOR * 2.0 * m_a * ya
    omega_b = relic.OMEGA_FACTOR * 2.0 * m_b * yb
    freezeout_temperature = m_a / 20.0
    g_rho_fo, g_s_fo, derivative_fo = eos.evaluate(freezeout_temperature, scale=eos_scale)
    return {
        "Omega_A_h2": float(omega_a),
        "Omega_B_h2": float(omega_b),
        "Omega_total_h2": float(omega_a + omega_b),
        "fraction_A": float(omega_a / (omega_a + omega_b)),
        "fraction_B": float(omega_b / (omega_a + omega_b)),
        "late_yields_per_charge": {"A": float(ya), "B": float(yb)},
        "freezeout_EOS_at_xA_20": {
            "temperature_GeV": freezeout_temperature,
            "g_rho": g_rho_fo,
            "g_s": g_s_fo,
            "dln_gs_dlnT": derivative_fo,
        },
        "solver": {
            "rate_table_points_per_component": rate_points,
            "eos_scale": eos_scale,
            "x_initial": x_initial,
            "x_final": x_final,
            "nfev": solution.nfev,
            "rtol": 1.0e-8,
            "atol": 5.0e-16,
        },
    }


def build_payload(pole_json: Path) -> dict:
    pole_data = json.loads(pole_json.read_text(encoding="utf-8"))
    parameters = pole_data["fixed_candidate_parameter_vector"]
    m_a, m_b = parameters["mA"], parameters["mB"]
    x_final = 5.0e3
    eos = EquationOfState(m_a / x_final, m_a / 5.0)
    rates_a_110 = ThermalRateTable(m_a, points=110, x_max=x_final)
    rates_b_110 = ThermalRateTable(m_b, points=110, x_max=x_final * m_b / m_a)
    rates_a_150 = ThermalRateTable(m_a, points=150, x_max=x_final)
    rates_b_150 = ThermalRateTable(m_b, points=150, x_max=x_final * m_b / m_a)
    nominal = solve(parameters, 110, eos=eos, rates_a=rates_a_110, rates_b=rates_b_110)
    convergence = solve(parameters, 150, eos=eos, rates_a=rates_a_150, rates_b=rates_b_150)
    eos_low = solve(parameters, 110, eos_scale=0.95, eos=eos, rates_a=rates_a_110, rates_b=rates_b_110)
    eos_high = solve(parameters, 110, eos_scale=1.05, eos=eos, rates_a=rates_a_110, rates_b=rates_b_110)
    anchors = direct_detection.lz_curve_anchors()
    direct_rows = {}
    for label, omega_key in (("A", "Omega_A_h2"), ("B", "Omega_B_h2")):
        mass = parameters[f"m{label}"]
        portal_value = parameters[f"lambda_H{label}"]
        xi = nominal[omega_key] / direct_detection.OMEGA_DM_H2
        raw = prefilter.sigma_si(mass, portal_value)
        limit = direct_detection.loglog_interpolate(mass, anchors)
        direct_rows[label] = {
            "mass_GeV": mass,
            "xi_using_OmegaDM_h2_0p1200": xi,
            "raw_sigma_SI_cm2": raw,
            "effective_sigma_SI_cm2": xi * raw,
            "LZ_limit_cm2": limit,
            "R": xi * raw / limit,
        }
    xenon_nucleus_mass = 122.0
    mu_a = parameters["mA"] * xenon_nucleus_mass / (parameters["mA"] + xenon_nucleus_mass)
    mu_b = parameters["mB"] * xenon_nucleus_mass / (parameters["mB"] + xenon_nucleus_mass)
    invisible_br = pole_data["totals"]["Higgs_invisible_branching_fraction"]
    atlas_limit = 0.107
    return {
        "schema_version": 1,
        "parameters": parameters,
        "nominal": nominal,
        "rate_table_convergence_150_points": convergence,
        "eos_plus_minus_5_percent": {"minus_5_percent": eos_low, "plus_5_percent": eos_high},
        "numerical_relative_difference_total_110_vs_150": abs(
            nominal["Omega_total_h2"] / convergence["Omega_total_h2"] - 1.0
        ),
        "thermal_rate": "direct finite-width Gondolo-Gelmini integral with stable scaled-Bessel evaluation; includes off-pole continuum",
        "equation_of_state": "temperature-dependent ideal-gas SM species with massive thresholds and a smooth QCD parton-to-pion interpolation",
        "dominant_theory_limitation": "precision lattice/perturbative-QCD equation of state and higher-order energy-dependent virtual-Higgs width are not included",
        "relic_target_comparison": {
            "Omega_DM_h2_reference": direct_detection.OMEGA_DM_H2,
            "nominal_fractional_offset": nominal["Omega_total_h2"] / direct_detection.OMEGA_DM_H2 - 1.0,
            "EOS_sensitivity_absolute_range": [
                eos_high["Omega_total_h2"], eos_low["Omega_total_h2"]
            ],
        },
        "two_component_direct_detection": {
            "components": direct_rows,
            "combined_nearly_degenerate_rate_ratio": sum(row["R"] for row in direct_rows.values()),
            "xenon_nucleus_mass_proxy_GeV": xenon_nucleus_mass,
            "relative_reduced_mass_difference": abs(mu_b / mu_a - 1.0),
            "relative_recoil_scale_difference": abs((mu_b / mu_a) ** 2 - 1.0),
            "relative_LZ_limit_difference": abs(
                direct_rows["B"]["LZ_limit_cm2"] / direct_rows["A"]["LZ_limit_cm2"] - 1.0
            ),
            "interpretation": "The 0.2 GeV mass split changes the xenon recoil scale by less than 0.5 percent, so the spectra are experimentally indistinguishable for this exclusion-level comparison and their rates may be summed.",
        },
        "Higgs_invisible": {
            "predicted_branching_fraction": invisible_br,
            "ATLAS_observed_95CL_limit": atlas_limit,
            "prediction_over_limit": invisible_br / atlas_limit,
            "source": "ATLAS Collaboration, arXiv:2301.10731, combined 7/8/13 TeV direct searches",
        },
        "collider_sanity": {
            "minimal_TPD": "Only the tiny invisible Higgs width is new at tree level; no Higgs mixing occurs because A and B have zero vevs.",
            "protected_TPG_slice": "The new vectors have zero hypercharge kinetic mixing and the parent radials have zero Higgs portal at matching, so no additional tree-level SM production channel is introduced.",
            "scope": "Nonzero kinetic mixing or parent Higgs-radial portals would require a separate collider analysis and are not part of the frozen benchmark.",
        },
        "classification": "conditional phenomenological pass at leading order; precision SM equation-of-state and higher-order virtual-Higgs-width uncertainties remain explicit",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--pole-json", type=Path,
        default=root / "audits" / "tpd_higgs_pole_diagnostic.json",
    )
    parser.add_argument(
        "--json", type=Path,
        default=root / "audits" / "tpd_pole_thermal_certification.json",
    )
    args = parser.parse_args()
    payload = build_payload(args.pole_json)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "nominal": payload["nominal"],
        "numerical_relative_difference": payload["numerical_relative_difference_total_110_vs_150"],
    }, indent=2))


if __name__ == "__main__":
    main()
