#!/usr/bin/env python3
"""Enumerate scalar monomials for the TP-D distinctness gate.

Fields:
    A ~ (1, 0), B ~ (0, 1) under Z3_m x Z3_E.
Their projected charges are both q_P = 1.

The script enumerates commuting, non-derivative A/B monomials through
engineering dimension four, groups Hermitian-conjugate pairs, and classifies
each class under the projected and full symmetries.  It separately records
the renormalizable Higgs-bilinear portals and kinetic terms.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


Exponent = tuple[int, int, int, int]  # (A, A^dagger, B, B^dagger)


@dataclass(frozen=True)
class OperatorClass:
    dimension: int
    representative: str
    conjugate: str
    self_conjugate: bool
    q_m: int
    q_e: int
    q_p: int
    projected_z3: bool
    dual_z3: bool
    comparator_only: bool


def conjugate(exp: Exponent) -> Exponent:
    a, ad, b, bd = exp
    return (ad, a, bd, b)


def charges(exp: Exponent) -> tuple[int, int, int]:
    a, ad, b, bd = exp
    q_m = (a - ad) % 3
    q_e = (b - bd) % 3
    return q_m, q_e, (q_m + q_e) % 3


def monomial(exp: Exponent) -> str:
    labels = ("A", "A†", "B", "B†")
    pieces: list[str] = []
    for label, power in zip(labels, exp):
        if power == 1:
            pieces.append(label)
        elif power > 1:
            pieces.append(f"{label}^{power}")
    return " ".join(pieces) if pieces else "1"


def canonical_pair(exp: Exponent) -> tuple[Exponent, Exponent]:
    conj = conjugate(exp)
    return (exp, conj) if exp <= conj else (conj, exp)


def enumerate_nonderivative() -> list[OperatorClass]:
    seen: set[tuple[Exponent, Exponent]] = set()
    result: list[OperatorClass] = []
    for dimension in range(1, 5):
        for a in range(dimension + 1):
            for ad in range(dimension - a + 1):
                for b in range(dimension - a - ad + 1):
                    bd = dimension - a - ad - b
                    exp = (a, ad, b, bd)
                    q_m, q_e, q_p = charges(exp)
                    if q_p != 0:
                        continue
                    pair = canonical_pair(exp)
                    if pair in seen:
                        continue
                    seen.add(pair)
                    rep, conj = pair
                    q_m, q_e, q_p = charges(rep)
                    dual = q_m == 0 and q_e == 0
                    result.append(
                        OperatorClass(
                            dimension=dimension,
                            representative=monomial(rep),
                            conjugate=monomial(conj),
                            self_conjugate=rep == conj,
                            q_m=q_m,
                            q_e=q_e,
                            q_p=q_p,
                            projected_z3=True,
                            dual_z3=dual,
                            comparator_only=not dual,
                        )
                    )
    return sorted(result, key=lambda item: (item.dimension, item.representative))


def extra_operators() -> dict[str, list[dict[str, object]]]:
    return {
        "kinetic_dimension_4": [
            {
                "operator": "∂_μ A† ∂^μ A",
                "projected_z3": True,
                "dual_z3": True,
            },
            {
                "operator": "∂_μ B† ∂^μ B",
                "projected_z3": True,
                "dual_z3": True,
            },
            {
                "operator": "∂_μ A† ∂^μ B + h.c.",
                "projected_z3": True,
                "dual_z3": False,
            },
        ],
        "higgs_portals": [
            {
                "dimension": 4,
                "operator": "(H†H)|A|²",
                "projected_z3": True,
                "dual_z3": True,
            },
            {
                "dimension": 4,
                "operator": "(H†H)|B|²",
                "projected_z3": True,
                "dual_z3": True,
            },
            {
                "dimension": 4,
                "operator": "(H†H)A†B + h.c.",
                "projected_z3": True,
                "dual_z3": False,
            },
        ],
    }


def build_payload() -> dict[str, object]:
    operators = enumerate_nonderivative()
    return {
        "schema_version": 1,
        "field_order": ["A", "A_dagger", "B", "B_dagger"],
        "charges": {"A": [1, 0], "B": [0, 1]},
        "projection": "q_P = q_m + q_E mod 3",
        "kernel": [[0, 0], [1, 2], [2, 1]],
        "non_derivative_operator_classes": [asdict(item) for item in operators],
        "comparator_only_non_derivative": [
            asdict(item) for item in operators if item.comparator_only
        ],
        **extra_operators(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
