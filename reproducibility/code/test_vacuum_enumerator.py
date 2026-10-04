#!/usr/bin/env python3
"""Randomized numerical cross-check of the analytic TP-1 branch enumerator."""

from __future__ import annotations

import json
import math

import numpy as np

from vacuum_audit import (
    Parameters,
    bfb_numerical_check,
    direct_minimum_check,
    enumerate_stationary_points,
)


def main() -> None:
    rng = np.random.default_rng(20260915)
    accepted = 0
    failures = []
    winning_branches = {}
    attempts = 0
    while accepted < 40 and attempts < 1000:
        attempts += 1
        p = Parameters(
            muH2=float(rng.uniform(-1.5, 1.5)),
            muS2=float(rng.uniform(-1.5, 1.5)),
            muc2=float(rng.uniform(-1.5, 1.5)),
            lamH=float(rng.uniform(0.12, 1.0)),
            lamS=float(rng.uniform(0.12, 1.0)),
            lamc=float(rng.uniform(0.12, 1.0)),
            lamHS=float(rng.uniform(-0.3, 0.6)),
            lamHc=float(rng.uniform(-0.3, 0.6)),
            lamSc=float(rng.uniform(-0.3, 0.6)),
            kappa=float(rng.uniform(0.01, 0.25)),
        )
        bfb = bfb_numerical_check(p)
        if not bfb["passes_exact_radial_test_numerically"]:
            continue
        accepted += 1
        candidates = enumerate_stationary_points(p)
        winning_branches[candidates[0]["branch"]] = winning_branches.get(candidates[0]["branch"], 0) + 1
        enum_v = float(candidates[0]["V"])
        direct = direct_minimum_check(p, upper=10.0)
        direct_v = float(direct["V"])
        error = abs(enum_v - direct_v)
        tolerance = 2e-6 * max(1.0, abs(enum_v), abs(direct_v))
        if error > tolerance:
            failures.append(
                {
                    "case": accepted,
                    "parameters": p.__dict__,
                    "enumerated_V": enum_v,
                    "direct_V": direct_v,
                    "error": error,
                    "enumerated_branch": candidates[0]["branch"],
                    "direct_point": direct["point"],
                }
            )

    result = {
        "seed": 20260915,
        "attempts": attempts,
        "bounded_cases_checked": accepted,
        "failure_count": len(failures),
        "failures": failures,
        "winning_branches": winning_branches,
        "criterion": "absolute energy mismatch > 2e-6 times the larger of 1 and the two energy magnitudes",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
