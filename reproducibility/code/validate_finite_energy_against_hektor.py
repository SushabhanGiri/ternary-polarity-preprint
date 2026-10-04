#!/usr/bin/env python3
"""Validate the numerical partial-wave engine against Hektor et al. Eqs. 3.6-3.7."""

from __future__ import annotations

import json
import math

import numpy as np
from numpy.polynomial.legendre import leggauss


def numerical_eigenvalues(mass: float, lam: float, mu3: float, s: float) -> np.ndarray:
    quartic = np.zeros((2, 2, 2, 2))
    cubic = np.zeros((2, 2, 2))
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    quartic[a, b, c, d] = 2 * lam * (
                        (a == b) * (c == d)
                        + (a == c) * (b == d)
                        + (a == d) * (b == c)
                    )
    cubic[0, 0, 0] = 3 * mu3 / math.sqrt(2)
    for indices in ((0, 1, 1), (1, 0, 1), (1, 1, 0)):
        cubic[indices] = -3 * mu3 / math.sqrt(2)

    pairs = ((0, 0), (0, 1), (1, 1))
    nodes, weights = leggauss(256)
    momentum = math.sqrt(s - 4 * mass * mass) / 2
    matrix = np.zeros((3, 3))
    for i, (a, b) in enumerate(pairs):
        for j, (c, d) in enumerate(pairs):
            integral = 0.0
            for costh, weight in zip(nodes, weights):
                t = -2 * momentum * momentum * (1 - costh)
                u = -2 * momentum * momentum * (1 + costh)
                value = -quartic[a, b, c, d]
                for e in range(2):
                    value -= cubic[a, b, e] * cubic[c, d, e] / (s - mass * mass)
                    value -= cubic[a, c, e] * cubic[b, d, e] / (t - mass * mass)
                    value -= cubic[a, d, e] * cubic[b, c, e] / (u - mass * mass)
                integral += weight * value
            norm = 2 ** (a == b) * 2 ** (c == d)
            prefactor = math.sqrt(4 * momentum * momentum / (norm * s)) / (32 * math.pi)
            matrix[j, i] = prefactor * integral
    return np.linalg.eigvalsh(0.5 * (matrix + matrix.T))


def analytic_eigenvalues(mass: float, lam: float, mu3: float, s: float) -> np.ndarray:
    a1 = -math.sqrt(s * (s - 4 * mass * mass)) * (
        4 * lam * (s - mass * mass) + 9 * mu3 * mu3
    ) / (32 * math.pi * s * (s - mass * mass))
    a2 = (
        4 * lam * (4 * mass * mass - s)
        + 9 * mu3 * mu3 * math.log((s - 3 * mass * mass) / (mass * mass))
    ) / (16 * math.pi * math.sqrt(s * (s - 4 * mass * mass)))
    return np.sort(np.array((a1, a1, a2)))


def main() -> None:
    mass, lam, mu3 = 500.0, 0.25, 80.0
    records = []
    max_relative_error = 0.0
    for ratio in (4.05, 5.0, 7.5, 12.0, 50.0):
        s = ratio * mass * mass
        numeric = numerical_eigenvalues(mass, lam, mu3, s)
        analytic = analytic_eigenvalues(mass, lam, mu3, s)
        relative = float(np.max(np.abs(numeric - analytic) / np.maximum(1e-14, np.abs(analytic))))
        max_relative_error = max(max_relative_error, relative)
        records.append(
            {
                "s_over_M2": ratio,
                "numeric": [float(v) for v in numeric],
                "analytic": [float(v) for v in analytic],
                "max_relative_error": relative,
            }
        )
    result = {
        "reference": "Hektor, Hryczuk and Kannike, JHEP 03 (2019) 204, Eqs. 3.6-3.7",
        "parameters": {"M_GeV": mass, "lambda": lam, "mu3_GeV": mu3},
        "records": records,
        "maximum_relative_error": max_relative_error,
        "passes_1e-10": bool(max_relative_error < 1e-10),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["passes_1e-10"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
