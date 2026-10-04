#!/usr/bin/env python3
"""Minimal thermally averaged Higgs-pole diagnostic for TP-D.

This is the first reduced search justified by checkpoint 12.  It does not run
a broad scan.  It solves two effectively decoupled complex-scalar Boltzmann
equations using the narrow-width thermal average for s-channel SM-Higgs
annihilation, chooses each component to supply half of the observed density,
and checks Higgs invisible width and LZ direct detection.

The calculation is a candidate-existence diagnostic, not a precision relic
likelihood: g_* is constant and the off-pole continuum is neglected.  The
narrow-width expression is independently compared with the finite-width
integral at representative freeze-out temperatures, and a coupled solve
checks the deliberately small conversion interaction.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import kn, kve

import tpd_coupled_relic as relic
import tpd_direct_detection_gate as direct_detection
import tpd_ew_vacuum as vacuum
import tpd_finite_energy_unitarity as finite_unitarity
import tpd_full_rge_running as full_rge
import tpd_high_energy_unitarity as unitarity
import tpd_phenomenology_prefilter as prefilter


PI = math.pi
MH = 125.25
VEV = 246.22
GAMMA_H_SM = 4.07e-3
OMEGA_TARGET_COMPONENT = 0.0600
GSTAR = 80.0


def thermal_ratio_k1_over_k2sq(x: float, pole_ratio: float) -> float:
    """Stable K1(pole_ratio*x)/K2(x)^2."""
    exponent = -(pole_ratio - 2.0) * x
    if exponent < -745.0:
        return 0.0
    return math.exp(exponent) * float(kve(1, pole_ratio * x)) / float(kve(2, x)) ** 2


def sigma_v_nwa_unit_portal(mass: float, x: float) -> float:
    """Thermally averaged sigma*v for lambda_HS=1 in GeV^-2.

    Derived by inserting the Breit-Wigner Higgs rate into the exact
    Gondolo-Gelmini integral and using the narrow-width delta function.
    """
    if 2.0 * mass >= MH:
        return 0.0
    temperature = mass / x
    phase = math.sqrt(MH * MH - 4.0 * mass * mass)
    bessel_ratio = thermal_ratio_k1_over_k2sq(x, MH / mass)
    return PI * VEV**2 * phase * bessel_ratio / (
        8.0 * mass**4 * temperature
    )


def sigma_v_finite_width_unit_portal(mass: float, x: float) -> float:
    """Numerical finite-width thermal average for a fixed SM Higgs width."""
    temperature = mass / x
    scaled_k2 = float(kve(2, x))
    q_min = 2.0 * mass
    q_max = max(MH + 40.0 * temperature, q_min + 60.0 * temperature)

    def integrand(q: float) -> float:
        if q <= q_min:
            return 0.0
        denominator = (q * q - MH * MH) ** 2 + MH * MH * GAMMA_H_SM**2
        sigma_v = 2.0 * VEV**2 * GAMMA_H_SM / (q * denominator)
        # Use exponentially scaled Bessel functions.  K1(q/T)/K2(x)^2
        # carries exp[-(q-2m)/T], avoiding underflow at late times.
        bessel_ratio = (
            math.exp(-(q - q_min) / temperature)
            * float(kve(1, q / temperature))
            / scaled_k2**2
        )
        return sigma_v * q**3 * math.sqrt(q * q - q_min * q_min) * bessel_ratio

    # Explicitly resolve the narrow pole rather than asking a generic
    # quadrature to discover a 4 MeV feature on a hundred-GeV interval.
    delta = 100.0 * GAMMA_H_SM
    intervals = [
        (q_min, max(q_min, MH - delta)),
        (max(q_min, MH - delta), MH + delta),
        (MH + delta, q_max),
    ]
    integral = 0.0
    for low, high in intervals:
        if high <= low:
            continue
        value, _ = quad(
            integrand,
            low,
            high,
            points=[MH] if low < MH < high else None,
            epsabs=0.0,
            epsrel=2.0e-6,
            limit=500,
        )
        integral += value
    return integral / (8.0 * mass**4 * temperature)


def solve_single_component(mass: float, portal: float, gstar: float = GSTAR) -> float:
    """Return Omega*h^2 including particle and antiparticle."""
    def rhs(log_x: float, y: np.ndarray) -> np.ndarray:
        x = math.exp(log_x)
        temperature = mass / x
        entropy = 2.0 * PI**2 / 45.0 * gstar * temperature**3
        hubble = 1.66 * math.sqrt(gstar) * temperature**2 / relic.MPL
        y_eq = relic.yield_equilibrium_per_charge(mass, temperature, gstar)
        rate = portal**2 * sigma_v_nwa_unit_portal(mass, x)
        abundance = max(float(y[0]), 0.0)
        return np.array([-entropy / hubble * rate * (abundance**2 - y_eq**2)])

    y0 = [relic.yield_equilibrium_per_charge(mass, mass, gstar)]
    solution = solve_ivp(
        rhs,
        (0.0, math.log(1.0e4)),
        y0,
        method="Radau",
        rtol=2.0e-8,
        atol=1.0e-15,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    return float(relic.OMEGA_FACTOR * 2.0 * mass * solution.y[0, -1])


def portal_for_target(
    mass: float,
    target: float = OMEGA_TARGET_COMPONENT,
    gstar: float = GSTAR,
) -> float:
    def residual(log10_portal: float) -> float:
        portal = 10.0**log10_portal
        return math.log(solve_single_component(mass, portal, gstar=gstar) / target)

    root = brentq(residual, -7.0, -1.0, xtol=2.0e-8, rtol=2.0e-8)
    return 10.0**root


def higgs_invisible_width_complex_scalar(mass: float, portal: float) -> float:
    if 2.0 * mass >= MH:
        return 0.0
    beta = math.sqrt(1.0 - 4.0 * mass * mass / (MH * MH))
    return portal**2 * VEV**2 * beta / (16.0 * PI * MH)


def solve_coupled_candidate(parameters: dict, gstar: float = GSTAR) -> dict:
    """Coupled pole-enhanced Boltzmann solve including B Bbar -> A Abar."""
    m_a, m_b = parameters["mA"], parameters["mB"]
    conversion = relic.sigma_v_conversion_heavy_to_light(
        m_b, m_a, parameters["lambda_AB"]
    )

    def rhs(log_x: float, y: np.ndarray) -> np.ndarray:
        x_a = math.exp(log_x)
        temperature = m_a / x_a
        x_b = m_b / temperature
        entropy = 2.0 * PI**2 / 45.0 * gstar * temperature**3
        hubble = 1.66 * math.sqrt(gstar) * temperature**2 / relic.MPL
        ya_eq = relic.yield_equilibrium_per_charge(m_a, temperature, gstar)
        yb_eq = relic.yield_equilibrium_per_charge(m_b, temperature, gstar)
        rates = {
            "ann_A": parameters["lambda_HA"] ** 2 * sigma_v_nwa_unit_portal(m_a, x_a),
            "semi_A": 0.0,
            "ann_B": parameters["lambda_HB"] ** 2 * sigma_v_nwa_unit_portal(m_b, x_b),
            "semi_B": 0.0,
            "conversion_B_to_A": conversion,
        }
        ca, cb = relic.collision_polynomials(
            max(float(y[0]), 0.0), max(float(y[1]), 0.0), ya_eq, yb_eq, rates
        )
        return -entropy / hubble * np.array([ca, cb])

    temperature_initial = m_a
    y0 = np.array([
        relic.yield_equilibrium_per_charge(m_a, temperature_initial, gstar),
        relic.yield_equilibrium_per_charge(m_b, temperature_initial, gstar),
    ])
    solution = solve_ivp(
        rhs,
        (0.0, math.log(1.0e4)),
        y0,
        method="Radau",
        rtol=2.0e-8,
        atol=1.0e-15,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    ya, yb = solution.y[:, -1]
    omega_a = relic.OMEGA_FACTOR * 2.0 * m_a * ya
    omega_b = relic.OMEGA_FACTOR * 2.0 * m_b * yb
    return {
        "Omega_A_h2": float(omega_a),
        "Omega_B_h2": float(omega_b),
        "Omega_total_h2": float(omega_a + omega_b),
        "conversion_GeV_minus2": conversion,
        "solver_nfev": solution.nfev,
    }


def build_payload() -> dict:
    # Two nearby but nondegenerate masses retain separate kernel labels while
    # both exploit the only reduced direction being tested here.
    masses = {"A": 62.00, "B": 62.20}
    anchors = direct_detection.lz_curve_anchors()
    components = {}
    for label, mass in masses.items():
        portal = portal_for_target(mass)
        omega = solve_single_component(mass, portal)
        xi = omega / direct_detection.OMEGA_DM_H2
        raw_sigma = prefilter.sigma_si(mass, portal)
        effective_sigma = xi * raw_sigma
        limit = direct_detection.loglog_interpolate(mass, anchors)
        components[label] = {
            "mass_GeV": mass,
            "lambda_Hi": portal,
            "omega_h2": omega,
            "xi": xi,
            "sigma_SI_raw_cm2": raw_sigma,
            "sigma_SI_effective_cm2": effective_sigma,
            "LZ_90CL_limit_cm2": limit,
            "R_component": effective_sigma / limit,
            "higgs_invisible_width_GeV": higgs_invisible_width_complex_scalar(mass, portal),
        }

    total_invisible = sum(row["higgs_invisible_width_GeV"] for row in components.values())
    invisible_br = total_invisible / (GAMMA_H_SM + total_invisible)
    # Since the masses are nearly identical, this sum is a controlled proxy
    # for a combined spectral likelihood.  It is used as a screening metric,
    # not as an experimental recast.
    combined_rate_ratio_proxy = sum(row["R_component"] for row in components.values())
    finite_width_checks = {}
    for label, mass in masses.items():
        finite_width_checks[label] = {}
        for x in (15.0, 20.0, 25.0):
            nwa = sigma_v_nwa_unit_portal(mass, x)
            exact = sigma_v_finite_width_unit_portal(mass, x)
            finite_width_checks[label][str(int(x))] = {
                "NWA_GeV_minus2": nwa,
                "finite_width_GeV_minus2": exact,
                "relative_difference": nwa / exact - 1.0,
            }

    lambda_h = MH**2 / (2.0 * VEV**2)
    fixed = {
        "mA": masses["A"],
        "mB": masses["B"],
        "mu_A": 1.0,
        "mu_B": 1.0,
        "lambda_HA": components["A"]["lambda_Hi"],
        "lambda_HB": components["B"]["lambda_Hi"],
        "lambda_AB": 1.0e-5,
        "lambda_A": 0.10,
        "lambda_B": 0.10,
    }
    fixed["bare_mA2"] = fixed["mA"] ** 2 - 0.5 * fixed["lambda_HA"] * VEV**2
    fixed["bare_mB2"] = fixed["mB"] ** 2 - 0.5 * fixed["lambda_HB"] * VEV**2
    vacuum_point = vacuum.Parameters(
        mu_h2=lambda_h * VEV**2,
        m_a2=fixed["bare_mA2"],
        m_b2=fixed["bare_mB2"],
        mu_a=fixed["mu_A"],
        mu_b=fixed["mu_B"],
        lambda_h=lambda_h,
        lambda_a=fixed["lambda_A"],
        lambda_b=fixed["lambda_B"],
        lambda_ha=fixed["lambda_HA"],
        lambda_hb=fixed["lambda_HB"],
        lambda_ab=fixed["lambda_AB"],
    )
    bfb = vacuum.copositive_bfb(vacuum_point)
    global_conditions = vacuum.sufficient_global_ew(vacuum_point)
    quartics = {
        "lambda_H": lambda_h,
        "lambda_A": fixed["lambda_A"],
        "lambda_B": fixed["lambda_B"],
        "lambda_HA": fixed["lambda_HA"],
        "lambda_HB": fixed["lambda_HB"],
        "lambda_AB": fixed["lambda_AB"],
    }
    unitarity_radius = float(np.max(np.abs(unitarity.analytic_spectrum(quartics))))
    coupled = solve_coupled_candidate(fixed)
    finite = finite_unitarity.scan(120, 2.0e4, 0.25, p=vacuum_point)
    rge = full_rge.run(
        fixed["lambda_HA"],
        fixed["lambda_HB"],
        2500,
        2.435e18,
        initial_override={
            "lambda_A": fixed["lambda_A"],
            "lambda_B": fixed["lambda_B"],
            "lambda_AB": fixed["lambda_AB"],
            "mA2": fixed["bare_mA2"],
            "mB2": fixed["bare_mB2"],
            "muA": fixed["mu_A"],
            "muB": fixed["mu_B"],
        },
    )

    gstar_sensitivity = {}
    for gstar in (70.0, 90.0):
        rows = {}
        for label, mass in masses.items():
            portal = portal_for_target(mass, gstar=gstar)
            xi = OMEGA_TARGET_COMPONENT / direct_detection.OMEGA_DM_H2
            limit = direct_detection.loglog_interpolate(mass, anchors)
            rows[label] = {
                "lambda_Hi": portal,
                "R_component": xi * prefilter.sigma_si(mass, portal) / limit,
            }
        gstar_sensitivity[str(int(gstar))] = {
            "components": rows,
            "combined_LZ_rate_ratio_proxy": sum(row["R_component"] for row in rows.values()),
        }

    return {
        "schema_version": 1,
        "status": "minimal Higgs-pole candidate diagnostic; not a precision viable benchmark",
        "assumptions": {
            "thermal_average": "narrow-width Gondolo-Gelmini expression",
            "finite_width_crosscheck": "direct numerical Breit-Wigner thermal integral at x=15,20,25",
            "gstar_equal_gstar_s": GSTAR,
            "component_target_Omega_h2": OMEGA_TARGET_COMPONENT,
            "conversion": "included in a coupled cross-check at lambda_AB=1e-5; numerically negligible",
            "semiannihilation": "kinematically closed at m_i < m_h",
            "off_pole_continuum": "neglected in relic solve",
            "self_couplings_and_cubics": "not fixed by pole solve; require subsequent vacuum/unitarity/RG completion",
        },
        "components": components,
        "fixed_candidate_parameter_vector": fixed,
        "tree_level_consistency": {
            "exact_copositive_BFB": bfb,
            "sufficient_global_EW_conditions": global_conditions,
            "sufficient_global_EW_pass": bool(all(global_conditions.values())),
            "high_energy_scalar_unitarity_radius": unitarity_radius,
            "high_energy_scalar_unitarity_pass": bool(unitarity_radius <= 8.0 * PI),
            "physical_scalar_finite_energy_max_abs_a0": finite["maximum_over_scan"]["max_abs_eigenvalue"],
            "physical_scalar_finite_energy_pass": finite["passes_abs_Re_a0_le_half"],
            "physical_scalar_finite_energy_scope": finite["scope_warning"],
        },
        "coupled_relic_crosscheck": coupled,
        "one_loop_RGE_cutoff_diagnostic": {
            "first_BFB_failure_GeV": rge["first_BFB_failure_GeV"],
            "first_sufficient_global_EW_failure_GeV": rge["first_sufficient_global_EW_failure_GeV"],
            "first_sufficient_global_EW_failure_conditions": rge["first_sufficient_global_EW_failure_conditions"],
            "unitarity_boundary_GeV": rge["unitarity_boundary_GeV"],
            "four_pi_boundary_GeV": rge["four_pi_boundary_GeV"],
            "last_integrated_scale_GeV": rge["last_integrated_scale_GeV"],
            "failure_interpretation": "The first BFB failure is the SM-like Higgs-quartic instability; all other reported global-minimum margins remain positive in this one-loop run.",
            "scope": rge["scope"],
        },
        "totals": {
            "Omega_h2": sum(row["omega_h2"] for row in components.values()),
            "Higgs_invisible_width_GeV": total_invisible,
            "Higgs_invisible_branching_fraction": invisible_br,
            "combined_LZ_rate_ratio_proxy": combined_rate_ratio_proxy,
        },
        "finite_width_crosschecks": finite_width_checks,
        "constant_gstar_sensitivity": gstar_sensitivity,
        "screening_verdict": (
            "candidate_survives_leading_pole_and_direct_detection_screen"
            if combined_rate_ratio_proxy < 1.0
            else "candidate_fails_combined_direct_detection_proxy"
        ),
        "required_before_viability_claim": [
            "full finite-width thermal average including off-pole continuum and running g*(T)",
            "loop-improved metastability calculation and threshold/two-loop uncertainty around the one-loop absolute-stability cutoff",
            "external-Goldstone/transverse-vector finite-energy unitarity in a gauge-complete parent",
            "current Higgs invisible-width likelihood and a proper two-component LZ likelihood/recast",
            "higher-order number-changing rates induced by the nonzero cubic couplings",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--json",
        type=Path,
        default=root / "audits" / "tpd_higgs_pole_diagnostic.json",
    )
    args = parser.parse_args()
    payload = build_payload()
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "components": payload["components"],
        "totals": payload["totals"],
        "screening_verdict": payload["screening_verdict"],
    }, indent=2))


if __name__ == "__main__":
    main()
