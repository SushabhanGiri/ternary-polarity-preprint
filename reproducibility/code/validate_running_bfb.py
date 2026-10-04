#!/usr/bin/env python3
"""Randomized cross-check of the algebraic running-coupling BFB test."""

from __future__ import annotations

import json
import random

import full_rge_tp1
import vacuum_audit


def main() -> None:
    rng = random.Random(20260915)
    records = []
    for _ in range(30):
        couplings = {
            "lamH": rng.uniform(0.06, 1.0),
            "lamS": rng.uniform(0.06, 1.0),
            "lamc": rng.uniform(0.06, 1.0),
            "lamHS": rng.uniform(-0.8, 0.8),
            "lamHc": rng.uniform(-0.8, 0.8),
            "lamSc": rng.uniform(-0.8, 0.8),
            "kappa": rng.uniform(0.001, 0.35),
        }
        exact_ok, exact_margin, exact_t = full_rge_tp1.exact_bfb_margin(couplings)
        p = vacuum_audit.Parameters(
            1.0, 1.0, 1.0,
            couplings["lamH"], couplings["lamS"], couplings["lamc"],
            couplings["lamHS"], couplings["lamHc"], couplings["lamSc"], couplings["kappa"],
        )
        numerical = vacuum_audit.bfb_numerical_check(p)
        numerical_ok = bool(numerical["passes_exact_radial_test_numerically"])
        if exact_ok != numerical_ok:
            raise RuntimeError({"couplings": couplings, "exact": (exact_ok, exact_margin, exact_t), "numerical": numerical})
        records.append({
            "exact_ok": exact_ok,
            "exact_margin": exact_margin,
            "exact_t": exact_t,
            "numerical_margin": numerical["reduced_min_value"],
            "numerical_t": numerical["reduced_min_t"],
        })
    report = {
        "seed": 20260915,
        "cases": len(records),
        "classification_agreement": len(records),
        "maximum_absolute_margin_difference": max(abs(r["exact_margin"] - r["numerical_margin"]) for r in records),
        "records": records,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
