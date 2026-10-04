#!/usr/bin/env python3
"""Leading quartic-bounce metastability diagnostic for TP-D benchmarks.

For a negative high-field Higgs quartic, the scale-invariant Fubini bounce has
S4 = 8*pi^2/(3*|lambda|).  This script evaluates that leading expression only
inside the interval preceding the first scalar-unitarity boundary.

It is intentionally not called a lifetime calculation: fluctuation
determinants, gauge-consistent effective couplings, threshold matching,
two-loop running, gravity, and higher-dimensional operators are omitted.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import tpd_full_rge_running as running


HBAR_GEV_S = 6.582119569e-25
YEAR_S = 365.25 * 24 * 3600
UNIVERSE_AGE_YEARS = 13.8e9


def diagnose(label: str, lambda_ha: float, lambda_hb: float, points: int) -> dict[str, object]:
    summary = running.run(lambda_ha, lambda_hb, points, 2.435e18)
    cutoff = min(
        value for value in (summary["unitarity_boundary_GeV"], summary["four_pi_boundary_GeV"])
        if value is not None
    )
    initial = summary["initial"]
    y0 = np.array([initial[name] for name in running.NAMES])
    t0, t1 = math.log(float(summary["mu0_GeV"])), math.log(float(cutoff))
    sol = solve_ivp(
        running.beta,
        (t0, t1),
        y0,
        dense_output=True,
        max_step=(t1 - t0) / 2500,
        rtol=2e-10,
        atol=1e-10,
        method="DOP853",
    )
    grid_t = np.linspace(t0, t1, points)
    trajectory = sol.sol(grid_t)
    lambda_h = trajectory[running.NAMES.index("lambda_H")]
    index = int(np.argmin(lambda_h))
    minimum = float(lambda_h[index])
    scale = float(math.exp(grid_t[index]))
    at_minimum = trajectory[:, index]
    beta_lambda_h = float(
        running.beta_numerator(at_minimum)[running.NAMES.index("lambda_H")] / running.LOOP
    )
    result: dict[str, object] = {
        "benchmark": label,
        "lambda_HA_initial": lambda_ha,
        "lambda_HB_initial": lambda_hb,
        "controlled_cutoff_GeV": cutoff,
        "cutoff_definition": "first high-energy scalar-unitarity or 4*pi boundary",
        "minimum_lambda_H": minimum,
        "minimum_scale_GeV": scale,
        "beta_lambda_H_at_minimum": beta_lambda_h,
        "minimum_at_scan_endpoint": index == len(grid_t) - 1,
        "first_BFB_failure_GeV": summary["first_BFB_failure_GeV"],
    }
    if minimum < 0:
        action = 8 * math.pi**2 / (3 * abs(minimum))
        age_gev_inverse = UNIVERSE_AGE_YEARS * YEAR_S / HBAR_GEV_S
        log_expected = 4 * math.log(age_gev_inverse * scale) - action
        result.update({
            "leading_Fubini_action": action,
            "log_expected_decay_events_order_of_magnitude": log_expected,
            "log10_expected_decay_events_order_of_magnitude": log_expected / math.log(10),
            "leading_diagnostic_long_lived": log_expected < 0,
        })
    else:
        result.update({
            "leading_Fubini_action": None,
            "leading_diagnostic_long_lived": True,
            "note": "No negative Higgs quartic occurs inside the declared perturbative interval.",
        })
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--points", type=int, default=8000)
    args = parser.parse_args()
    results = [
        diagnose("B0", 0.020, 0.030, args.points),
        diagnose("B1", 0.180, 0.180, args.points),
        diagnose("B2", 0.2385, 0.0, args.points),
    ]
    payload = {
        "schema_version": 1,
        "universe_age_years": UNIVERSE_AGE_YEARS,
        "benchmarks": results,
        "formula": "S4=8*pi^2/(3*abs(lambda_H)); ln(N_decay)~4*ln(T_U*mu)-S4",
        "classification": "leading semiclassical diagnostic only",
        "limitations": [
            "minimum at a cutoff is UV sensitive and does not identify a stationary bounce scale",
            "one-loop no-threshold running",
            "no fluctuation determinant or gauge-consistent effective quartic",
            "no gravitational or higher-dimensional operators",
            "no multi-field bounce search"
        ]
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
