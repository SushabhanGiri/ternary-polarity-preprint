#!/usr/bin/env python3
"""Electroweak-plus-dark tree-level vacuum audit for TP-D v0.1.

Radial conventions:
  H^dagger H = h^2/2, |A|^2 = a^2/2, |B|^2 = b^2/2.
The independent A and B phases are minimized exactly.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, root


@dataclass(frozen=True)
class Parameters:
    mu_h2: float
    m_a2: float
    m_b2: float
    mu_a: float
    mu_b: float
    lambda_h: float
    lambda_a: float
    lambda_b: float
    lambda_ha: float
    lambda_hb: float
    lambda_ab: float


def potential(y: np.ndarray, p: Parameters) -> float:
    h, a, b = y
    return (
        -0.5 * p.mu_h2 * h * h
        + 0.25 * p.lambda_h * h**4
        + 0.5 * p.m_a2 * a * a
        - p.mu_a * a**3 / (3 * math.sqrt(2))
        + 0.25 * p.lambda_a * a**4
        + 0.5 * p.m_b2 * b * b
        - p.mu_b * b**3 / (3 * math.sqrt(2))
        + 0.25 * p.lambda_b * b**4
        + 0.25 * p.lambda_ha * h * h * a * a
        + 0.25 * p.lambda_hb * h * h * b * b
        + 0.25 * p.lambda_ab * a * a * b * b
    )


def gradient(y: np.ndarray, p: Parameters) -> np.ndarray:
    h, a, b = y
    return np.array(
        [
            h
            * (
                -p.mu_h2
                + p.lambda_h * h * h
                + 0.5 * p.lambda_ha * a * a
                + 0.5 * p.lambda_hb * b * b
            ),
            a
            * (
                p.m_a2
                - p.mu_a * a / math.sqrt(2)
                + p.lambda_a * a * a
                + 0.5 * p.lambda_ha * h * h
                + 0.5 * p.lambda_ab * b * b
            ),
            b
            * (
                p.m_b2
                - p.mu_b * b / math.sqrt(2)
                + p.lambda_b * b * b
                + 0.5 * p.lambda_hb * h * h
                + 0.5 * p.lambda_ab * a * a
            ),
        ]
    )


def hessian(y: np.ndarray, p: Parameters) -> np.ndarray:
    h, a, b = y
    return np.array(
        [
            [
                -p.mu_h2 + 3 * p.lambda_h * h * h + 0.5 * p.lambda_ha * a * a + 0.5 * p.lambda_hb * b * b,
                p.lambda_ha * h * a,
                p.lambda_hb * h * b,
            ],
            [
                p.lambda_ha * h * a,
                p.m_a2 - math.sqrt(2) * p.mu_a * a + 3 * p.lambda_a * a * a + 0.5 * p.lambda_ha * h * h + 0.5 * p.lambda_ab * b * b,
                p.lambda_ab * a * b,
            ],
            [
                p.lambda_hb * h * b,
                p.lambda_ab * a * b,
                p.m_b2 - math.sqrt(2) * p.mu_b * b + 3 * p.lambda_b * b * b + 0.5 * p.lambda_hb * h * h + 0.5 * p.lambda_ab * a * a,
            ],
        ]
    )


def copositive_bfb(p: Parameters) -> dict[str, float | bool]:
    lh, la, lb = p.lambda_h, p.lambda_a, p.lambda_b
    ha, hb, ab = p.lambda_ha / 2, p.lambda_hb / 2, p.lambda_ab / 2
    if min(lh, la, lb) < 0:
        return {"passes": False, "final_margin": float("-inf")}
    bha = ha + math.sqrt(lh * la)
    bhb = hb + math.sqrt(lh * lb)
    bab = ab + math.sqrt(la * lb)
    pairwise = min(bha, bhb, bab)
    if pairwise < 0:
        return {"passes": False, "pairwise_margin": pairwise, "final_margin": float("-inf")}
    final = (
        math.sqrt(lh * la * lb)
        + ha * math.sqrt(lb)
        + hb * math.sqrt(la)
        + ab * math.sqrt(lh)
        + math.sqrt(max(0.0, 2 * bha * bhb * bab))
    )
    return {
        "passes": final >= 0,
        "bar_HA": bha,
        "bar_HB": bhb,
        "bar_AB": bab,
        "pairwise_margin": pairwise,
        "final_margin": final,
    }


def sufficient_global_ew(p: Parameters) -> dict[str, bool]:
    return {
        "positive_dark_masses": p.m_a2 > 0 and p.m_b2 > 0,
        "nonnegative_portals": min(p.lambda_ha, p.lambda_hb, p.lambda_ab) >= 0,
        "A_single_field_nonnegative": p.mu_a**2 <= 9 * p.lambda_a * p.m_a2,
        "B_single_field_nonnegative": p.mu_b**2 <= 9 * p.lambda_b * p.m_b2,
        "SM_Higgs_minimum": p.mu_h2 > 0 and p.lambda_h > 0,
    }


def stationary_search(p: Parameters, upper: float, starts: int, seed: int) -> list[dict[str, object]]:
    rng = np.random.default_rng(seed)
    candidates: list[np.ndarray] = []
    for mask in range(8):
        active = [i for i in range(3) if mask & (1 << i)]
        if not active:
            candidates.append(np.zeros(3))
            continue

        def reduced(z: np.ndarray) -> np.ndarray:
            y = np.zeros(3)
            y[active] = z
            return gradient(y, p)[active]

        deterministic = np.full(len(active), 100.0)
        seeds = [deterministic]
        seeds.extend(rng.uniform(1e-6, upper, size=(starts, len(active))))
        for z0 in seeds:
            sol = root(reduced, z0)
            if not sol.success or np.max(np.abs(reduced(sol.x))) > 1e-5 * max(1.0, np.max(np.abs(sol.x))):
                continue
            if np.min(sol.x) < -1e-7 or np.max(sol.x) > 10 * upper:
                continue
            y = np.zeros(3)
            y[active] = np.maximum(sol.x, 0.0)
            if not any(np.linalg.norm(y - old) < 1e-5 * max(1.0, np.linalg.norm(y)) for old in candidates):
                candidates.append(y)

    rows: list[dict[str, object]] = []
    for y in candidates:
        eig = np.linalg.eigvalsh(hessian(y, p))
        rows.append(
            {
                "h_GeV": float(y[0]),
                "a_GeV": float(y[1]),
                "b_GeV": float(y[2]),
                "V_GeV4": float(potential(y, p)),
                "gradient_inf_norm": float(np.linalg.norm(gradient(y, p), ord=np.inf)),
                "radial_hessian_eigenvalues_GeV2": eig.tolist(),
                "radial_local_minimum": bool(np.min(eig) >= -1e-6),
            }
        )
    return sorted(rows, key=lambda row: row["V_GeV4"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--starts", type=int, default=250)
    parser.add_argument("--upper", type=float, default=2500.0)
    args = parser.parse_args()

    v, mh = 246.22, 125.25
    lambda_h = mh**2 / (2 * v**2)
    lambda_ha, lambda_hb = 0.020, 0.030
    target_ma, target_mb = 180.0, 400.0
    p = Parameters(
        mu_h2=lambda_h * v**2,
        m_a2=target_ma**2 - 0.5 * lambda_ha * v**2,
        m_b2=target_mb**2 - 0.5 * lambda_hb * v**2,
        mu_a=60.0,
        mu_b=90.0,
        lambda_h=lambda_h,
        lambda_a=0.20,
        lambda_b=0.25,
        lambda_ha=lambda_ha,
        lambda_hb=lambda_hb,
        lambda_ab=0.10,
    )
    sufficient = sufficient_global_ew(p)
    points = stationary_search(p, args.upper, args.starts, 20260915)
    result_de = differential_evolution(
        lambda y: potential(y, p),
        bounds=[(0, args.upper)] * 3,
        seed=20260915,
        tol=1e-11,
        polish=True,
    )
    ew = np.array([v, 0.0, 0.0])
    payload = {
        "schema_version": 1,
        "radial_convention": "HdagH=h^2/2, |A|^2=a^2/2, |B|^2=b^2/2; phases minimized",
        "parameters": asdict(p),
        "target_physical_masses_GeV": {"A": target_ma, "B": target_mb, "h": mh},
        "exact_copositivity_test": copositive_bfb(p),
        "analytic_sufficient_global_EW_conditions": sufficient,
        "analytic_sufficient_global_EW_pass": all(sufficient.values()),
        "electroweak_point": {
            "coordinates_GeV": ew.tolist(),
            "V_GeV4": potential(ew, p),
            "gradient_inf_norm": float(np.linalg.norm(gradient(ew, p), ord=np.inf)),
            "hessian_eigenvalues_GeV2": np.linalg.eigvalsh(hessian(ew, p)).tolist(),
        },
        "stationary_points": points,
        "differential_evolution_cross_check": {
            "success": bool(result_de.success),
            "coordinates_GeV": result_de.x.tolist(),
            "V_GeV4": float(result_de.fun),
            "difference_from_EW_V_GeV4": float(result_de.fun - potential(ew, p)),
            "bounds_GeV": [0.0, args.upper],
            "seed": 20260915,
        },
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
