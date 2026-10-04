#!/usr/bin/env python3
"""High-energy scalar coupled-channel unitarity matrix for TP-1.

For constant quartic amplitudes and massless kinematics, the Hektor-Hryczuk-
Kannike convention gives

 a0[(ij),(kl)] = -lambda_ijkl /
                  (16*pi*sqrt(2^delta_ij 2^delta_kl)).

Therefore every eigenvalue L of the normalized quartic tensor must satisfy
|L| <= 8*pi when |Re a0| <= 1/2.  This script derives the 36x36 real-scalar
matrix directly from the potential used by scalar_rge_generator.py.
"""

from __future__ import annotations

import json
import math
from typing import Dict, List, Tuple

import numpy as np

import scalar_rge_generator as rge


COUPLINGS = ("lamH", "lamS", "lamc", "lamHS", "lamHc", "lamSc", "kappa")
PAIRS: List[Tuple[int, int]] = [(i, j) for i in range(rge.N) for j in range(i, rge.N)]


def matrix(couplings: Dict[str, float]) -> np.ndarray:
    out = np.zeros((len(PAIRS), len(PAIRS)), dtype=float)
    for row, (i, j) in enumerate(PAIRS):
        ni = math.sqrt(2.0 if i == j else 1.0)
        for col, (k, ell) in enumerate(PAIRS):
            nf = math.sqrt(2.0 if k == ell else 1.0)
            linear = rge.tensor((i, j, k, ell))
            out[row, col] = sum(float(coefficient) * couplings.get(name, 0.0) for name, coefficient in linear.items()) / (ni * nf)
    return out


def spectrum(couplings: Dict[str, float]) -> np.ndarray:
    return np.linalg.eigvalsh(matrix(couplings))


def main() -> None:
    rge.build_potential()
    benchmark = {
        "lamH": 0.13,
        "lamS": 0.30,
        "lamc": 0.25,
        "lamHS": 0.02,
        "lamHc": 0.05,
        "lamSc": 0.08,
        "kappa": 0.05,
    }
    eig = spectrum(benchmark)
    one_at_a_time = {}
    for name in COUPLINGS:
        unit = {key: 0.0 for key in COUPLINGS}
        unit[name] = 1.0
        unit_eig = spectrum(unit)
        rho = float(np.max(np.abs(unit_eig)))
        one_at_a_time[name] = {
            "spectral_radius_for_unit_coupling": rho,
            "necessary_individual_bound_from_abs_eigenvalue_le_8pi": 8 * math.pi / rho,
        }
    result = {
        "basis_dimension": len(PAIRS),
        "partial_wave_convention": "a0=-L/(16*pi); require |Re a0|<=1/2",
        "eigenvalue_condition": "every normalized quartic eigenvalue satisfies |L|<=8*pi",
        "benchmark_couplings": benchmark,
        "benchmark_eigenvalues": [float(v) for v in eig],
        "benchmark_spectral_radius": float(np.max(np.abs(eig))),
        "benchmark_max_abs_a0": float(np.max(np.abs(eig))) / (16 * math.pi),
        "benchmark_passes": bool(np.max(np.abs(eig)) <= 8 * math.pi),
        "single_coupling_diagnostics": one_at_a_time,
        "scope_warning": "Quartic high-energy scalar limit only; finite-energy exchange diagrams, gauge/Goldstone channels, and resonance excisions are not included.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
