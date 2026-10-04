#!/usr/bin/env python3
"""Finite-energy physical-scalar unitarity audit for TP-D benchmark B0.

Includes the physical Higgs and both real components of each inert complex
singlet.  Every scalar contact and s/t/u exchange diagram is included.  SM
Goldstones, longitudinal/transverse vectors, and any UV gauge-origin states
are outside this deliberately limited calculation.
"""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np

import finite_energy_unitarity as engine
import tpd_ew_vacuum as vacuum
import tpd_scalar_rge as scalar


LABELS = ("h", "G1", "G2", "G3", "A1", "A2", "B1", "B2")
PHYSICAL = (0, 4, 5, 6, 7)


def benchmark() -> vacuum.Parameters:
    v, mh = 246.22, 125.25
    lambda_h = mh**2 / (2 * v**2)
    lambda_ha, lambda_hb = 0.020, 0.030
    return vacuum.Parameters(
        mu_h2=lambda_h * v**2,
        m_a2=180.0**2 - 0.5 * lambda_ha * v**2,
        m_b2=400.0**2 - 0.5 * lambda_hb * v**2,
        mu_a=60.0,
        mu_b=90.0,
        lambda_h=lambda_h,
        lambda_a=0.20,
        lambda_b=0.25,
        lambda_ha=lambda_ha,
        lambda_hb=lambda_hb,
        lambda_ab=0.10,
    )


def tensors(p: vacuum.Parameters) -> dict[str, np.ndarray]:
    scalar.build_potential()
    couplings = {
        "lambda_H": p.lambda_h,
        "lambda_A": p.lambda_a,
        "lambda_B": p.lambda_b,
        "lambda_HA": p.lambda_ha,
        "lambda_HB": p.lambda_hb,
        "lambda_AB": p.lambda_ab,
    }
    quartic = np.zeros((scalar.N,) * 4)
    for indices in np.ndindex(quartic.shape):
        quartic[indices] = sum(
            float(coefficient) * couplings[name]
            for name, coefficient in scalar.tensor(indices).items()
        )

    vev = np.zeros(scalar.N)
    vev[0] = 246.22
    cubic = np.einsum("abcd,d->abc", quartic, vev)
    # Phase convention:
    # V contains -mu_A(A^3+A*^3)/3 and similarly for B, with
    # A=(A1+i A2)/sqrt(2).  These are third derivatives of V.
    for first, second, mu in ((4, 5, p.mu_a), (6, 7, p.mu_b)):
        cubic[first, first, first] += -math.sqrt(2) * mu
        for indices in ((first, second, second), (second, first, second), (second, second, first)):
            cubic[indices] += math.sqrt(2) * mu

    quadratic = np.diag([-p.mu_h2] * 4 + [p.m_a2] * 2 + [p.m_b2] * 2)
    mass2 = quadratic + 0.5 * np.einsum("abcd,c,d->ab", quartic, vev, vev)
    masses = np.sqrt(np.clip(np.diag(mass2), 0.0, None))
    if np.max(np.abs(mass2 - np.diag(np.diag(mass2)))) > 1e-10:
        raise RuntimeError("B0 mass matrix is unexpectedly non-diagonal")
    return {"quartic": quartic, "cubic": cubic, "mass2": mass2, "masses": masses}


def high_energy_physical_matrix(channels, quartic) -> np.ndarray:
    out = np.zeros((len(channels), len(channels)))
    for i, (a, b) in enumerate(channels):
        ni = math.sqrt(2) if a == b else 1.0
        for j, (c, d) in enumerate(channels):
            nf = math.sqrt(2) if c == d else 1.0
            out[j, i] = -quartic[a, b, c, d] / (16 * math.pi * ni * nf)
    return 0.5 * (out + out.T)


def scan(
    points: int,
    upper: float,
    c_s: float,
    p: vacuum.Parameters | None = None,
) -> dict[str, object]:
    p = p or benchmark()
    data = tensors(p)
    masses, cubic, quartic = data["masses"], data["cubic"], data["quartic"]
    all_channels = list(combinations_with_replacement(PHYSICAL, 2))
    thresholds = sorted(set(float(masses[i] + masses[j]) for i, j in all_channels))
    lower = thresholds[0] * (1 + 1e-5)
    grid = list(np.geomspace(lower, upper, points))
    for threshold in thresholds:
        for factor in (1.00001, 1.001, 1.01, 1.05, 1.20):
            energy = threshold * factor
            if lower <= energy <= upper:
                grid.append(float(energy))
    grid = sorted(set(grid))

    maximum = {"max_abs_eigenvalue": -1.0}
    records = []
    skipped_s = 0
    skipped_tu_all = 0
    for sqrt_s in grid:
        s = sqrt_s**2
        channels = [pair for pair in all_channels if masses[pair[0]] + masses[pair[1]] <= sqrt_s]
        if engine.near_s_channel_pole(s, channels, masses, cubic, c_s):
            skipped_s += 1
            continue
        bad: set[int] = set()
        for i, incoming in enumerate(channels):
            for j, outgoing in enumerate(channels):
                if engine.has_tu_pole(s, incoming, outgoing, masses, cubic):
                    bad.update((i, j))
        retained = [pair for i, pair in enumerate(channels) if i not in bad]
        if not retained:
            skipped_tu_all += 1
            continue
        partial = engine.partial_wave_matrix_analytic(sqrt_s, retained, masses, cubic, quartic)
        eig = np.linalg.eigvalsh(partial)
        row = {
            "sqrt_s_GeV": float(sqrt_s),
            "open_channels": len(channels),
            "retained_channels": len(retained),
            "max_abs_eigenvalue": float(np.max(np.abs(eig))),
            "min_eigenvalue": float(eig[0]),
            "max_eigenvalue": float(eig[-1]),
        }
        records.append(row)
        if row["max_abs_eigenvalue"] > maximum["max_abs_eigenvalue"]:
            maximum = row

    # Validate analytic angular integration against numerical quadrature away
    # from thresholds/poles at three energies.
    integration_checks = []
    for sqrt_s in (1000.0, 3000.0, 10000.0):
        channels = [pair for pair in all_channels if masses[pair[0]] + masses[pair[1]] <= sqrt_s]
        analytic = engine.partial_wave_matrix_analytic(sqrt_s, channels, masses, cubic, quartic)
        numeric = engine.partial_wave_matrix(sqrt_s, channels, masses, cubic, quartic, 192)
        integration_checks.append({
            "sqrt_s_GeV": sqrt_s,
            "maximum_absolute_matrix_difference": float(np.max(np.abs(analytic - numeric))),
        })

    he = high_energy_physical_matrix(all_channels, quartic)
    he_radius = float(np.max(np.abs(np.linalg.eigvalsh(he))))
    return {
        "schema_version": 1,
        "benchmark": "B0" if p == benchmark() else "custom",
        "external_states": [LABELS[i] for i in PHYSICAL],
        "masses_GeV": {LABELS[i]: float(masses[i]) for i in PHYSICAL},
        "channels": len(all_channels),
        "thresholds_GeV": thresholds,
        "scan_range_GeV": [lower, upper],
        "grid_points": len(grid),
        "evaluated_points": len(records),
        "s_channel_excision_Cs": c_s,
        "skipped_s_channel_points": skipped_s,
        "skipped_all_channels_due_tu_poles": skipped_tu_all,
        "tu_policy": "Remove every two-particle state participating in a matrix element with an on-shell t/u exchange.",
        "maximum_over_scan": maximum,
        "passes_abs_Re_a0_le_half": bool(maximum["max_abs_eigenvalue"] <= 0.5),
        "high_energy_physical_subspace_max_abs_a0": he_radius,
        "analytic_vs_quadrature": integration_checks,
        "sampled_scan": records[::max(1, len(records) // 35)],
        "scope_warning": "Physical scalars only. No external Goldstones or vectors, no gauge diagrams, no widths/resummation, and no UV gauge-origin states.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--points", type=int, default=420)
    parser.add_argument("--upper", type=float, default=20000.0)
    parser.add_argument("--c-s", type=float, default=0.25)
    args = parser.parse_args()
    payload = scan(args.points, args.upper, args.c_s)
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
