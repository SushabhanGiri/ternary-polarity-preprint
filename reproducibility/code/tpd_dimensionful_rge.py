#!/usr/bin/env python3
"""Exact scalar-only one-loop dimensionful RGEs for TP-D.

The potential is represented in eight real fields.  The complex-singlet cubic
normalization uses k_A=mu_A/sqrt(2) and k_B=mu_B/sqrt(2):

  V_cubic = -k_A A1^3/3 + k_A A1 A2^2 + (A -> B).

Two implementations are required to agree coefficient by coefficient:

1. extraction from (1/2) Tr[(V'')^2];
2. direct mass/cubic/quartic tensor contractions.

All returned polynomials are the numerators of (16*pi^2) beta_parameter.
Gauge, Yukawa, and threshold terms are deliberately outside this file.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path


N = 8
H = range(4)
A = range(4, 6)
B = range(6, 8)
Powers = tuple[int, ...]
Linear = dict[str, Fraction]
Quadratic = dict[tuple[str, str], Fraction]
FieldPolynomial = dict[Powers, Linear]

PARAMETERS = (
    "muH2", "mA2", "mB2", "kA", "kB",
    "lambda_H", "lambda_A", "lambda_B",
    "lambda_HA", "lambda_HB", "lambda_AB",
)


def add_term(poly: FieldPolynomial, parameter: str, coefficient: Fraction, indices) -> None:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    key = tuple(powers)
    if key not in poly:
        poly[key] = {}
    poly[key][parameter] = poly[key].get(parameter, Fraction(0)) + coefficient


def build_potential() -> FieldPolynomial:
    out: FieldPolynomial = {}
    for i in H:
        add_term(out, "muH2", Fraction(-1, 2), (i, i))
    for i in A:
        add_term(out, "mA2", Fraction(1, 2), (i, i))
    for i in B:
        add_term(out, "mB2", Fraction(1, 2), (i, i))

    # Real-component form of -(mu/3)(Phi^3+Phi*^3), with k=mu/sqrt(2).
    add_term(out, "kA", Fraction(-1, 3), (4, 4, 4))
    add_term(out, "kA", Fraction(1), (4, 5, 5))
    add_term(out, "kB", Fraction(-1, 3), (6, 6, 6))
    add_term(out, "kB", Fraction(1), (6, 7, 7))

    for sector, name in ((H, "lambda_H"), (A, "lambda_A"), (B, "lambda_B")):
        for i in sector:
            for j in sector:
                add_term(out, name, Fraction(1, 4), (i, i, j, j))
    for first, second, name in (
        (H, A, "lambda_HA"),
        (H, B, "lambda_HB"),
        (A, B, "lambda_AB"),
    ):
        for i in first:
            for j in second:
                add_term(out, name, Fraction(1, 4), (i, i, j, j))
    return out


def multiply_linear(left: Linear, right: Linear) -> Quadratic:
    out: defaultdict[tuple[str, str], Fraction] = defaultdict(Fraction)
    for name_l, coefficient_l in left.items():
        for name_r, coefficient_r in right.items():
            out[tuple(sorted((name_l, name_r)))] += coefficient_l * coefficient_r
    return {key: value for key, value in out.items() if value}


def add_quadratic(target: defaultdict, source: Quadratic, factor: Fraction = Fraction(1)) -> None:
    for key, value in source.items():
        target[key] += factor * value


def derivative_entry(poly: FieldPolynomial, a: int, b: int) -> FieldPolynomial:
    out: dict[Powers, defaultdict[str, Fraction]] = {}
    for powers, linear in poly.items():
        if powers[a] == 0 or powers[b] - (1 if a == b else 0) == 0:
            continue
        factor = Fraction(powers[a] * (powers[b] - (1 if a == b else 0)))
        reduced = list(powers)
        reduced[a] -= 1
        reduced[b] -= 1
        key = tuple(reduced)
        if key not in out:
            out[key] = defaultdict(Fraction)
        for name, coefficient in linear.items():
            out[key][name] += factor * coefficient
    return {key: dict(value) for key, value in out.items()}


def multiply_field_polys(left: FieldPolynomial, right: FieldPolynomial) -> dict[Powers, Quadratic]:
    out: dict[Powers, defaultdict[tuple[str, str], Fraction]] = {}
    for powers_l, linear_l in left.items():
        for powers_r, linear_r in right.items():
            key = tuple(x + y for x, y in zip(powers_l, powers_r))
            if key not in out:
                out[key] = defaultdict(Fraction)
            add_quadratic(out[key], multiply_linear(linear_l, linear_r))
    return {key: dict(value) for key, value in out.items()}


def effective_beta_potential(poly: FieldPolynomial) -> dict[Powers, Quadratic]:
    hessian = [[derivative_entry(poly, i, j) for j in range(N)] for i in range(N)]
    out: dict[Powers, defaultdict[tuple[str, str], Fraction]] = {}
    for i in range(N):
        for j in range(N):
            for powers, quadratic in multiply_field_polys(hessian[i][j], hessian[j][i]).items():
                if powers not in out:
                    out[powers] = defaultdict(Fraction)
                add_quadratic(out[powers], quadratic, Fraction(1, 2))
    return {key: {term: value for term, value in quadratic.items() if value} for key, quadratic in out.items()}


def tensor(poly: FieldPolynomial, indices: tuple[int, ...]) -> Linear:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    factor = 1
    for power in powers:
        factor *= factorial(power)
    return {
        name: coefficient * factor
        for name, coefficient in poly.get(tuple(powers), {}).items()
    }


def tensor_beta_mass(poly: FieldPolynomial, a: int, b: int) -> Quadratic:
    out: defaultdict[tuple[str, str], Fraction] = defaultdict(Fraction)
    for e, f in product(range(N), repeat=2):
        add_quadratic(out, multiply_linear(tensor(poly, (a, b, e, f)), tensor(poly, (e, f))))
        add_quadratic(out, multiply_linear(tensor(poly, (a, e, f)), tensor(poly, (b, e, f))))
    return {key: value for key, value in out.items() if value}


def tensor_beta_cubic(poly: FieldPolynomial, a: int, b: int, c: int) -> Quadratic:
    out: defaultdict[tuple[str, str], Fraction] = defaultdict(Fraction)
    for e, f in product(range(N), repeat=2):
        for quartic_indices, cubic_indices in (
            ((a, b, e, f), (c, e, f)),
            ((a, c, e, f), (b, e, f)),
            ((b, c, e, f), (a, e, f)),
        ):
            add_quadratic(out, multiply_linear(tensor(poly, quartic_indices), tensor(poly, cubic_indices)))
    return {key: value for key, value in out.items() if value}


def tensor_beta_quartic(poly: FieldPolynomial, a: int, b: int, c: int, d: int) -> Quadratic:
    out: defaultdict[tuple[str, str], Fraction] = defaultdict(Fraction)
    for e, f in product(range(N), repeat=2):
        for left, right in (
            ((a, b, e, f), (e, f, c, d)),
            ((a, c, e, f), (e, f, b, d)),
            ((a, d, e, f), (e, f, b, c)),
        ):
            add_quadratic(out, multiply_linear(tensor(poly, left), tensor(poly, right)))
    return {key: value for key, value in out.items() if value}


def scale(poly: Quadratic, factor: Fraction) -> Quadratic:
    return {key: factor * value for key, value in poly.items() if value}


def project_effective(beta_v: dict[Powers, Quadratic]) -> dict[str, Quadratic]:
    def key(*indices: int) -> Powers:
        powers = [0] * N
        for index in indices:
            powers[index] += 1
        return tuple(powers)

    return {
        "muH2": scale(beta_v[key(0, 0)], Fraction(-2)),
        "mA2": scale(beta_v[key(4, 4)], Fraction(2)),
        "mB2": scale(beta_v[key(6, 6)], Fraction(2)),
        "kA": scale(beta_v[key(4, 4, 4)], Fraction(-3)),
        "kB": scale(beta_v[key(6, 6, 6)], Fraction(-3)),
        "lambda_H": scale(beta_v[key(0, 0, 0, 0)], Fraction(4)),
        "lambda_A": scale(beta_v[key(4, 4, 4, 4)], Fraction(4)),
        "lambda_B": scale(beta_v[key(6, 6, 6, 6)], Fraction(4)),
        "lambda_HA": scale(beta_v[key(0, 0, 4, 4)], Fraction(4)),
        "lambda_HB": scale(beta_v[key(0, 0, 6, 6)], Fraction(4)),
        "lambda_AB": scale(beta_v[key(4, 4, 6, 6)], Fraction(4)),
    }


def project_tensors(poly: FieldPolynomial) -> dict[str, Quadratic]:
    return {
        "muH2": scale(tensor_beta_mass(poly, 0, 0), Fraction(-1)),
        "mA2": tensor_beta_mass(poly, 4, 4),
        "mB2": tensor_beta_mass(poly, 6, 6),
        "kA": scale(tensor_beta_cubic(poly, 4, 4, 4), Fraction(-1, 2)),
        "kB": scale(tensor_beta_cubic(poly, 6, 6, 6), Fraction(-1, 2)),
        "lambda_H": scale(tensor_beta_quartic(poly, 0, 0, 0, 0), Fraction(1, 6)),
        "lambda_A": scale(tensor_beta_quartic(poly, 4, 4, 4, 4), Fraction(1, 6)),
        "lambda_B": scale(tensor_beta_quartic(poly, 6, 6, 6, 6), Fraction(1, 6)),
        "lambda_HA": tensor_beta_quartic(poly, 0, 0, 4, 4),
        "lambda_HB": tensor_beta_quartic(poly, 0, 0, 6, 6),
        "lambda_AB": tensor_beta_quartic(poly, 4, 4, 6, 6),
    }


def serialise(poly: Quadratic) -> dict[str, str]:
    return {"*".join(key): str(value) for key, value in sorted(poly.items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    potential = build_potential()
    effective = project_effective(effective_beta_potential(potential))
    tensors = project_tensors(potential)
    if effective != tensors:
        differing = {name: {"effective": effective[name], "tensor": tensors[name]}
                     for name in effective if effective[name] != tensors[name]}
        raise RuntimeError(f"Independent dimensionful RGE methods disagree: {differing}")

    # The alternative A1 A2 A2 projection must encode the same k_A beta,
    # and likewise for B.  This catches a broken Z3 tensor structure.
    alt_a = scale(tensor_beta_cubic(potential, 4, 5, 5), Fraction(1, 2))
    alt_b = scale(tensor_beta_cubic(potential, 6, 7, 7), Fraction(1, 2))
    if alt_a != tensors["kA"] or alt_b != tensors["kB"]:
        raise RuntimeError("Cubic beta tensor does not preserve the Z3 cubic structure")

    payload = {
        "schema_version": 1,
        "normalization": "Each polynomial is the scalar-only (16*pi^2) beta numerator; kA=muA/sqrt(2), kB=muB/sqrt(2)",
        "methods": ["one-loop effective-potential Hessian", "direct mass/cubic/quartic tensor contractions"],
        "exact_agreement": True,
        "z3_cubic_tensor_preserved": True,
        "beta_functions": {name: serialise(poly) for name, poly in tensors.items()},
        "scope": "Scalar-only one-loop MS-bar system. Gauge/Yukawa terms, thresholds, and two-loop terms are excluded.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
