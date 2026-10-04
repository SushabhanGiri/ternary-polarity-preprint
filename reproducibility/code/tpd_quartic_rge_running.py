#!/usr/bin/env python3
"""One-loop TP-D dimensionless-coupling running and consistency boundaries.

Includes SM gauge and third-family Yukawa couplings plus all six TP-D
quartics. The scalar terms are independently derived in tpd_scalar_rge.py.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import tpd_ew_vacuum as vacuum
import tpd_high_energy_unitarity as unitarity
import tpd_scalar_rge as scalar


LOOP = 16 * math.pi**2
NAMES = (
    "g1", "g2", "g3", "yt", "yb", "ytau",
    "lambda_H", "lambda_A", "lambda_B", "lambda_HA", "lambda_HB", "lambda_AB",
)


def unpack(y: np.ndarray) -> dict[str, float]:
    return dict(zip(NAMES, map(float, y)))


def beta_numerator(y: np.ndarray) -> np.ndarray:
    p = unpack(y)
    g1, g2, g3 = p["g1"], p["g2"], p["g3"]
    yt, yb, ytau = p["yt"], p["yb"], p["ytau"]
    lh, la, lb = p["lambda_H"], p["lambda_A"], p["lambda_B"]
    ha, hb, ab = p["lambda_HA"], p["lambda_HB"], p["lambda_AB"]
    trace_y = 3 * yt**2 + 3 * yb**2 + ytau**2
    trace_y4 = 3 * yt**4 + 3 * yb**4 + ytau**4
    out = {
        "g1": 41 * g1**3 / 6,
        "g2": -19 * g2**3 / 6,
        "g3": -7 * g3**3,
        "yt": yt * (1.5 * (yt**2 - yb**2) + trace_y - 17 * g1**2 / 12 - 9 * g2**2 / 4 - 8 * g3**2),
        "yb": yb * (1.5 * (yb**2 - yt**2) + trace_y - 5 * g1**2 / 12 - 9 * g2**2 / 4 - 8 * g3**2),
        "ytau": ytau * (1.5 * ytau**2 + trace_y - 15 * g1**2 / 4 - 9 * g2**2 / 4),
        "lambda_H": 24 * lh**2 + ha**2 + hb**2 + 4 * lh * trace_y - 2 * trace_y4
        - (9 * g2**2 + 3 * g1**2) * lh
        + 9 * g2**4 / 8 + 3 * g2**2 * g1**2 / 4 + 3 * g1**4 / 8,
        "lambda_A": 20 * la**2 + 2 * ha**2 + ab**2,
        "lambda_B": 20 * lb**2 + 2 * hb**2 + ab**2,
        "lambda_HA": 12 * lh * ha + 8 * la * ha + 4 * ha**2 + 2 * hb * ab
        + 2 * trace_y * ha - (9 * g2**2 / 2 + 3 * g1**2 / 2) * ha,
        "lambda_HB": 12 * lh * hb + 8 * lb * hb + 4 * hb**2 + 2 * ha * ab
        + 2 * trace_y * hb - (9 * g2**2 / 2 + 3 * g1**2 / 2) * hb,
        "lambda_AB": 8 * la * ab + 8 * lb * ab + 4 * ab**2 + 4 * ha * hb,
    }
    return np.array([out[name] for name in NAMES])


def beta(t: float, y: np.ndarray) -> np.ndarray:
    del t
    return beta_numerator(y) / LOOP


def bfb(p: dict[str, float]) -> tuple[bool, float]:
    dummy = vacuum.Parameters(
        mu_h2=1, m_a2=1, m_b2=1, mu_a=0, mu_b=0,
        lambda_h=p["lambda_H"], lambda_a=p["lambda_A"], lambda_b=p["lambda_B"],
        lambda_ha=p["lambda_HA"], lambda_hb=p["lambda_HB"], lambda_ab=p["lambda_AB"],
    )
    result = vacuum.copositive_bfb(dummy)
    # Keep the diagnostic JSON standards-compliant even after a failed BFB
    # condition.  The copositivity helper uses -inf as an internal sentinel
    # when an earlier condition fails; the running audit instead reports the
    # first finite failed inequality.
    candidates = [p["lambda_H"], p["lambda_A"], p["lambda_B"]]
    for key in ("pairwise_margin", "final_margin"):
        value = float(result.get(key, math.nan))
        if math.isfinite(value):
            candidates.append(value)
    margin = min(candidates)
    return bool(result["passes"]), margin


def unitary_radius(p: dict[str, float]) -> float:
    couplings = {name: p[name] for name in scalar.NAMES}
    return float(np.max(np.abs(unitarity.analytic_spectrum(couplings))))


def first_crossing(scales: np.ndarray, values: np.ndarray, threshold: float) -> float | None:
    indices = np.where(values >= threshold)[0]
    if len(indices) == 0:
        return None
    index = int(indices[0])
    if index == 0:
        return float(scales[0])
    x0, x1 = np.log(scales[index - 1]), np.log(scales[index])
    y0, y1 = values[index - 1], values[index]
    fraction = (threshold - y0) / (y1 - y0)
    return float(math.exp(x0 + fraction * (x1 - x0)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--mu-max", type=float, default=2.435e18)
    parser.add_argument("--points", type=int, default=4000)
    parser.add_argument("--lambda-ha", type=float, default=0.020)
    parser.add_argument("--lambda-hb", type=float, default=0.030)
    parser.add_argument("--lambda-ab", type=float, default=0.10)
    parser.add_argument("--lambda-a", type=float, default=0.20)
    parser.add_argument("--lambda-b", type=float, default=0.25)
    args = parser.parse_args()
    scalar.build_potential()
    mu0 = 173.0
    initial = {
        "g1": 0.3583, "g2": 0.6478, "g3": 1.1666,
        "yt": 0.9369, "yb": 0.0164, "ytau": 0.0102,
        "lambda_H": 125.25**2 / (2 * 246.22**2),
        "lambda_A": args.lambda_a, "lambda_B": args.lambda_b,
        "lambda_HA": args.lambda_ha, "lambda_HB": args.lambda_hb, "lambda_AB": args.lambda_ab,
    }
    t_eval = np.linspace(math.log(mu0), math.log(args.mu_max), args.points)
    sol = solve_ivp(
        beta,
        (t_eval[0], t_eval[-1]),
        np.array([initial[name] for name in NAMES]),
        t_eval=t_eval,
        rtol=2e-10,
        atol=1e-12,
        method="DOP853",
    )
    scales = np.exp(sol.t)
    max_abs = np.max(np.abs(sol.y), axis=0)
    radii = []
    margins = []
    bfb_pass = []
    for column in sol.y.T:
        point = unpack(column)
        radii.append(unitary_radius(point))
        passed, margin = bfb(point)
        bfb_pass.append(passed)
        margins.append(margin)
    radii_array = np.array(radii)
    margins_array = np.array(margins)
    first_bfb_fail = next((float(scales[i]) for i, passed in enumerate(bfb_pass) if not passed), None)
    payload = {
        "schema_version": 1,
        "mu0_GeV": mu0,
        "requested_mu_max_GeV": args.mu_max,
        "last_integrated_scale_GeV": float(scales[-1]),
        "solver_success": bool(sol.success),
        "solver_message": sol.message,
        "rtol": 2e-10,
        "atol": 1e-12,
        "initial": initial,
        "final": unpack(sol.y[:, -1]),
        "first_BFB_failure_GeV": first_bfb_fail,
        "minimum_BFB_margin": float(np.min(margins_array)),
        "unitarity_boundary_GeV": first_crossing(scales, radii_array, 8 * math.pi),
        "four_pi_boundary_GeV": first_crossing(scales, max_abs, 4 * math.pi),
        "maximum_unitarity_eigenvalue_reached": float(np.max(radii_array)),
        "maximum_absolute_coupling_reached": float(np.max(max_abs)),
        "sample_points": len(scales),
        "scope": "One-loop dimensionless running. No threshold matching, two-loop terms, or dimensionful mass/cubic running.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
