#!/usr/bin/env python3
"""Independent analytic/numerical checks for the minimal TP-D scalar model."""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np


def unitarity_matrix(lambda_a: float, lambda_b: float, lambda_ab: float):
    """Return the normalized real-scalar quartic scattering matrix.

    A=(a1+i a2)/sqrt(2), B=(b1+i b2)/sqrt(2).  The fourth derivative
    tensor is reconstructed analytically from Kronecker deltas.
    """
    fields = tuple(range(4))
    pairs = list(combinations_with_replacement(range(4), 2))
    matrix = np.zeros((len(pairs), len(pairs)), dtype=float)

    def delta(i: int, j: int) -> int:
        return int(i == j)

    def quartic_tensor(i: int, j: int, k: int, ell: int) -> float:
        indices = (i, j, k, ell)
        if all(x < 2 for x in indices):
            return 2 * lambda_a * (
                delta(i, j) * delta(k, ell)
                + delta(i, k) * delta(j, ell)
                + delta(i, ell) * delta(j, k)
            )
        if all(x >= 2 for x in indices):
            return 2 * lambda_b * (
                delta(i, j) * delta(k, ell)
                + delta(i, k) * delta(j, ell)
                + delta(i, ell) * delta(j, k)
            )
        # Cross term lambda_AB (a_i a_i)(b_j b_j)/4.
        a_positions = [x for x in indices if x < 2]
        b_positions = [x - 2 for x in indices if x >= 2]
        if len(a_positions) == 2 and len(b_positions) == 2:
            return lambda_ab * delta(a_positions[0], a_positions[1]) * delta(
                b_positions[0], b_positions[1]
            )
        return 0.0

    for row, (i, j) in enumerate(pairs):
        ni = math.sqrt(2) if i == j else 1.0
        for col, (k, ell) in enumerate(pairs):
            nf = math.sqrt(2) if k == ell else 1.0
            matrix[row, col] = quartic_tensor(i, j, k, ell) / (ni * nf)
    return fields, pairs, matrix


def symbolic_unitarity_spectrum() -> list[dict[str, str | int]]:
    return [
        {"eigenvalue": "2 lambda_A", "multiplicity": 2},
        {"eigenvalue": "2 lambda_B", "multiplicity": 2},
        {"eigenvalue": "lambda_AB", "multiplicity": 4},
        {
            "eigenvalue": "2(lambda_A+lambda_B) - sqrt(4(lambda_A-lambda_B)^2+lambda_AB^2)",
            "multiplicity": 1,
        },
        {
            "eigenvalue": "2(lambda_A+lambda_B) + sqrt(4(lambda_A-lambda_B)^2+lambda_AB^2)",
            "multiplicity": 1,
        },
    ]


def mass_mixing(m_a2: float, m_b2: float, delta_re: float, delta_im: float):
    delta = complex(delta_re, delta_im)
    matrix = np.array([[m_a2, delta], [delta.conjugate(), m_b2]], dtype=complex)
    numerical = np.linalg.eigvalsh(matrix)
    discriminant = math.sqrt((m_b2 - m_a2) ** 2 + 4 * abs(delta) ** 2)
    analytic = np.array([(m_a2 + m_b2 - discriminant) / 2, (m_a2 + m_b2 + discriminant) / 2])
    theta = 0.5 * math.atan2(2 * abs(delta), m_b2 - m_a2)
    return {
        "numeric_eigenvalues": numerical.real.tolist(),
        "analytic_eigenvalues": analytic.tolist(),
        "max_abs_difference": float(np.max(np.abs(numerical.real - analytic))),
        "mixing_angle_rad": theta,
        "tan_2theta": 2 * abs(delta) / (m_b2 - m_a2) if m_b2 != m_a2 else math.inf,
    }


def two_body_width(m_parent: float, m_child: float, m_h: float, coupling: float) -> float:
    x = (m_child / m_parent) ** 2
    y = (m_h / m_parent) ** 2
    kallen = 1 + x * x + y * y - 2 * x - 2 * y - 2 * x * y
    if kallen <= 0:
        return 0.0
    return coupling * coupling * math.sqrt(kallen) / (16 * math.pi * m_parent)


def sufficient_inert_vacuum_check(params: dict[str, float], samples: int, seed: int):
    ma2, mb2 = params["m_A"] ** 2, params["m_B"] ** 2
    ua, ub = abs(params["mu_A"]), abs(params["mu_B"])
    la, lb, lab = params["lambda_A"], params["lambda_B"], params["lambda_AB"]
    analytic = {
        "bfb": la > 0 and lb > 0 and lab > -2 * math.sqrt(la * lb),
        "nonnegative_single_A": ua * ua <= 9 * la * ma2,
        "nonnegative_single_B": ub * ub <= 9 * lb * mb2,
        "nonnegative_portal": lab >= 0,
    }
    rng = np.random.default_rng(seed)
    # Log-uniform radial exploration plus exact origin. Phases have already been minimized.
    radii = 10 ** rng.uniform(-5, 4, size=(samples, 2))
    radii *= np.array([params["m_A"], params["m_B"]])
    ra, rb = radii[:, 0], radii[:, 1]
    values = (
        ma2 * ra**2
        + mb2 * rb**2
        - 2 * ua * ra**3 / 3
        - 2 * ub * rb**3 / 3
        + la * ra**4
        + lb * rb**4
        + lab * ra**2 * rb**2
    )
    return {
        "analytic_sufficient_conditions": analytic,
        "all_sufficient_conditions_pass": all(analytic.values()),
        "random_seed": seed,
        "samples": samples,
        "minimum_sampled_potential_GeV4": float(np.min(values)),
        "negative_sample_count": int(np.count_nonzero(values < -1e-8)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--samples", type=int, default=200_000)
    args = parser.parse_args()

    benchmark = {
        "m_A": 180.0,
        "m_B": 400.0,
        "mu_A": 60.0,
        "mu_B": 90.0,
        "lambda_A": 0.20,
        "lambda_B": 0.25,
        "lambda_AB": 0.10,
        "lambda_HA": 0.020,
        "lambda_HB": 0.030,
    }
    _, _, numerical_matrix = unitarity_matrix(
        benchmark["lambda_A"], benchmark["lambda_B"], benchmark["lambda_AB"]
    )
    eig = np.linalg.eigvalsh(numerical_matrix)
    # Comparator example only: lambda_HAB is forbidden in exact TP-D.
    comparator_lambda_hab = 0.01
    higgs_vev = 246.22
    g_hab = comparator_lambda_hab * higgs_vev
    payload = {
        "schema_version": 1,
        "benchmark": benchmark,
        "vacuum": sufficient_inert_vacuum_check(benchmark, args.samples, 20260915),
        "unitarity": {
            "symbolic_eigenvalues": symbolic_unitarity_spectrum(),
            "numeric_eigenvalues": eig.tolist(),
            "spectral_radius": float(np.max(np.abs(eig))),
            "condition": "|eigenvalue| <= 8*pi",
            "passes": bool(np.max(np.abs(eig)) <= 8 * math.pi),
        },
        "mass_mixing_cross_check": mass_mixing(180.0**2, 400.0**2, 1500.0, -700.0),
        "kernel_sensitive_decay_example": {
            "process": "B -> A + h",
            "m_B_GeV": benchmark["m_B"],
            "m_A_GeV": benchmark["m_A"],
            "m_h_GeV": 125.25,
            "generic_Z3_lambda_HAB": comparator_lambda_hab,
            "generic_Z3_width_GeV": two_body_width(
                benchmark["m_B"], benchmark["m_A"], 125.25, g_hab
            ),
            "exact_TP_D_width_GeV": 0.0,
            "warning": "The generic-Z3 coupling is free and can be tuned to zero; only a nonzero observed width is a one-sided falsification of exact TP-D under the benchmark assumptions.",
        },
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
