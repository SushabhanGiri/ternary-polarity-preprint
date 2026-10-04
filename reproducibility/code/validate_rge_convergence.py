#!/usr/bin/env python3
"""Convergence check for the TP-1 one-loop benchmark evolution."""

from __future__ import annotations

import json

import full_rge_tp1


def main() -> None:
    settings = [
        {"name": "loose", "samples": 600, "rtol": 2e-8, "atol": 1e-10, "max_step": 0.10},
        {"name": "nominal", "samples": 1200, "rtol": 2e-10, "atol": 1e-12, "max_step": 0.05},
        {"name": "tight", "samples": 2400, "rtol": 2e-12, "atol": 1e-14, "max_step": 0.025},
    ]
    runs = []
    for setting in settings:
        result = full_rge_tp1.run_benchmark(
            samples=setting["samples"], rtol=setting["rtol"],
            atol=setting["atol"], max_step=setting["max_step"],
        )
        boundary = result["first_failure"]["refined_boundary"]["scale_GeV"]
        runs.append({
            **setting,
            "unitarity_boundary_GeV": boundary,
            "perturbative_4pi_stop_GeV": result["integration_end_GeV"],
            "nfev": result["solver"]["nfev"],
        })
    reference = runs[-1]["unitarity_boundary_GeV"]
    for run in runs:
        run["relative_boundary_difference_from_tight"] = abs(run["unitarity_boundary_GeV"] / reference - 1.0)
    report = {
        "runs": runs,
        "maximum_relative_boundary_difference": max(r["relative_boundary_difference_from_tight"] for r in runs),
        "passed_target_1e-7": max(r["relative_boundary_difference_from_tight"] for r in runs) < 1e-7,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
