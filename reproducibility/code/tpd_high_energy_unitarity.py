#!/usr/bin/env python3
"""Full Higgs+A+B high-energy scalar unitarity matrix for TP-D v0.1."""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np

import tpd_scalar_rge as scalar


PAIRS = list(combinations_with_replacement(range(scalar.N), 2))


def matrix(couplings: dict[str, float]) -> np.ndarray:
    out = np.zeros((len(PAIRS), len(PAIRS)))
    for row, (i, j) in enumerate(PAIRS):
        norm_i = math.sqrt(2) if i == j else 1.0
        for col, (k, ell) in enumerate(PAIRS):
            norm_f = math.sqrt(2) if k == ell else 1.0
            out[row, col] = sum(
                float(coefficient) * couplings[name]
                for name, coefficient in scalar.tensor((i, j, k, ell)).items()
            ) / (norm_i * norm_f)
    return out


def analytic_spectrum(c: dict[str, float]) -> np.ndarray:
    singlet = np.array(
        [
            [6 * c["lambda_H"], math.sqrt(2) * c["lambda_HA"], math.sqrt(2) * c["lambda_HB"]],
            [math.sqrt(2) * c["lambda_HA"], 4 * c["lambda_A"], c["lambda_AB"]],
            [math.sqrt(2) * c["lambda_HB"], c["lambda_AB"], 4 * c["lambda_B"]],
        ]
    )
    values = [
        *([2 * c["lambda_H"]] * 9),
        *([2 * c["lambda_A"]] * 2),
        *([2 * c["lambda_B"]] * 2),
        *([c["lambda_HA"]] * 8),
        *([c["lambda_HB"]] * 8),
        *([c["lambda_AB"]] * 4),
        *np.linalg.eigvalsh(singlet).tolist(),
    ]
    return np.sort(np.array(values))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--random-tests", type=int, default=250)
    args = parser.parse_args()
    scalar.build_potential()
    v, mh = 246.22, 125.25
    benchmark = {
        "lambda_H": mh**2 / (2 * v**2),
        "lambda_A": 0.20,
        "lambda_B": 0.25,
        "lambda_HA": 0.020,
        "lambda_HB": 0.030,
        "lambda_AB": 0.10,
    }
    numeric = np.linalg.eigvalsh(matrix(benchmark))
    analytic = analytic_spectrum(benchmark)
    if not np.allclose(numeric, analytic, rtol=1e-12, atol=1e-12):
        raise RuntimeError("Analytic multiplicity spectrum does not match tensor matrix")
    rng = np.random.default_rng(314159)
    max_error = 0.0
    for _ in range(args.random_tests):
        point = {name: float(value) for name, value in zip(scalar.NAMES, rng.uniform(-1, 1, size=6))}
        direct = np.linalg.eigvalsh(matrix(point))
        predicted = analytic_spectrum(point)
        max_error = max(max_error, float(np.max(np.abs(direct - predicted))))
        if not np.allclose(direct, predicted, rtol=1e-11, atol=1e-11):
            raise RuntimeError(f"Random spectrum mismatch at {point}")
    spectral_radius = float(np.max(np.abs(numeric)))
    payload = {
        "schema_version": 1,
        "basis_dimension": len(PAIRS),
        "benchmark": benchmark,
        "eigenvalues": numeric.tolist(),
        "spectral_radius": spectral_radius,
        "partial_wave_convention": "a0=-Lambda/(16*pi)",
        "unitarity_condition": "|Lambda| <= 8*pi",
        "max_abs_a0": spectral_radius / (16 * math.pi),
        "passes": spectral_radius <= 8 * math.pi,
        "analytic_structure": {
            "2lambda_H_multiplicity": 9,
            "2lambda_A_multiplicity": 2,
            "2lambda_B_multiplicity": 2,
            "lambda_HA_multiplicity": 8,
            "lambda_HB_multiplicity": 8,
            "lambda_AB_multiplicity": 4,
            "remaining": "three eigenvalues of [[6lambda_H,sqrt(2)lambda_HA,sqrt(2)lambda_HB],[sqrt(2)lambda_HA,4lambda_A,lambda_AB],[sqrt(2)lambda_HB,lambda_AB,4lambda_B]]",
        },
        "random_cross_check": {
            "points": args.random_tests,
            "seed": 314159,
            "maximum_absolute_eigenvalue_error": max_error,
        },
        "scope_warning": "High-energy scalar/Goldstone quartic limit. Finite-energy exchanges, transverse gauge states, and pole excision are not included.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
