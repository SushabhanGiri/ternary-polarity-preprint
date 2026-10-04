#!/usr/bin/env python3
"""Exact U(1) gauge check for the TP-1 scalar quartic beta functions.

This implements the one-loop gauge terms in Eqs. (38), (42), and (43) of
Luo, Wang, and Xiao, Phys. Rev. D 67, 065019 (2003), in the real-scalar
tensor convention used by scalar_rge_generator.py.  It is deliberately
independent of the numerical RGE implementation.

For one Abelian factor the generator on each complex scalar is a 2x2
antisymmetric real block.  The overall sign convention drops out of the
Casimir and pure-gauge anticommutator invariants.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from typing import Dict, Tuple

import scalar_rge_generator as scalar


QS = Fraction(3)
QCHI = Fraction(1)


def charge(index: int) -> Fraction:
    if index in scalar.S:
        return QS
    if index in scalar.X:
        return QCHI
    return Fraction(0)


def same_complex_block(a: int, b: int) -> bool:
    return (a in scalar.S and b in scalar.S) or (a in scalar.X and b in scalar.X)


def anticommutator(a: int, b: int) -> Fraction:
    """Return {theta,theta}_ab for a single U(1) generator."""
    if a == b and same_complex_block(a, b):
        return -2 * charge(a) ** 2
    return Fraction(0)


def pure_gauge_A(indices: Tuple[int, int, int, int]) -> Fraction:
    total = Fraction(0)
    # Count all 24 permutations, including duplicates when indices coincide,
    # exactly as in the symmetrized general-tensor formula.
    for p in permutations(indices):
        total += anticommutator(p[0], p[1]) * anticommutator(p[2], p[3])
    return total / 8


def gauge_wave_tensor(indices: Tuple[int, int, int, int]) -> Dict[str, Fraction]:
    lam = scalar.tensor(indices)
    casimir_sum = sum((charge(i) ** 2 for i in indices), Fraction(0))
    return {name: -3 * casimir_sum * coefficient for name, coefficient in lam.items()}


def projected_gauge_terms(indices: Tuple[int, int, int, int], divisor: int) -> Tuple[Dict[str, Fraction], Fraction]:
    wave = {name: coefficient / divisor for name, coefficient in gauge_wave_tensor(indices).items()}
    pure = 3 * pure_gauge_A(indices) / divisor
    return wave, pure


def main() -> None:
    scalar.build_potential()
    projections = {
        "lamS": ((4, 4, 4, 4), 6),
        "lamc": ((6, 6, 6, 6), 6),
        "lamSc": ((4, 4, 6, 6), 1),
        "kappa": ((4, 6, 6, 6), 3),
    }
    results = {}
    for name, (indices, divisor) in projections.items():
        wave, pure = projected_gauge_terms(indices, divisor)
        results[name] = (wave, pure)

    expected = {
        "lamS": ({"lamS": Fraction(-108)}, Fraction(486)),
        "lamc": ({"lamc": Fraction(-12)}, Fraction(6)),
        "lamSc": ({"lamSc": Fraction(-60)}, Fraction(108)),
        "kappa": ({"kappa": Fraction(-36)}, Fraction(0)),
    }
    if results != expected:
        raise RuntimeError(f"U(1) gauge tensor check failed: {results} != {expected}")

    print("Exact U(1)_X gauge contributions; RHS equals (16*pi^2)*beta:")
    print("beta_lamS  += -108*gX^2*lamS + 486*gX^4")
    print("beta_lamc  +=  -12*gX^2*lamc +   6*gX^4")
    print("beta_lamSc +=  -60*gX^2*lamSc + 108*gX^4")
    print("beta_kappa +=  -36*gX^2*kappa")
    print("Checks: Luo-Wang-Xiao quartic gauge tensor projections passed exactly.")


if __name__ == "__main__":
    main()
