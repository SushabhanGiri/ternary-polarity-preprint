#!/usr/bin/env python3
"""Two-method exact one-loop scalar-quartic RGE derivation for TP-D.

Method 1 contracts the four-index quartic tensor. Method 2 evaluates
1/2 Tr[(V''_4)^2]. All arithmetic is rational and the results must agree
coefficient by coefficient.
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
H, A, B = range(4), range(4, 6), range(6, 8)
NAMES = ("lambda_H", "lambda_A", "lambda_B", "lambda_HA", "lambda_HB", "lambda_AB")
Powers = tuple[int, ...]
Linear = dict[str, Fraction]
Quadratic = dict[tuple[str, str], Fraction]
potential: dict[Powers, dict[str, Fraction]] = {}


def add_monomial(name: str, coefficient: Fraction, indices) -> None:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    key = tuple(powers)
    if key not in potential:
        potential[key] = {}
    potential[key][name] = potential[key].get(name, Fraction(0)) + coefficient


def build_potential() -> None:
    potential.clear()
    for sector, name in ((H, "lambda_H"), (A, "lambda_A"), (B, "lambda_B")):
        for i in sector:
            for j in sector:
                add_monomial(name, Fraction(1, 4), (i, i, j, j))
    for first, second, name in (
        (H, A, "lambda_HA"),
        (H, B, "lambda_HB"),
        (A, B, "lambda_AB"),
    ):
        for i in first:
            for j in second:
                add_monomial(name, Fraction(1, 4), (i, i, j, j))


def tensor(indices: tuple[int, int, int, int]) -> Linear:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    factor = 1
    for power in powers:
        factor *= factorial(power)
    return {name: coefficient * factor for name, coefficient in potential.get(tuple(powers), {}).items()}


def multiply_linear(left: Linear, right: Linear) -> Quadratic:
    out = defaultdict(Fraction)
    for name_l, coeff_l in left.items():
        for name_r, coeff_r in right.items():
            out[tuple(sorted((name_l, name_r)))] += coeff_l * coeff_r
    return dict(out)


def beta_tensor(a: int, b: int, c: int, d: int) -> Quadratic:
    out = defaultdict(Fraction)
    for e, f in product(range(N), repeat=2):
        for left, right in (
            ((a, b, e, f), (e, f, c, d)),
            ((a, c, e, f), (e, f, b, d)),
            ((a, d, e, f), (e, f, b, c)),
        ):
            for key, value in multiply_linear(tensor(left), tensor(right)).items():
                out[key] += value
    return dict(out)


def derivative_entry(a: int, b: int):
    out: dict[Powers, dict[str, Fraction]] = {}
    for powers, poly in potential.items():
        if powers[a] == 0 or powers[b] - (1 if a == b else 0) == 0:
            continue
        factor = Fraction(powers[a] * (powers[b] - (1 if a == b else 0)))
        reduced = list(powers)
        reduced[a] -= 1
        reduced[b] -= 1
        key = tuple(reduced)
        if key not in out:
            out[key] = defaultdict(Fraction)
        for name, coefficient in poly.items():
            out[key][name] += factor * coefficient
    return {key: dict(value) for key, value in out.items()}


def multiply_field_polys(left, right):
    out = {}
    for powers_l, poly_l in left.items():
        for powers_r, poly_r in right.items():
            key = tuple(x + y for x, y in zip(powers_l, powers_r))
            if key not in out:
                out[key] = defaultdict(Fraction)
            for names, value in multiply_linear(poly_l, poly_r).items():
                out[key][names] += value
    return {key: dict(value) for key, value in out.items()}


def beta_potential():
    hessian = [[derivative_entry(i, j) for j in range(N)] for i in range(N)]
    out = {}
    for i in range(N):
        for j in range(N):
            for powers, poly in multiply_field_polys(hessian[i][j], hessian[j][i]).items():
                if powers not in out:
                    out[powers] = defaultdict(Fraction)
                for names, coefficient in poly.items():
                    out[powers][names] += coefficient / 2
    return {key: dict(value) for key, value in out.items()}


def scale(poly: Quadratic, factor: Fraction) -> Quadratic:
    return {key: factor * value for key, value in poly.items() if value}


def projections_tensor() -> dict[str, Quadratic]:
    return {
        "lambda_H": scale(beta_tensor(0, 0, 0, 0), Fraction(1, 6)),
        "lambda_A": scale(beta_tensor(4, 4, 4, 4), Fraction(1, 6)),
        "lambda_B": scale(beta_tensor(6, 6, 6, 6), Fraction(1, 6)),
        "lambda_HA": beta_tensor(0, 0, 4, 4),
        "lambda_HB": beta_tensor(0, 0, 6, 6),
        "lambda_AB": beta_tensor(4, 4, 6, 6),
    }


def projections_hessian() -> dict[str, Quadratic]:
    beta_v = beta_potential()
    keys = {
        "lambda_H": (4, 0, 0, 0, 0, 0, 0, 0),
        "lambda_A": (0, 0, 0, 0, 4, 0, 0, 0),
        "lambda_B": (0, 0, 0, 0, 0, 0, 4, 0),
        "lambda_HA": (2, 0, 0, 0, 2, 0, 0, 0),
        "lambda_HB": (2, 0, 0, 0, 0, 0, 2, 0),
        "lambda_AB": (0, 0, 0, 0, 2, 0, 2, 0),
    }
    return {name: scale(beta_v[key], Fraction(4)) for name, key in keys.items()}


def serialise(poly: Quadratic) -> dict[str, str]:
    return {"*".join(key): str(value) for key, value in sorted(poly.items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    build_potential()
    tensor_result = projections_tensor()
    hessian_result = projections_hessian()
    if tensor_result != hessian_result:
        raise RuntimeError(f"Independent RGE methods disagree: {tensor_result} != {hessian_result}")
    expected = {
        "lambda_H": {("lambda_H", "lambda_H"): Fraction(24), ("lambda_HA", "lambda_HA"): Fraction(1), ("lambda_HB", "lambda_HB"): Fraction(1)},
        "lambda_A": {("lambda_A", "lambda_A"): Fraction(20), ("lambda_HA", "lambda_HA"): Fraction(2), ("lambda_AB", "lambda_AB"): Fraction(1)},
        "lambda_B": {("lambda_B", "lambda_B"): Fraction(20), ("lambda_HB", "lambda_HB"): Fraction(2), ("lambda_AB", "lambda_AB"): Fraction(1)},
        "lambda_HA": {("lambda_H", "lambda_HA"): Fraction(12), ("lambda_A", "lambda_HA"): Fraction(8), ("lambda_HA", "lambda_HA"): Fraction(4), ("lambda_AB", "lambda_HB"): Fraction(2)},
        "lambda_HB": {("lambda_H", "lambda_HB"): Fraction(12), ("lambda_B", "lambda_HB"): Fraction(8), ("lambda_HB", "lambda_HB"): Fraction(4), ("lambda_AB", "lambda_HA"): Fraction(2)},
        "lambda_AB": {("lambda_A", "lambda_AB"): Fraction(8), ("lambda_AB", "lambda_B"): Fraction(8), ("lambda_AB", "lambda_AB"): Fraction(4), ("lambda_HA", "lambda_HB"): Fraction(4)},
    }
    if tensor_result != expected:
        raise RuntimeError(f"RGE normalization check failed: {tensor_result} != {expected}")
    payload = {
        "schema_version": 1,
        "normalization": "Each polynomial is (16*pi^2) beta_lambda, scalar-only one-loop",
        "methods": ["four-index quartic tensor", "one-loop effective-potential Hessian"],
        "exact_agreement": True,
        "beta_functions": {name: serialise(poly) for name, poly in tensor_result.items()},
        "scope": "Scalar quartics only. Standard-Model gauge/Yukawa terms and dimensionful mass/cubic beta functions are separate tasks.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
