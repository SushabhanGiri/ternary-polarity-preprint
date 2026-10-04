#!/usr/bin/env python3
"""Reproducible leading-order TP-D relic-density parameter scan.

This is a triage scan, not a likelihood analysis.  It applies the exact
tree-level copositivity test, the simple sufficient inert-vacuum certificate,
and the exact high-energy scalar-quartic eigenvalue test before solving the
leading coupled Boltzmann equations.  It deliberately does *not* declare a
point experimentally viable: exact detector-limit curves and precision
thermal averages are separate downstream gates.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict
from pathlib import Path

import numpy as np

import tpd_coupled_relic as relic
import tpd_ew_vacuum as vacuum
import tpd_high_energy_unitarity as unitarity
import tpd_phenomenology_prefilter as prefilter


V = relic.VEV
MH = relic.MH
LAMBDA_H = MH**2 / (2.0 * V**2)
PLANCK_OMEGA = 0.1200


def log_uniform(rng: np.random.Generator, low: float, high: float) -> float:
    return float(math.exp(rng.uniform(math.log(low), math.log(high))))


def draw_point(rng: np.random.Generator) -> dict[str, float]:
    m_a = log_uniform(rng, 130.0, 1500.0)
    m_b = m_a * log_uniform(rng, 1.05, 3.0)
    lambda_a = log_uniform(rng, 0.05, 1.0)
    lambda_b = log_uniform(rng, 0.05, 1.0)
    lambda_ha = log_uniform(rng, 0.002, 0.25)
    lambda_hb = log_uniform(rng, 0.002, 0.25)
    lambda_ab = log_uniform(rng, 0.002, 0.8)

    m_a2 = m_a**2 - 0.5 * lambda_ha * V**2
    m_b2 = m_b**2 - 0.5 * lambda_hb * V**2
    if m_a2 <= 0.0 or m_b2 <= 0.0:
        return {}

    # Fractions of the sufficient one-field global-vacuum bounds.
    frac_a = rng.uniform(0.35, 0.995)
    frac_b = rng.uniform(0.35, 0.995)
    mu_a = float(frac_a * math.sqrt(9.0 * lambda_a * m_a2))
    mu_b = float(frac_b * math.sqrt(9.0 * lambda_b * m_b2))
    return {
        "mA": m_a,
        "mB": m_b,
        "mu_A": mu_a,
        "mu_B": mu_b,
        "lambda_HA": lambda_ha,
        "lambda_HB": lambda_hb,
        "lambda_AB": lambda_ab,
        "lambda_A": lambda_a,
        "lambda_B": lambda_b,
        "cubic_fraction_A": float(frac_a),
        "cubic_fraction_B": float(frac_b),
        "bare_mA2": float(m_a2),
        "bare_mB2": float(m_b2),
    }


def internal_consistency(point: dict[str, float]) -> dict[str, object]:
    p = vacuum.Parameters(
        mu_h2=LAMBDA_H * V**2,
        m_a2=point["bare_mA2"],
        m_b2=point["bare_mB2"],
        mu_a=point["mu_A"],
        mu_b=point["mu_B"],
        lambda_h=LAMBDA_H,
        lambda_a=point["lambda_A"],
        lambda_b=point["lambda_B"],
        lambda_ha=point["lambda_HA"],
        lambda_hb=point["lambda_HB"],
        lambda_ab=point["lambda_AB"],
    )
    bfb = vacuum.copositive_bfb(p)
    sufficient = vacuum.sufficient_global_ew(p)
    couplings = {
        "lambda_H": LAMBDA_H,
        "lambda_A": point["lambda_A"],
        "lambda_B": point["lambda_B"],
        "lambda_HA": point["lambda_HA"],
        "lambda_HB": point["lambda_HB"],
        "lambda_AB": point["lambda_AB"],
    }
    radius = float(np.max(np.abs(unitarity.analytic_spectrum(couplings))))
    return {
        "bfb": bfb,
        "sufficient_global_conditions": sufficient,
        "sufficient_global_pass": bool(all(sufficient.values())),
        "high_energy_scalar_unitarity_radius": radius,
        "high_energy_scalar_unitarity_pass": bool(radius <= 8.0 * math.pi),
        "parameters_for_vacuum": asdict(p),
    }


def direct_detection_observables(point: dict[str, float], omega: dict[str, float]) -> dict[str, float]:
    sigma_a = prefilter.sigma_si(point["mA"], point["lambda_HA"])
    sigma_b = prefilter.sigma_si(point["mB"], point["lambda_HB"])
    return {
        "sigma_A_cm2": sigma_a,
        "sigma_B_cm2": sigma_b,
        "fraction_rescaled_sigma_A_cm2": omega["fraction_A"] * sigma_a,
        "fraction_rescaled_sigma_B_cm2": omega["fraction_B"] * sigma_b,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=int, default=160)
    parser.add_argument("--seed", type=int, default=20260919)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    accepted: list[dict[str, object]] = []
    failed_internal = 0
    solver_failures = 0

    for index in range(args.points):
        point = draw_point(rng)
        if not point:
            failed_internal += 1
            continue
        consistency = internal_consistency(point)
        if not (
            consistency["bfb"]["passes"]
            and consistency["sufficient_global_pass"]
            and consistency["high_energy_scalar_unitarity_pass"]
        ):
            failed_internal += 1
            continue
        relic_parameters = {
            key: point[key]
            for key in ("mA", "mB", "mu_A", "mu_B", "lambda_HA", "lambda_HB", "lambda_AB")
        }
        try:
            relic_result = relic.solve_coupled_freezeout(relic_parameters)
        except RuntimeError:
            solver_failures += 1
            continue
        omega = relic_result["omega_h2"]
        accepted.append(
            {
                "sample_index": index,
                "parameters": point,
                "consistency": consistency,
                "omega_h2": omega,
                "absolute_relic_residual": abs(omega["total"] - PLANCK_OMEGA),
                "direct_detection": direct_detection_observables(point, omega),
                "rates_GeV_minus2": relic_result["rates_GeV_minus2"],
            }
        )

    accepted.sort(key=lambda row: row["absolute_relic_residual"])
    near_relic = [
        row for row in accepted if 0.10 <= row["omega_h2"]["total"] <= 0.14
    ]
    payload = {
        "schema_version": 1,
        "status": "leading-order triage scan; not a precision likelihood or viability certification",
        "sampling": {
            "requested_points": args.points,
            "seed": args.seed,
            "ranges": {
                "mA_GeV": "log-uniform [130,1500]",
                "mB_over_mA": "log-uniform [1.05,3]",
                "lambda_A_lambda_B": "log-uniform [0.05,1]",
                "lambda_HA_lambda_HB": "log-uniform [0.002,0.25]",
                "lambda_AB": "log-uniform [0.002,0.8]",
                "cubic_fraction_of_sufficient_bound": "uniform [0.35,0.995]",
            },
            "accepted_internal": len(accepted),
            "failed_internal": failed_internal,
            "solver_failures": solver_failures,
        },
        "filters": {
            "tree_BFB": "exact three-field copositivity",
            "global_vacuum": "sufficient, not necessary, inert-EW certificate",
            "unitarity": "exact eigenvalues of high-energy scalar quartic matrix; |Lambda|<=8*pi",
            "relic_target_window": [0.10, 0.14],
            "direct_detection": "computed but not cut; official mass-dependent limit not yet ingested",
        },
        "near_relic_count": len(near_relic),
        "near_relic_points": near_relic,
        "best_20_by_relic_residual": accepted[:20],
        "limitations": [
            "threshold rather than thermally averaged cross sections",
            "constant g*=g*s=90",
            "tree-level rates",
            "restricted hierarchy mB>mA",
            "no resonant Higgs region below 130 GeV",
            "no experimental exclusions applied",
        ],
    }
    rendered = json.dumps(payload, indent=2)
    output = args.json or (Path(__file__).resolve().parents[1] / "audits" / "tpd_relic_parameter_scan.json")
    output.write_text(rendered + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "accepted_internal": len(accepted),
        "near_relic_count": len(near_relic),
        "best_total_omega": accepted[0]["omega_h2"]["total"] if accepted else None,
        "best_residual": accepted[0]["absolute_relic_residual"] if accepted else None,
    }, indent=2))


if __name__ == "__main__":
    main()
