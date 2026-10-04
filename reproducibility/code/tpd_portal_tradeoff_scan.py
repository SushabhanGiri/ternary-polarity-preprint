#!/usr/bin/env python3
"""Reproducible one-loop scan of the TP-D portal-stability trade-off.

This is a deliberately small diagnostic grid at fixed dark masses, self
couplings, and cubic couplings.  It tests whether portal choices can delay the
Higgs-quartic BFB failure without losing the simple inert-vacuum certificate or
perturbative unitarity.  It is not a statistical parameter scan.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import tpd_full_rge_running as running


EQUAL_PORTALS = tuple(round(0.02 * i, 2) for i in range(1, 12))
LIGHT_ONLY_PORTALS = (0.225, 0.230, 0.235, 0.238, 0.2385, 0.240, 0.245)


def evaluate(lambda_ha: float, lambda_hb: float, points: int) -> dict[str, object]:
    result = running.run(lambda_ha, lambda_hb, points, 2.435e18)
    return {
        "lambda_HA": lambda_ha,
        "lambda_HB": lambda_hb,
        "first_BFB_failure_GeV": result["first_BFB_failure_GeV"],
        "first_sufficient_global_EW_failure_GeV": result["first_sufficient_global_EW_failure_GeV"],
        "first_sufficient_global_EW_failure_conditions": result["first_sufficient_global_EW_failure_conditions"],
        "minimum_BFB_margin": result["minimum_margins"]["BFB_margin"],
        "unitarity_boundary_GeV": result["unitarity_boundary_GeV"],
        "four_pi_boundary_GeV": result["four_pi_boundary_GeV"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--points", type=int, default=1600)
    args = parser.parse_args()
    equal = [evaluate(portal, portal, args.points) for portal in EQUAL_PORTALS]
    light_only = [evaluate(portal, 0.0, args.points) for portal in LIGHT_ONLY_PORTALS]
    all_rows = equal + light_only
    best = max(
        all_rows,
        key=lambda row: float(row["first_sufficient_global_EW_failure_GeV"] or row["unitarity_boundary_GeV"]),
    )
    payload = {
        "schema_version": 1,
        "fixed_inputs": {
            "M_A_GeV": 180.0,
            "M_B_GeV": 400.0,
            "lambda_A": 0.20,
            "lambda_B": 0.25,
            "lambda_AB": 0.10,
            "mu_A_GeV": 60.0,
            "mu_B_GeV": 90.0,
        },
        "equal_portal_scan": equal,
        "light_species_only_initial_portal_scan": light_only,
        "largest_simple_certificate_reach_on_grid": best,
        "interpretation": "Asymmetric portals perform better because beta_lambda_H depends on squares while beta_muH2 is weighted linearly by dark mass-squared. Near-critical points have small BFB margins and are not robust predictions.",
        "scope": "Sparse deterministic grid, one-loop MS-bar, no thresholds or two-loop uncertainty; not a proof of global optimality.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
