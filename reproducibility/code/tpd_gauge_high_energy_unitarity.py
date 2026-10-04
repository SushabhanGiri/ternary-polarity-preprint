#!/usr/bin/env python3
"""High-energy scalar/Goldstone quartic matrix for TP-G0.

Twelve real fields are used: four Higgs components, A1/A2, B1/B2,
Phi_m1/Phi_m2, and Phi_E1/Phi_E2.  The 78-channel matrix includes the
phase-sensitive kappa_m Phi_m^dag A^3 and kappa_E Phi_E^dag B^3 operators.
Gauge-exchange contributions are not included.
"""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations_with_replacement
from math import factorial
from pathlib import Path

import numpy as np

import tpd_high_energy_unitarity as low_unitarity
import tpd_scalar_rge as low_scalar


N = 12
H, A, B, PM, PE = range(4), range(4, 6), range(6, 8), range(8, 10), range(10, 12)
PAIRS = list(combinations_with_replacement(range(N), 2))


def add(poly: dict[tuple[int, ...], float], coefficient: float, indices) -> None:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    key = tuple(powers)
    poly[key] = poly.get(key, 0.0) + coefficient


def potential(c: dict[str, float]) -> dict[tuple[int, ...], float]:
    poly: dict[tuple[int, ...], float] = {}
    for sector, name in (
        (H, "lambda_H"), (A, "lambda_A"), (B, "lambda_B"),
        (PM, "lambda_Phi_m"), (PE, "lambda_Phi_E"),
    ):
        for i in sector:
            for j in sector:
                add(poly, c[name] / 4, (i, i, j, j))
    for first, second, name in (
        (H, A, "lambda_HA"), (H, B, "lambda_HB"),
        (H, PM, "lambda_HPhi_m"), (H, PE, "lambda_HPhi_E"),
        (A, B, "lambda_AB"), (A, PM, "lambda_APhi_m"),
        (A, PE, "lambda_APhi_E"), (B, PM, "lambda_BPhi_m"),
        (B, PE, "lambda_BPhi_E"), (PM, PE, "lambda_Phi_mPhi_E"),
    ):
        for i in first:
            for j in second:
                add(poly, c.get(name, 0.0) / 4, (i, i, j, j))

    # kappa/2 [p(a^3-3ab^2)+q(3a^2b-b^3)] and B-sector analogue.
    for real, imag, p, q, name in ((4, 5, 8, 9, "kappa_m"), (6, 7, 10, 11, "kappa_E")):
        kappa = c[name]
        add(poly, kappa / 2, (p, real, real, real))
        add(poly, -3 * kappa / 2, (p, real, imag, imag))
        add(poly, 3 * kappa / 2, (q, real, real, imag))
        add(poly, -kappa / 2, (q, imag, imag, imag))
    return poly


def tensor(poly: dict[tuple[int, ...], float], indices: tuple[int, int, int, int]) -> float:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    factor = math.prod(factorial(power) for power in powers)
    return factor * poly.get(tuple(powers), 0.0)


def matrix(c: dict[str, float]) -> np.ndarray:
    poly = potential(c)
    out = np.zeros((len(PAIRS), len(PAIRS)))
    for row, (i, j) in enumerate(PAIRS):
        norm_in = math.sqrt(2) if i == j else 1.0
        for col, (k, ell) in enumerate(PAIRS):
            norm_out = math.sqrt(2) if k == ell else 1.0
            out[row, col] = tensor(poly, (i, j, k, ell)) / (norm_in * norm_out)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    v, mh, f = 246.22, 125.25, 1000.0
    benchmark = {
        "lambda_H": mh**2 / (2 * v**2),
        "lambda_A": 0.20, "lambda_B": 0.25,
        "lambda_HA": 0.020, "lambda_HB": 0.030, "lambda_AB": 0.10,
        "lambda_Phi_m": 0.20, "lambda_Phi_E": 0.20,
        "kappa_m": math.sqrt(2) * 60.0 / (3 * f),
        "kappa_E": math.sqrt(2) * 90.0 / (3 * f),
    }
    scattering = matrix(benchmark)
    eigenvalues = np.linalg.eigvalsh(scattering)
    radius = float(np.max(np.abs(eigenvalues)))

    # The low-energy H+A+B principal submatrix must reproduce the independent
    # 36-channel generator exactly.
    low_scalar.build_potential()
    low_couplings = {name: benchmark[name] for name in low_scalar.NAMES}
    low_direct = low_unitarity.matrix(low_couplings)
    low_positions = [position for position, pair in enumerate(PAIRS) if pair[1] < 8]
    principal = scattering[np.ix_(low_positions, low_positions)]
    principal_error = float(np.max(np.abs(principal - low_direct)))
    if not np.allclose(principal, low_direct, rtol=1e-13, atol=1e-13):
        raise RuntimeError("TP-G0 low-energy principal submatrix mismatch")

    payload = {
        "schema_version": 1,
        "benchmark": "TP-G0",
        "real_scalar_components": N,
        "two_particle_channels": len(PAIRS),
        "couplings": benchmark,
        "spectral_radius": radius,
        "max_abs_a0": radius / (16 * math.pi),
        "unitarity_condition": "abs(Lambda)<=8*pi, with a0=-Lambda/(16*pi)",
        "passes": radius <= 8 * math.pi,
        "eigenvalues": eigenvalues.tolist(),
        "low_energy_principal_submatrix_max_abs_error": principal_error,
        "scope_warning": "Complete scalar-potential quartic matrix including would-be Goldstones. Gauge-exchange diagrams, transverse vectors, finite-energy exchanges, and kinetic mixing are not included."
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
