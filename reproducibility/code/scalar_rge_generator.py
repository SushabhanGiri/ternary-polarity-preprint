#!/usr/bin/env python3
"""Independent tensor derivation of the scalar-only one-loop TP-1 quartic RGEs.

The real-scalar convention is V = lambda_abcd phi_a phi_b phi_c phi_d / 4!.
At one loop, omitting gauge and Yukawa terms,

 (16 pi^2) beta_abcd = lambda_abef lambda_efcd
                      + lambda_acef lambda_efbd
                      + lambda_adef lambda_efbc.

All arithmetic is exact.  The output is a reproducible intermediate result,
not the complete model RGE system.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial
from typing import DefaultDict, Dict, Iterable, Tuple


FIELDS = ("h1", "h2", "h3", "h4", "s1", "s2", "x1", "x2")
N = len(FIELDS)
H = range(0, 4)
S = range(4, 6)
X = range(6, 8)

Linear = Dict[str, Fraction]
Quadratic = Dict[Tuple[str, str], Fraction]
potential: DefaultDict[Tuple[int, ...], Linear] = defaultdict(dict)


def add_linear(target: Linear, coupling: str, coefficient: Fraction) -> None:
    target[coupling] = target.get(coupling, Fraction(0)) + coefficient
    if target[coupling] == 0:
        del target[coupling]


def add_monomial(coupling: str, coefficient: Fraction, indices: Iterable[int]) -> None:
    powers = [0] * N
    for i in indices:
        powers[i] += 1
    add_linear(potential[tuple(powers)], coupling, coefficient)


def build_potential() -> None:
    # Idempotence is essential because several validation modules call this
    # builder in one Python process.  Without clearing, coefficients would be
    # silently duplicated on every call.
    potential.clear()
    for i in H:
        for j in H:
            add_monomial("lamH", Fraction(1, 4), (i, i, j, j))
    for i in S:
        for j in S:
            add_monomial("lamS", Fraction(1, 4), (i, i, j, j))
    for i in X:
        for j in X:
            add_monomial("lamc", Fraction(1, 4), (i, i, j, j))
    for i in H:
        for j in S:
            add_monomial("lamHS", Fraction(1, 4), (i, i, j, j))
    for i in H:
        for j in X:
            add_monomial("lamHc", Fraction(1, 4), (i, i, j, j))
    for i in S:
        for j in X:
            add_monomial("lamSc", Fraction(1, 4), (i, i, j, j))

    # kappa/2 * [s1(x1^3-3 x1 x2^2) + s2(3 x1^2 x2-x2^3)]
    add_monomial("kappa", Fraction(1, 2), (4, 6, 6, 6))
    add_monomial("kappa", Fraction(-3, 2), (4, 6, 7, 7))
    add_monomial("kappa", Fraction(3, 2), (5, 6, 6, 7))
    add_monomial("kappa", Fraction(-1, 2), (5, 7, 7, 7))


def tensor(indices: Tuple[int, int, int, int]) -> Linear:
    powers = [0] * N
    for i in indices:
        powers[i] += 1
    key = tuple(powers)
    derivative_factor = 1
    for power in powers:
        derivative_factor *= factorial(power)
    return {name: coefficient * derivative_factor for name, coefficient in potential.get(key, {}).items()}


def multiply_linear(a: Linear, b: Linear) -> Quadratic:
    out: DefaultDict[Tuple[str, str], Fraction] = defaultdict(Fraction)
    for name_a, coeff_a in a.items():
        for name_b, coeff_b in b.items():
            key = tuple(sorted((name_a, name_b)))
            out[key] += coeff_a * coeff_b
    return dict(out)


def add_quadratic(target: DefaultDict[Tuple[str, str], Fraction], term: Quadratic) -> None:
    for key, coefficient in term.items():
        target[key] += coefficient


def beta_tensor(a: int, b: int, c: int, d: int) -> Quadratic:
    out: DefaultDict[Tuple[str, str], Fraction] = defaultdict(Fraction)
    for e, f in product(range(N), repeat=2):
        add_quadratic(out, multiply_linear(tensor((a, b, e, f)), tensor((e, f, c, d))))
        add_quadratic(out, multiply_linear(tensor((a, c, e, f)), tensor((e, f, b, d))))
        add_quadratic(out, multiply_linear(tensor((a, d, e, f)), tensor((e, f, b, c))))
    return {key: val for key, val in out.items() if val}


def divide(poly: Quadratic, denominator: int) -> Quadratic:
    return {key: val / denominator for key, val in poly.items()}


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def format_poly(poly: Quadratic) -> str:
    order = {name: i for i, name in enumerate(("lamH", "lamS", "lamc", "lamHS", "lamHc", "lamSc", "kappa"))}
    items = sorted(poly.items(), key=lambda item: (order[item[0][0]], order[item[0][1]]))
    pieces = []
    for (a, b), coefficient in items:
        sign = "+" if coefficient > 0 else "-"
        magnitude = abs(coefficient)
        monomial = f"{a}^2" if a == b else f"{a}*{b}"
        body = monomial if magnitude == 1 else f"{format_fraction(magnitude)}*{monomial}"
        if not pieces:
            pieces.append(body if sign == "+" else f"-{body}")
        else:
            pieces.append(f" {sign} {body}")
    return "".join(pieces) if pieces else "0"


def main() -> None:
    build_potential()
    projections = {
        "beta_lamH": divide(beta_tensor(0, 0, 0, 0), 6),
        "beta_lamS": divide(beta_tensor(4, 4, 4, 4), 6),
        "beta_lamc": divide(beta_tensor(6, 6, 6, 6), 6),
        "beta_lamHS": beta_tensor(0, 0, 4, 4),
        "beta_lamHc": beta_tensor(0, 0, 6, 6),
        "beta_lamSc": beta_tensor(4, 4, 6, 6),
        "beta_kappa": divide(beta_tensor(4, 6, 6, 6), 3),
    }
    print("Scalar-only one-loop contributions; each right-hand side equals (16*pi^2)*beta:")
    for name, poly in projections.items():
        print(f"{name} = {format_poly(poly)}")

    checks = {
        "O4_H_coefficient": projections["beta_lamH"].get(("lamH", "lamH")),
        "O2_S_coefficient": projections["beta_lamS"].get(("lamS", "lamS")),
        "O2_chi_coefficient": projections["beta_lamc"].get(("lamc", "lamc")),
    }
    expected = {"O4_H_coefficient": Fraction(24), "O2_S_coefficient": Fraction(20), "O2_chi_coefficient": Fraction(20)}
    if checks != expected:
        raise RuntimeError(f"O(N) cross-check failed: {checks} != {expected}")
    print("Checks: O(4) -> 24 lambda_H^2; O(2) -> 20 lambda^2 (passed).")


if __name__ == "__main__":
    main()
