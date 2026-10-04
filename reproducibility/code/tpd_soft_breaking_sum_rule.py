#!/usr/bin/env python3
"""Tree-level kernel-sensitive sum rule for minimally soft-broken TP.

Exact TP-D forbids both A^dag B and (H^dag H)A^dag B.  A dimension-two
bilinear delta^2 A^dag B softly breaks Z3_m x Z3_E to the projected diagonal
Z3 while retaining zero hard off-diagonal Higgs portal eta_HAB.

After diagonalizing the two-state mass matrix, the Higgs-coupling matrix G
obeys

  2 G12 cos(2 theta) - (G22-G11) sin(2 theta) = 0.

A generic single-Z3 theory permits eta_HAB independently and instead gives
the right-hand side 2 v eta_HAB.  This file verifies the identity numerically
and evaluates the stored spectrum as a function of the soft mixing angle.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from tpd_phenomenology_prefilter import generic_offdiagonal_width_coefficient


def rotation(theta: float) -> np.ndarray:
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s], [s, c]])


def higgs_matrix(theta: float, lambda_a: float, lambda_b: float,
                 eta: float, vev: float) -> np.ndarray:
    portal = np.array([[lambda_a, eta], [eta, lambda_b]], dtype=float)
    r = rotation(theta)
    return vev * r.T @ portal @ r


def residual(theta: float, matrix: np.ndarray) -> float:
    return (
        2 * matrix[0, 1] * math.cos(2 * theta)
        - (matrix[1, 1] - matrix[0, 0]) * math.sin(2 * theta)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rng = np.random.default_rng(20260919)
    maximum_error = 0.0
    for _ in range(1000):
        theta = float(rng.uniform(-0.75, 0.75))
        la, lb, eta = map(float, rng.uniform(-1, 1, size=3))
        v = float(rng.uniform(1, 1000))
        g = higgs_matrix(theta, la, lb, eta, v)
        maximum_error = max(maximum_error, abs(residual(theta, g) - 2 * v * eta))
    if maximum_error > 2e-10:
        raise RuntimeError(f"Sum-rule verification failed: {maximum_error}")

    v, mh = 246.22, 125.25
    m1, m2 = 180.0, 400.0
    la, lb = 0.020, 0.030
    width_prefactor = generic_offdiagonal_width_coefficient(m2, m1, mh, v)
    hbar_gev_s = 6.582119569e-25
    examples = {}
    for theta in (1e-2, 1e-3, 1e-5, 1e-7):
        g = higgs_matrix(theta, la, lb, 0.0, v)
        eta_effective = g[0, 1] / v
        width = width_prefactor * eta_effective**2
        delta2 = 0.5 * (m2**2 - m1**2) * math.sin(2 * theta)
        examples[str(theta)] = {
            "soft_delta2_GeV2": delta2,
            "G12_GeV": float(g[0, 1]),
            "eta_effective_G12_over_v": float(eta_effective),
            "B_to_A_h_width_GeV": width,
            "ctau_m": 299792458.0 * hbar_gev_s / width if width else math.inf,
            "sum_rule_residual_GeV": residual(theta, g),
        }

    payload = {
        "schema_version": 1,
        "model": "TP-Bsoft: dimension-two A^dag B breaking only; eta_HAB=0",
        "mass_matrix": "[[M_A^2, delta^2], [delta^2, M_B^2]]",
        "mixing_relation": "tan(2 theta)=2 delta^2/(M_B^2-M_A^2)",
        "higgs_matrix": "G_h=v R(theta)^T [[lambda_HA,eta_HAB],[eta_HAB,lambda_HB]] R(theta)",
        "generic_Z3_identity": "2 G12 cos(2 theta)-(G22-G11) sin(2 theta)=2 v eta_HAB",
        "minimal_soft_TP_sum_rule": "2 G12 cos(2 theta)=(G22-G11) sin(2 theta)",
        "independent_random_checks": 1000,
        "maximum_absolute_identity_error_GeV": maximum_error,
        "benchmark_examples": examples,
        "radiative_status": "In a mass-independent scheme, a dimension-two soft breaking does not create an inhomogeneous beta function for the forbidden dimension-four eta_HAB operator. Physical amplitudes still receive calculable loop corrections.",
        "observability_condition": "theta is physical only if another interaction identifies the A/B charge basis. TP-G gauge-current couplings can do this in principle; the Higgs portal alone cannot.",
        "novelty_warning": "The matrix identity is standard two-state mixing/alignment algebra. Its use as a TP benchmark is potentially distinctive, but literature novelty is not demonstrated.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
