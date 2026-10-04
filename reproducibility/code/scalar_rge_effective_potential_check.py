#!/usr/bin/env python3
"""Independent scalar RGE derivation from the one-loop potential divergence.

For canonically normalized real scalars,

    (16*pi^2) beta_V = 1/2 Tr[(V''_4)^2].

This exact-arithmetic Hessian algorithm is different from the four-index
contraction used in scalar_rge_generator.py. Agreement checks the loop
combinatorics, including the S^dagger chi^3 operator normalization.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import DefaultDict, Dict, Tuple

import scalar_rge_generator as scalar


Powers = Tuple[int, ...]
Linear = Dict[str, Fraction]
Quadratic = Dict[Tuple[str, str], Fraction]
LinearFieldPoly = Dict[Powers, Linear]
QuadraticFieldPoly = Dict[Powers, Quadratic]


def add_linear(target: DefaultDict[str, Fraction], source: Linear, factor: Fraction) -> None:
    for name, coefficient in source.items():
        target[name] += factor * coefficient


def hessian_entry(a: int, b: int) -> LinearFieldPoly:
    out: Dict[Powers, DefaultDict[str, Fraction]] = {}
    for powers, coefficient in scalar.potential.items():
        if powers[a] == 0 or powers[b] - (1 if a == b else 0) == 0:
            continue
        factor = Fraction(powers[a] * (powers[b] - (1 if a == b else 0)))
        reduced = list(powers)
        reduced[a] -= 1
        reduced[b] -= 1
        key = tuple(reduced)
        if key not in out:
            out[key] = defaultdict(Fraction)
        add_linear(out[key], coefficient, factor)
    return {powers: dict(poly) for powers, poly in out.items()}


def multiply(a: LinearFieldPoly, b: LinearFieldPoly) -> QuadraticFieldPoly:
    out: Dict[Powers, DefaultDict[Tuple[str, str], Fraction]] = {}
    for pa, ca in a.items():
        for pb, cb in b.items():
            powers = tuple(x + y for x, y in zip(pa, pb))
            if powers not in out:
                out[powers] = defaultdict(Fraction)
            for name_a, coeff_a in ca.items():
                for name_b, coeff_b in cb.items():
                    key = tuple(sorted((name_a, name_b)))
                    out[powers][key] += coeff_a * coeff_b
    return {powers: dict(poly) for powers, poly in out.items()}


def beta_potential() -> QuadraticFieldPoly:
    hessian = [[hessian_entry(a, b) for b in range(scalar.N)] for a in range(scalar.N)]
    out: Dict[Powers, DefaultDict[Tuple[str, str], Fraction]] = {}
    for a in range(scalar.N):
        for b in range(scalar.N):
            product = multiply(hessian[a][b], hessian[b][a])
            for powers, poly in product.items():
                if powers not in out:
                    out[powers] = defaultdict(Fraction)
                for names, coefficient in poly.items():
                    out[powers][names] += coefficient / 2
    return {powers: dict(poly) for powers, poly in out.items()}


def scale(poly: Quadratic, factor: int) -> Quadratic:
    return {names: factor * coefficient for names, coefficient in poly.items() if coefficient}


def fmt(poly: Quadratic) -> str:
    terms = []
    for names, coefficient in sorted(poly.items()):
        monomial = names[0] + "^2" if names[0] == names[1] else "*".join(names)
        terms.append(f"{coefficient}*{monomial}")
    return " + ".join(terms).replace("+ -", "- ")


def main() -> None:
    scalar.build_potential()
    betaV = beta_potential()
    projections = {
        "lamH": scale(betaV[(4, 0, 0, 0, 0, 0, 0, 0)], 4),
        "lamS": scale(betaV[(0, 0, 0, 0, 4, 0, 0, 0)], 4),
        "lamc": scale(betaV[(0, 0, 0, 0, 0, 0, 4, 0)], 4),
        "lamHS": scale(betaV[(2, 0, 0, 0, 2, 0, 0, 0)], 4),
        "lamHc": scale(betaV[(2, 0, 0, 0, 0, 0, 2, 0)], 4),
        "lamSc": scale(betaV[(0, 0, 0, 0, 2, 0, 2, 0)], 4),
        "kappa": scale(betaV[(0, 0, 0, 0, 1, 0, 3, 0)], 2),
    }
    F = Fraction
    expected = {
        "lamH": {("lamH", "lamH"): F(24), ("lamHS", "lamHS"): F(1), ("lamHc", "lamHc"): F(1)},
        "lamS": {("lamS", "lamS"): F(20), ("lamHS", "lamHS"): F(2), ("lamSc", "lamSc"): F(1)},
        "lamc": {("lamc", "lamc"): F(20), ("lamHc", "lamHc"): F(2), ("lamSc", "lamSc"): F(1), ("kappa", "kappa"): F(18)},
        "lamHS": {("lamH", "lamHS"): F(12), ("lamHS", "lamS"): F(8), ("lamHS", "lamHS"): F(4), ("lamHc", "lamSc"): F(2)},
        "lamHc": {("lamH", "lamHc"): F(12), ("lamHc", "lamc"): F(8), ("lamHc", "lamHc"): F(4), ("lamHS", "lamSc"): F(2)},
        "lamSc": {("lamS", "lamSc"): F(8), ("lamSc", "lamc"): F(8), ("lamSc", "lamSc"): F(4), ("lamHS", "lamHc"): F(4), ("kappa", "kappa"): F(36)},
        "kappa": {("kappa", "lamc"): F(12), ("kappa", "lamSc"): F(6)},
    }
    if projections != expected:
        raise RuntimeError(f"Effective-potential scalar RGE check failed: {projections} != {expected}")
    print("Independent one-loop effective-potential Hessian check passed exactly.")
    for name, poly in projections.items():
        print(f"beta_{name} = {fmt(poly)}")


if __name__ == "__main__":
    main()
