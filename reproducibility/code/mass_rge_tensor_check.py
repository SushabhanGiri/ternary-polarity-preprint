#!/usr/bin/env python3
"""Exact scalar-loop check of the TP-1 quadratic-mass beta functions."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import DefaultDict, Dict, Tuple

import scalar_rge_generator as scalar


MassTerm = Tuple[str, str]


def mass_name(index: int) -> str:
    if index in scalar.H:
        return "mH2"
    if index in scalar.S:
        return "mS2"
    if index in scalar.X:
        return "mc2"
    raise IndexError(index)


def scalar_mass_beta(a: int) -> Dict[MassTerm, Fraction]:
    # Luo-Wang-Xiao Eq. (86), with no cubic dimensionful couplings:
    # beta_m2[aa] = sum_e m2[ee] lambda[aaee].
    out: DefaultDict[MassTerm, Fraction] = defaultdict(Fraction)
    for e in range(scalar.N):
        for coupling, coefficient in scalar.tensor((a, a, e, e)).items():
            out[(coupling, mass_name(e))] += coefficient
    return dict(out)


def main() -> None:
    scalar.build_potential()
    got = {
        "mH2": scalar_mass_beta(0),
        "mS2": scalar_mass_beta(4),
        "mc2": scalar_mass_beta(6),
    }
    expected = {
        "mH2": {("lamH", "mH2"): Fraction(12), ("lamHS", "mS2"): Fraction(2), ("lamHc", "mc2"): Fraction(2)},
        "mS2": {("lamHS", "mH2"): Fraction(4), ("lamS", "mS2"): Fraction(8), ("lamSc", "mc2"): Fraction(2)},
        "mc2": {("lamHc", "mH2"): Fraction(4), ("lamSc", "mS2"): Fraction(2), ("lamc", "mc2"): Fraction(8)},
    }
    if got != expected:
        raise RuntimeError(f"Scalar mass-tensor check failed: {got} != {expected}")
    print("Scalar-loop quadratic-mass beta functions; RHS equals (16*pi^2)*beta:")
    print("beta_mH2 += 12*lamH*mH2 + 2*lamHS*mS2 + 2*lamHc*mc2")
    print("beta_mS2 +=  4*lamHS*mH2 + 8*lamS*mS2 + 2*lamSc*mc2")
    print("beta_mc2 +=  4*lamHc*mH2 + 2*lamSc*mS2 + 8*lamc*mc2")
    print("Check: exact real-scalar tensor contraction passed.")


if __name__ == "__main__":
    main()
