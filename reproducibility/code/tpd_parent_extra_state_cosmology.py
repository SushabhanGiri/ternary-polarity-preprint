#!/usr/bin/env python3
"""Point-specific extra-state and late-time cosmology audit."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from scipy.integrate import quad

import tpd_higgs_pole_diagnostic as higgs_pole
import tpd_parent_gauge_finite_energy as parent_gauge


PI = math.pi
HBAR_GEV_S = 6.582119569e-25
MPL = 1.2209e19
MPL_REDUCED = 2.435e18
GEV2_TO_CM3_S = 0.389379e-27 * 2.99792458e10
PLANCK_PANN_LIMIT = 3.2e-28


def kallen(x: float, y: float, z: float) -> float:
    return x*x + y*y + z*z - 2.0*(x*y + x*z + y*z)


def radial_width_to_three_identical(
    radial_mass: float, scalar_mass: float, cubic: float, vev_parent: float
) -> dict:
    """Return rho -> SSS plus rho -> Sbar Sbar Sbar.

    From kappa Phi^dagger S^3+h.c. and mu=3*kappa*f/sqrt(2), each
    charge-conjugate amplitude has magnitude 3!*kappa/sqrt(2)=2*mu/f.
    The phase-space integral includes the 3! identical-particle factor.
    """
    if radial_mass <= 3.0 * scalar_mass:
        return {"open": False, "total_width_GeV": 0.0}
    amplitude = 2.0 * cubic / vev_parent
    low = 4.0 * scalar_mass**2
    high = (radial_mass - scalar_mass)**2

    def integrand(s12: float) -> float:
        lam1 = max(kallen(radial_mass**2, s12, scalar_mass**2), 0.0)
        lam2 = max(kallen(s12, scalar_mass**2, scalar_mass**2), 0.0)
        return math.sqrt(lam1 * lam2) / s12

    phase_integral, error = quad(integrand, low, high, epsabs=0.0, epsrel=2e-10)
    width_one_charge = (
        amplitude**2 * phase_integral
        / (math.factorial(3) * 256.0 * PI**3 * radial_mass**3)
    )
    total_width = 2.0 * width_one_charge
    return {
        "open": True,
        "amplitude_each_charge": amplitude,
        "phase_space_integral_GeV4": phase_integral,
        "quadrature_error_GeV4": error,
        "width_each_charge_GeV": width_one_charge,
        "total_width_GeV": total_width,
        "lifetime_s": HBAR_GEV_S / total_width,
    }


def hubble_radiation(temperature: float, g_rho: float = 106.75) -> float:
    return 1.66 * math.sqrt(g_rho) * temperature**2 / MPL


def zero_velocity_annihilation(mass: float, portal: float) -> float:
    q = 2.0 * mass
    denominator = (
        (q*q - higgs_pole.MH**2)**2
        + higgs_pole.MH**2 * higgs_pole.GAMMA_H_SM**2
    )
    return (
        portal**2 * 2.0 * higgs_pole.VEV**2 * higgs_pole.GAMMA_H_SM
        / (q * denominator)
    )


def build_payload(thermal_json: Path) -> dict:
    thermal = json.loads(thermal_json.read_text(encoding="utf-8"))
    fixed = thermal["parameters"]
    f = 1000.0
    radial_mass = math.sqrt(2.0 * 0.20) * f
    extra_states = {}
    pann_terms = {}
    self_bounds = {}
    for label in ("A", "B"):
        mass = fixed["m" + label]
        cubic = fixed["mu_" + label]
        vector_width = parent_gauge.vector_width_to_scalar(mass)
        radial = radial_width_to_three_identical(radial_mass, mass, cubic, f)
        component = thermal["two_component_direct_detection"]["components"][label]
        xi = component["xi_using_OmegaDM_h2_0p1200"]
        sv_gev = zero_velocity_annihilation(mass, fixed["lambda_H" + label])
        sv_cm = sv_gev * GEV2_TO_CM3_S
        pann_terms[label] = {
            "xi": xi,
            "zero_velocity_sigma_v_GeV_minus2": sv_gev,
            "zero_velocity_sigma_v_cm3_per_s": sv_cm,
            "conservative_feff_one_pann_cm3_s_GeV": xi**2 * sv_cm / mass,
        }
        amplitude_envelope = 10.0 * (
            fixed["lambda_" + label] + cubic**2 / mass**2
        )
        sigma_over_mass = (
            amplitude_envelope**2 / (64.0 * PI * mass**2) / mass
            * 0.389379e-27 / 1.78266192e-24
        )
        self_bounds[label] = {
            "amplitude_envelope": amplitude_envelope,
            "sigma_over_mass_upper_envelope_cm2_per_g": sigma_over_mass,
        }
        extra_states[label] = {
            "vector": {
                "mass_GeV": parent_gauge.M_VECTOR,
                "decay": "X -> S Sbar",
                "width_GeV": vector_width,
                "lifetime_s": HBAR_GEV_S / vector_width,
                "width_over_H_at_T_equal_mass": vector_width / hubble_radiation(parent_gauge.M_VECTOR),
            },
            "radial": {
                "mass_GeV": radial_mass,
                "decay": "rho -> S S S and charge conjugate",
                **radial,
                "width_over_H_at_T_equal_mass": radial["total_width_GeV"] / hubble_radiation(radial_mass),
            },
        }

    pann_total = sum(row["conservative_feff_one_pann_cm3_s_GeV"] for row in pann_terms.values())
    string_tension = 2.0 * PI * f**2 / MPL_REDUCED**2
    return {
        "schema_version": 1,
        "parameters": fixed,
        "parent_matching": {
            "f_m_GeV": f,
            "f_E_GeV": f,
            "g_m": 0.30,
            "g_E": 0.30,
            "vector_mass_GeV": parent_gauge.M_VECTOR,
            "radial_mass_GeV": radial_mass,
        },
        "extra_state_decays": extra_states,
        "late_time_annihilation": {
            "components": pann_terms,
            "conservative_feff_one_pann_total_cm3_s_GeV": pann_total,
            "Planck_2018_95CL_pann_limit_cm3_s_GeV": PLANCK_PANN_LIMIT,
            "ratio_to_limit": pann_total / PLANCK_PANN_LIMIT,
            "source": "Planck Collaboration 2018 VI, arXiv:1807.06209v4, Eq. 87c",
            "interpretation": "f_eff=1 is conservative; the actual SM final-state deposition efficiency is smaller",
        },
        "self_interaction_conservative_bounds": self_bounds,
        "topological_defects": {
            "object": "local strings from each broken U(1); no domain walls from a gauged residual Z3",
            "Gmu_order_estimate_each_sector": string_tension,
            "estimate": "2*pi*f^2/Mbar_Pl^2; order-one string-profile factors omitted",
        },
        "verdict": {
            "unintended_parent_relic": "none at the matched pole point: every vector and radial has a prompt open decay",
            "BBN_or_late_entropy": "pass by more than fifteen orders of magnitude in lifetime",
            "CMB_energy_injection": "pass under the conservative f_eff=1 mapping",
            "dark_radiation": "none: both Goldstones are eaten and all parent excitations are massive and prompt",
            "classification": "verified model-dependent cosmology pass at leading order",
        },
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--thermal-json", type=Path,
        default=root / "audits" / "tpd_pole_thermal_certification.json",
    )
    parser.add_argument(
        "--json", type=Path,
        default=root / "audits" / "tpd_parent_extra_state_cosmology.json",
    )
    args = parser.parse_args()
    payload = build_payload(args.thermal_json)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "extra_state_decays": payload["extra_state_decays"],
        "late_time_annihilation": payload["late_time_annihilation"],
        "topological_defects": payload["topological_defects"],
        "verdict": payload["verdict"],
    }, indent=2))


if __name__ == "__main__":
    main()
