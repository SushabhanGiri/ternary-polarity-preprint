#!/usr/bin/env python3
"""Exact scalar-only one-loop quartic RGEs for the general TP-G parent.

The parent has H plus four complex singlets A, B, Phi_m, Phi_E.  The
potential contains five self quartics, ten modulus portals, and the two real
phase-sensitive couplings

    kappa_m Phi_m^dag A^3 + h.c.,
    kappa_E Phi_E^dag B^3 + h.c.

Two independent implementations are used:
  (1) 1/2 Tr[(V''_4)^2] as a polynomial in the real fields;
  (2) direct quartic-tensor contractions for representative projections.

All arithmetic is exact.  The output convention is
    output[ coupling ] = (16*pi^2) beta_coupling.
Gauge, Yukawa, and dimensionful terms are deliberately excluded.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path


N = 12
SECTORS = {
    "H": tuple(range(0, 4)),
    "A": tuple(range(4, 6)),
    "B": tuple(range(6, 8)),
    "Phi_m": tuple(range(8, 10)),
    "Phi_E": tuple(range(10, 12)),
}
SELF = {
    "H": "lambda_H",
    "A": "lambda_A",
    "B": "lambda_B",
    "Phi_m": "lambda_Phi_m",
    "Phi_E": "lambda_Phi_E",
}
PORTALS = {
    ("H", "A"): "lambda_HA",
    ("H", "B"): "lambda_HB",
    ("H", "Phi_m"): "lambda_HPhi_m",
    ("H", "Phi_E"): "lambda_HPhi_E",
    ("A", "B"): "lambda_AB",
    ("A", "Phi_m"): "lambda_APhi_m",
    ("A", "Phi_E"): "lambda_APhi_E",
    ("B", "Phi_m"): "lambda_BPhi_m",
    ("B", "Phi_E"): "lambda_BPhi_E",
    ("Phi_m", "Phi_E"): "lambda_Phi_mPhi_E",
}
COUPLINGS = tuple(SELF.values()) + tuple(PORTALS.values()) + ("kappa_m", "kappa_E")
Powers = tuple[int, ...]
Linear = dict[str, Fraction]
Quadratic = dict[tuple[str, str], Fraction]


def add(poly: dict[Powers, Linear], name: str, coefficient: Fraction, indices) -> None:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    key = tuple(powers)
    if key not in poly:
        poly[key] = {}
    poly[key][name] = poly[key].get(name, Fraction(0)) + coefficient


def potential() -> dict[Powers, Linear]:
    poly: dict[Powers, Linear] = {}
    for sector_name, coupling in SELF.items():
        sector = SECTORS[sector_name]
        for i in sector:
            for j in sector:
                add(poly, coupling, Fraction(1, 4), (i, i, j, j))
    for (left_name, right_name), coupling in PORTALS.items():
        for i in SECTORS[left_name]:
            for j in SECTORS[right_name]:
                add(poly, coupling, Fraction(1, 4), (i, i, j, j))

    # For real kappa:
    # kappa Phi^dag X^3+h.c. = kappa/2 [p(x^3-3xy^2)+q(3x^2y-y^3)].
    for real, imag, p, q, coupling in (
        (4, 5, 8, 9, "kappa_m"),
        (6, 7, 10, 11, "kappa_E"),
    ):
        add(poly, coupling, Fraction(1, 2), (p, real, real, real))
        add(poly, coupling, Fraction(-3, 2), (p, real, imag, imag))
        add(poly, coupling, Fraction(3, 2), (q, real, real, imag))
        add(poly, coupling, Fraction(-1, 2), (q, imag, imag, imag))
    return poly


def multiply_linear(left: Linear, right: Linear) -> Quadratic:
    out: defaultdict[tuple[str, str], Fraction] = defaultdict(Fraction)
    for name_l, value_l in left.items():
        for name_r, value_r in right.items():
            out[tuple(sorted((name_l, name_r)))] += value_l * value_r
    return dict(out)


def derivative_entry(poly: dict[Powers, Linear], a: int, b: int) -> dict[Powers, Linear]:
    out: dict[Powers, defaultdict[str, Fraction]] = {}
    for powers, expression in poly.items():
        second = powers[b] - (1 if a == b else 0)
        if powers[a] == 0 or second == 0:
            continue
        factor = powers[a] * second
        reduced = list(powers)
        reduced[a] -= 1
        reduced[b] -= 1
        key = tuple(reduced)
        if key not in out:
            out[key] = defaultdict(Fraction)
        for name, value in expression.items():
            out[key][name] += factor * value
    return {key: dict(value) for key, value in out.items()}


def multiply_field_polys(left: dict[Powers, Linear], right: dict[Powers, Linear]) -> dict[Powers, Quadratic]:
    out: dict[Powers, defaultdict[tuple[str, str], Fraction]] = {}
    for powers_l, expression_l in left.items():
        for powers_r, expression_r in right.items():
            key = tuple(x + y for x, y in zip(powers_l, powers_r))
            if key not in out:
                out[key] = defaultdict(Fraction)
            for names, value in multiply_linear(expression_l, expression_r).items():
                out[key][names] += value
    return {key: dict(value) for key, value in out.items()}


def beta_potential(poly: dict[Powers, Linear]) -> dict[Powers, Quadratic]:
    hessian = [[derivative_entry(poly, i, j) for j in range(N)] for i in range(N)]
    out: dict[Powers, defaultdict[tuple[str, str], Fraction]] = {}
    for i in range(N):
        for j in range(N):
            for powers, expression in multiply_field_polys(hessian[i][j], hessian[j][i]).items():
                if powers not in out:
                    out[powers] = defaultdict(Fraction)
                for names, value in expression.items():
                    out[powers][names] += value / 2
    return {key: dict(value) for key, value in out.items()}


def monomial(indices) -> Powers:
    powers = [0] * N
    for index in indices:
        powers[index] += 1
    return tuple(powers)


def scale(expression: Quadratic, factor: Fraction) -> Quadratic:
    return {key: value * factor for key, value in expression.items() if value}


def project_hessian(beta_v: dict[Powers, Quadratic]) -> dict[str, Quadratic]:
    result: dict[str, Quadratic] = {}
    for sector_name, coupling in SELF.items():
        i = SECTORS[sector_name][0]
        result[coupling] = scale(beta_v[monomial((i, i, i, i))], Fraction(4))
    for (left_name, right_name), coupling in PORTALS.items():
        i, j = SECTORS[left_name][0], SECTORS[right_name][0]
        result[coupling] = scale(beta_v[monomial((i, i, j, j))], Fraction(4))

    phase_projections = {
        "kappa_m": [
            (monomial((8, 4, 4, 4)), Fraction(2)),
            (monomial((8, 4, 5, 5)), Fraction(-2, 3)),
            (monomial((9, 4, 4, 5)), Fraction(2, 3)),
            (monomial((9, 5, 5, 5)), Fraction(-2)),
        ],
        "kappa_E": [
            (monomial((10, 6, 6, 6)), Fraction(2)),
            (monomial((10, 6, 7, 7)), Fraction(-2, 3)),
            (monomial((11, 6, 6, 7)), Fraction(2, 3)),
            (monomial((11, 7, 7, 7)), Fraction(-2)),
        ],
    }
    for coupling, projections in phase_projections.items():
        candidates = [scale(beta_v[key], factor) for key, factor in projections]
        if any(candidate != candidates[0] for candidate in candidates[1:]):
            raise RuntimeError(f"Broken phase-tensor covariance for {coupling}: {candidates}")
        result[coupling] = candidates[0]
    return result


def tensor(poly: dict[Powers, Linear], indices: tuple[int, int, int, int]) -> Linear:
    powers = monomial(indices)
    factor = 1
    for power in powers:
        factor *= factorial(power)
    return {name: value * factor for name, value in poly.get(powers, {}).items()}


def beta_tensor(poly: dict[Powers, Linear], a: int, b: int, c: int, d: int) -> Quadratic:
    out: defaultdict[tuple[str, str], Fraction] = defaultdict(Fraction)
    for e, f in product(range(N), repeat=2):
        for left, right in (
            ((a, b, e, f), (e, f, c, d)),
            ((a, c, e, f), (e, f, b, d)),
            ((a, d, e, f), (e, f, b, c)),
        ):
            for names, value in multiply_linear(tensor(poly, left), tensor(poly, right)).items():
                out[names] += value
    return dict(out)


def tensor_cross_checks(poly: dict[Powers, Linear], projected: dict[str, Quadratic]) -> dict[str, bool]:
    checks = {
        "lambda_H": scale(beta_tensor(poly, 0, 0, 0, 0), Fraction(1, 6)),
        "lambda_A": scale(beta_tensor(poly, 4, 4, 4, 4), Fraction(1, 6)),
        "lambda_HPhi_m": beta_tensor(poly, 0, 0, 8, 8),
        "lambda_APhi_m": beta_tensor(poly, 4, 4, 8, 8),
        "lambda_Phi_mPhi_E": beta_tensor(poly, 8, 8, 10, 10),
        "kappa_m": scale(beta_tensor(poly, 8, 4, 4, 4), Fraction(1, 3)),
        "kappa_E": scale(beta_tensor(poly, 10, 6, 6, 6), Fraction(1, 3)),
    }
    return {name: expression == projected[name] for name, expression in checks.items()}


def serialise(expression: Quadratic) -> dict[str, str]:
    return {"*".join(key): str(value) for key, value in sorted(expression.items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    poly = potential()
    projected = project_hessian(beta_potential(poly))
    checks = tensor_cross_checks(poly, projected)
    if not all(checks.values()):
        raise RuntimeError(f"Independent tensor checks failed: {checks}")

    # The exact TP-D subtheory must reappear when all parent couplings vanish.
    low_expected = {
        "lambda_H": {("lambda_H", "lambda_H"): Fraction(24), ("lambda_HA", "lambda_HA"): Fraction(1), ("lambda_HB", "lambda_HB"): Fraction(1)},
        "lambda_A": {("lambda_A", "lambda_A"): Fraction(20), ("lambda_HA", "lambda_HA"): Fraction(2), ("lambda_AB", "lambda_AB"): Fraction(1)},
        "lambda_B": {("lambda_B", "lambda_B"): Fraction(20), ("lambda_HB", "lambda_HB"): Fraction(2), ("lambda_AB", "lambda_AB"): Fraction(1)},
        "lambda_HA": {("lambda_H", "lambda_HA"): Fraction(12), ("lambda_A", "lambda_HA"): Fraction(8), ("lambda_HA", "lambda_HA"): Fraction(4), ("lambda_AB", "lambda_HB"): Fraction(2)},
        "lambda_HB": {("lambda_H", "lambda_HB"): Fraction(12), ("lambda_B", "lambda_HB"): Fraction(8), ("lambda_HB", "lambda_HB"): Fraction(4), ("lambda_AB", "lambda_HA"): Fraction(2)},
        "lambda_AB": {("lambda_A", "lambda_AB"): Fraction(8), ("lambda_AB", "lambda_B"): Fraction(8), ("lambda_AB", "lambda_AB"): Fraction(4), ("lambda_HA", "lambda_HB"): Fraction(4)},
    }
    low_names = set(low_expected)
    for coupling, expected in low_expected.items():
        restricted = {
            names: value for names, value in projected[coupling].items()
            if all(name in low_names for name in names)
        }
        if restricted != expected:
            raise RuntimeError(f"Low-energy projection failed for {coupling}: {restricted}")

    zero_surface_sources = {}
    benchmark_nonzero = {
        "lambda_H", "lambda_A", "lambda_B", "lambda_Phi_m", "lambda_Phi_E",
        "lambda_HA", "lambda_HB", "lambda_AB", "kappa_m", "kappa_E",
    }
    for coupling in COUPLINGS:
        if coupling in benchmark_nonzero:
            continue
        source = {
            names: value for names, value in projected[coupling].items()
            if coupling not in names and all(name in benchmark_nonzero for name in names)
        }
        zero_surface_sources[coupling] = serialise(source)

    payload = {
        "schema_version": 1,
        "normalization": "Each polynomial is (16*pi^2) beta_coupling, scalar-only one-loop",
        "field_content": "H (4 real components) plus A, B, Phi_m, Phi_E (2 real components each)",
        "coupling_count": len(COUPLINGS),
        "couplings": COUPLINGS,
        "methods": ["one-loop effective-potential Hessian", "independent quartic-tensor projections"],
        "tensor_cross_checks": checks,
        "low_energy_TP_D_limit_verified": True,
        "beta_functions": {name: serialise(projected[name]) for name in COUPLINGS},
        "TP_G0_zero_portal_sources": zero_surface_sources,
        "scope_warning": "Scalar-only one-loop system. Gauge, Yukawa, dimensionful, kinetic-mixing, and threshold terms remain separate.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
