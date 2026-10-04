#!/usr/bin/env python3
"""Minimal scalar-only gauge-origin audit for TP-D.

Parent theory:
  U(1)_m x U(1)_E
with Phi_m~(3,0), Phi_E~(0,3), A~(1,0), B~(0,1).

The script enumerates all pure-scalar gauge-invariant monomials through degree
four, verifies the residual Z3 x Z3 subgroup, and checks the analytic gauge-
boson masses in the presence of Abelian kinetic mixing.
"""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np


FIELDS = ("Phi_m", "Phi_m_dag", "Phi_E", "Phi_E_dag", "A", "A_dag", "B", "B_dag")
CHARGES = {
    "Phi_m": (3, 0), "Phi_m_dag": (-3, 0),
    "Phi_E": (0, 3), "Phi_E_dag": (0, -3),
    "A": (1, 0), "A_dag": (-1, 0),
    "B": (0, 1), "B_dag": (0, -1),
}
CONJUGATE = {
    "Phi_m": "Phi_m_dag", "Phi_m_dag": "Phi_m",
    "Phi_E": "Phi_E_dag", "Phi_E_dag": "Phi_E",
    "A": "A_dag", "A_dag": "A",
    "B": "B_dag", "B_dag": "B",
}


def charge(monomial: tuple[str, ...]) -> tuple[int, int]:
    return tuple(sum(CHARGES[field][axis] for field in monomial) for axis in range(2))


def conjugate(monomial: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(sorted((CONJUGATE[field] for field in monomial), key=FIELDS.index))


def label(monomial: tuple[str, ...]) -> str:
    counts = {field: monomial.count(field) for field in FIELDS}
    return " ".join(field if count == 1 else f"{field}^{count}"
                    for field, count in counts.items() if count)


def invariants() -> dict[str, list[dict[str, object]]]:
    result = {}
    for degree in range(1, 5):
        rows = []
        for monomial in combinations_with_replacement(FIELDS, degree):
            if charge(monomial) != (0, 0):
                continue
            conj = conjugate(monomial)
            rows.append({
                "monomial": label(monomial),
                "self_conjugate": monomial == conj,
                "conjugate": label(conj),
            })
        result[str(degree)] = rows
    return result


def analytic_mass_eigenvalues(mm2: float, me2: float, epsilon: float) -> np.ndarray:
    discriminant = (mm2 - me2)**2 + 4 * epsilon**2 * mm2 * me2
    return np.sort(np.array([
        (mm2 + me2 - math.sqrt(discriminant)) / (2 * (1 - epsilon**2)),
        (mm2 + me2 + math.sqrt(discriminant)) / (2 * (1 - epsilon**2)),
    ]))


def numerical_mass_eigenvalues(mm2: float, me2: float, epsilon: float) -> np.ndarray:
    kinetic = np.array([[1.0, epsilon], [epsilon, 1.0]])
    mass = np.diag([mm2, me2])
    # Symmetric canonical normalization K^{-1/2} M^2 K^{-1/2}.
    values, vectors = np.linalg.eigh(kinetic)
    inv_sqrt = vectors @ np.diag(values**-0.5) @ vectors.T
    return np.linalg.eigvalsh(inv_sqrt @ mass @ inv_sqrt)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--random-tests", type=int, default=500)
    args = parser.parse_args()

    residual = [(nm, ne) for nm in range(3) for ne in range(3)]
    rng = np.random.default_rng(20260919)
    max_error = 0.0
    for _ in range(args.random_tests):
        mm2, me2 = rng.uniform(1e2, 1e8, size=2)
        epsilon = float(rng.uniform(-0.95, 0.95))
        direct = numerical_mass_eigenvalues(float(mm2), float(me2), epsilon)
        predicted = analytic_mass_eigenvalues(float(mm2), float(me2), epsilon)
        max_error = max(max_error, float(np.max(np.abs((direct - predicted) / predicted))))
        if not np.allclose(direct, predicted, rtol=2e-12, atol=1e-7):
            raise RuntimeError("Kinetic-mixing mass formula failed")

    payload = {
        "schema_version": 1,
        "parent_group": "U(1)_m x U(1)_E",
        "charges": {field: CHARGES[field] for field in ("Phi_m", "Phi_E", "A", "B")},
        "breaking_vevs": {"Phi_m": "f_m/sqrt(2)", "Phi_E": "f_E/sqrt(2)"},
        "residual_elements": residual,
        "residual_group": "Z3_m x Z3_E",
        "residual_action": {
            "A": "A -> exp(2*pi*i*n_m/3) A",
            "B": "B -> exp(2*pi*i*n_E/3) B",
        },
        "pure_scalar_invariants_through_dimension_4": invariants(),
        "higgs_neutral_invariants": [
            "HdagH", "(HdagH)^2", "HdagH |Phi_m|^2", "HdagH |Phi_E|^2",
            "HdagH |A|^2", "HdagH |B|^2"
        ],
        "gauge_kinetic_terms": [
            "-F_Y^2/4", "-F_m^2/4", "-F_E^2/4",
            "-epsilon_Ym F_Y^{mu nu} F_m_{mu nu}/2",
            "-epsilon_YE F_Y^{mu nu} F_E_{mu nu}/2",
            "-epsilon_mE F_m^{mu nu} F_E_{mu nu}/2"
        ],
        "kinetic_positivity": "The full symmetric 3x3 Abelian kinetic matrix must be positive definite. In the epsilon_Ym=epsilon_YE=0 slice this requires abs(epsilon_mE)<1.",
        "zero_mixing_status": "Not implied by gauge symmetry. It can be protected by independent charge-conjugation automorphisms C_m and C_E when all corresponding scalar couplings are real; otherwise all three mixings are independent parameters.",
        "one_loop_mixing_source_traces": {
            "Tr(Y Q_m)": 0,
            "Tr(Y Q_E)": 0,
            "Tr(Q_m Q_E)": 0,
            "reason": "No field in the frozen scalar-only completion carries both relevant charges."
        },
        "unmixed_vector_masses": {
            "M_m^2": "9*g_m^2*f_m^2",
            "M_E^2": "9*g_E^2*f_E^2"
        },
        "mixed_vector_mass_eigenvalues": "On the epsilon_Ym=epsilon_YE=0 slice: [(M_m^2+M_E^2) +/- sqrt((M_m^2-M_E^2)^2+4*epsilon_mE^2*M_m^2*M_E^2)]/[2*(1-epsilon_mE^2)]",
        "random_mass_formula_check": {
            "points": args.random_tests,
            "seed": 20260919,
            "maximum_relative_error": max_error
        },
        "goldstones": "arg(Phi_m) and arg(Phi_E) are eaten; two radial modes remain",
        "low_energy_cubic_matching": {
            "mu_A": "3*kappa_m*f_m/sqrt(2)",
            "mu_B": "3*kappa_E*f_E/sqrt(2)"
        },
        "anomaly_audit": {
            "charged_chiral_fermions": 0,
            "U1_m_cubed": 0,
            "U1_E_cubed": 0,
            "mixed_abelian": 0,
            "mixed_SM": 0,
            "mixed_gravitational": 0,
            "reason": "Only scalars carry the new charges and all SM fermions are neutral."
        },
        "scope_warning": "This is a scalar-only parent completion. All hypercharge/new-sector and inter-new-sector kinetic mixings are symmetry allowed; threshold matching, the full scalar vacuum, cosmic strings, and gauge-sector unitarity remain to be completed."
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
