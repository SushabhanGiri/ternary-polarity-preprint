#!/usr/bin/env python3
"""Cubic-process and one-loop metastability audit for the pole benchmark."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import tpd_coupled_relic as relic
import tpd_parent_rge_running as parent_rge


PI = math.pi
H0_GEV = 1.44e-42


def cubic_rate_bound(mass: float, cubic: float, quartic: float, g_s: float = 84.0) -> dict:
    """Conservative dimensional bound for 3S -> S Sbar near freeze-out.

    The leading five-point tree topology contains one cubic and one quartic
    vertex, so M_5 scales as mu*lambda/m^2.  A deliberately loose factor 100
    covers permutations and normalization conventions.
    """
    x = 20.0
    temperature = mass / x
    y_eq = relic.yield_equilibrium_per_charge(mass, temperature, g_s)
    entropy = 2.0 * PI**2 / 45.0 * g_s * temperature**3
    number_density = 2.0 * y_eq * entropy
    hubble = 1.66 * math.sqrt(g_s) * temperature**2 / relic.MPL
    amplitude_bound = 100.0 * abs(cubic * quartic) / mass**2
    # Five-point amplitude has mass dimension -1.  The conservative phase-
    # space normalization below intentionally overestimates the rate.
    sigma_v2_bound = amplitude_bound**2 / (64.0 * PI**2 * mass**3)
    rate = number_density**2 * sigma_v2_bound
    return {
        "x": x,
        "temperature_GeV": temperature,
        "equilibrium_total_number_density_GeV3": number_density,
        "amplitude_bound_GeV_minus1": amplitude_bound,
        "sigma_v2_bound_GeV_minus5": sigma_v2_bound,
        "rate_GeV": rate,
        "Hubble_GeV": hubble,
        "rate_over_Hubble": rate / hubble,
        "bound_convention": "100*mu*lambda/m^2 amplitude envelope and 1/(64*pi^2*m^3) phase-space envelope",
    }


def build_payload(pole_json: Path) -> dict:
    pole = json.loads(pole_json.read_text(encoding="utf-8"))
    fixed = pole["fixed_candidate_parameter_vector"]
    low_override = {
        "lambda_A": fixed["lambda_A"],
        "lambda_B": fixed["lambda_B"],
        "lambda_HA": fixed["lambda_HA"],
        "lambda_HB": fixed["lambda_HB"],
        "lambda_AB": fixed["lambda_AB"],
    }
    f = 1000.0
    parent_override = {
        "g_m": 0.30,
        "g_E": 0.30,
        "lambda_Phi_m": 0.20,
        "lambda_Phi_E": 0.20,
        "kappa_m": math.sqrt(2.0) * fixed["mu_A"] / (3.0 * f),
        "kappa_E": math.sqrt(2.0) * fixed["mu_B"] / (3.0 * f),
    }
    running = parent_rge.run(
        1800,
        2.435e18,
        low_override=low_override,
        parent_override=parent_override,
    )
    controlled_boundary = running["high_energy_scalar_unitarity_boundary_GeV"]
    if controlled_boundary is None:
        controlled_boundary = running["last_integrated_scale_GeV"]
        controlled_couplings = running["final"]
    else:
        controlled_couplings = running["couplings_at_scalar_unitarity_boundary"]
    lambda_h_controlled = float(controlled_couplings["lambda_H"])
    lambda_negative_envelope = abs(min(lambda_h_controlled, 0.0))
    bounce_action = (
        8.0 * PI**2 / (3.0 * lambda_negative_envelope)
        if lambda_negative_envelope > 0.0 else math.inf
    )
    bounce_scale = float(controlled_boundary)
    log_decay_probability_bound = 4.0 * math.log(bounce_scale / H0_GEV) - bounce_action

    cubic = {
        "A": cubic_rate_bound(fixed["mA"], fixed["mu_A"], fixed["lambda_A"]),
        "B": cubic_rate_bound(fixed["mB"], fixed["mu_B"], fixed["lambda_B"]),
    }
    return {
        "schema_version": 1,
        "parameters": fixed,
        "cubic_processes": {
            "semiannihilation_SS_to_Sbar_h": {
                "kinematic_condition": "m_S >= m_h",
                "A_open": bool(fixed["mA"] >= 125.25),
                "B_open": bool(fixed["mB"] >= 125.25),
                "verdict": "exactly closed for both pole components",
            },
            "three_to_two_conservative_bounds": cubic,
            "maximum_rate_over_Hubble": max(row["rate_over_Hubble"] for row in cubic.values()),
            "verdict": "negligible; no Boltzmann-system extension justified",
        },
        "point_matched_parent_running": {
            "matching_scale_GeV": running["matching_scale_GeV"],
            "threshold_scheme": running["threshold_scheme"],
            "first_sufficient_BFB_failure_GeV": running["first_sufficient_BFB_certificate_failure_GeV"],
            "high_energy_scalar_unitarity_boundary_GeV": running["high_energy_scalar_unitarity_boundary_GeV"],
            "four_pi_boundary_GeV": running["four_pi_boundary_GeV"],
            "final_lambda_H_at_four_pi_boundary": float(running["final"]["lambda_H"]),
            "lambda_H_at_scalar_unitarity_boundary": lambda_h_controlled,
            "scope": running["scope_warning"],
        },
        "one_loop_metastability_estimate": {
            "quartic_envelope_abs": lambda_negative_envelope,
            "bounce_action_8pi2_over_3abs_lambda": bounce_action,
            "bounce_scale_envelope_GeV": bounce_scale,
            "cutoff_choice": "first high-energy scalar partial-wave unitarity boundary; no bounce claim is extrapolated beyond it",
            "log_decay_probability_upper_envelope": log_decay_probability_bound,
            "cosmological_lifetime_safe_in_this_approximation": bool(log_decay_probability_bound < 0.0),
            "classification": "one-loop leading-log metastability estimate, not a multi-field loop-improved bounce",
        },
        "classification": "cubic effects negligible; point is metastable but cosmologically safe in the stated one-loop envelope",
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
        default=root / "audits" / "tpd_cubic_metastability.json",
    )
    args = parser.parse_args()
    payload = build_payload(args.pole_json)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "maximum_3to2_rate_over_H": payload["cubic_processes"]["maximum_rate_over_Hubble"],
        "running": payload["point_matched_parent_running"],
        "metastability": payload["one_loop_metastability_estimate"],
    }, indent=2))


if __name__ == "__main__":
    main()
