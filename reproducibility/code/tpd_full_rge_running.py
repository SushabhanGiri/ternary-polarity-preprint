#!/usr/bin/env python3
"""One-loop TP-D running including scalar masses and Z3 cubic couplings.

The dimensionless system contains SM gauge couplings, third-family Yukawas,
and all TP-D quartics.  The dimensionful system contains mu_H^2, m_A^2,
m_B^2, mu_A, and mu_B.  The integration stops at the first 4*pi coupling
boundary, avoiding numerical claims after perturbation theory is already lost.

This is an MS-bar, no-threshold, one-loop audit.  It is not a precision pole-
mass evolution or a metastability calculation.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import tpd_ew_vacuum as vacuum
import tpd_quartic_rge_running as dimensionless


DIMENSIONFUL_NAMES = ("muH2", "mA2", "mB2", "muA", "muB")
NAMES = dimensionless.NAMES + DIMENSIONFUL_NAMES
LOOP = 16 * math.pi**2


def unpack(y: np.ndarray) -> dict[str, float]:
    return dict(zip(NAMES, map(float, y)))


def beta_numerator(y: np.ndarray) -> np.ndarray:
    p = unpack(y)
    dimless = np.array([p[name] for name in dimensionless.NAMES])
    out = dict(zip(dimensionless.NAMES, dimensionless.beta_numerator(dimless)))

    g1, g2 = p["g1"], p["g2"]
    yt, yb, ytau = p["yt"], p["yb"], p["ytau"]
    lh, la, lb = p["lambda_H"], p["lambda_A"], p["lambda_B"]
    ha, hb, ab = p["lambda_HA"], p["lambda_HB"], p["lambda_AB"]
    muh, ma, mb = p["muH2"], p["mA2"], p["mB2"]
    mua, mub = p["muA"], p["muB"]
    trace_y = 3 * yt**2 + 3 * yb**2 + ytau**2

    out.update({
        "muH2": muh * (12 * lh + 2 * trace_y - 4.5 * g2**2 - 1.5 * g1**2)
        - 2 * ha * ma - 2 * hb * mb,
        "mA2": 8 * la * ma + 2 * ab * mb - 4 * ha * muh + 4 * mua**2,
        "mB2": 8 * lb * mb + 2 * ab * ma - 4 * hb * muh + 4 * mub**2,
        "muA": 12 * la * mua,
        "muB": 12 * lb * mub,
    })
    return np.array([out[name] for name in NAMES])


def beta(_t: float, y: np.ndarray) -> np.ndarray:
    return beta_numerator(y) / LOOP


def perturbativity_event(_t: float, y: np.ndarray) -> float:
    return 4 * math.pi - float(np.max(np.abs(y[:len(dimensionless.NAMES)])))


perturbativity_event.terminal = True
perturbativity_event.direction = -1


def bfb_and_global_margins(p: dict[str, float]) -> dict[str, float | bool]:
    params = vacuum.Parameters(
        mu_h2=p["muH2"],
        m_a2=p["mA2"],
        m_b2=p["mB2"],
        mu_a=abs(p["muA"]),
        mu_b=abs(p["muB"]),
        lambda_h=p["lambda_H"],
        lambda_a=p["lambda_A"],
        lambda_b=p["lambda_B"],
        lambda_ha=p["lambda_HA"],
        lambda_hb=p["lambda_HB"],
        lambda_ab=p["lambda_AB"],
    )
    bfb_pass, bfb_margin = dimensionless.bfb(p)
    margins = {
        "muH2": p["muH2"],
        "mA2": p["mA2"],
        "mB2": p["mB2"],
        "portal_min": min(p["lambda_HA"], p["lambda_HB"], p["lambda_AB"]),
        "A_cubic": 9 * p["lambda_A"] * p["mA2"] - p["muA"]**2,
        "B_cubic": 9 * p["lambda_B"] * p["mB2"] - p["muB"]**2,
    }
    global_pass = bfb_pass and all(value >= 0 for value in margins.values())
    return {
        "BFB_pass": bfb_pass,
        "BFB_margin": bfb_margin,
        "sufficient_global_EW_pass": global_pass,
        **{f"global_margin_{key}": value for key, value in margins.items()},
        "analytic_condition_cross_check": all(vacuum.sufficient_global_ew(params).values()),
    }


def first_failure_details(scales: np.ndarray, diagnostics: list[dict[str, float | bool]]) -> dict[str, object] | None:
    for scale, row in zip(scales, diagnostics):
        if bool(row["sufficient_global_EW_pass"]):
            continue
        failed = {
            key.removeprefix("global_margin_"): float(value)
            for key, value in row.items()
            if key.startswith("global_margin_") and float(value) < 0
        }
        if not bool(row["BFB_pass"]):
            failed["BFB_margin"] = float(row["BFB_margin"])
        return {"scale_GeV": float(scale), "failed_margins": failed}
    return None


def first_downward_zero(scales: np.ndarray, values: np.ndarray) -> float | None:
    indices = np.where(values < 0)[0]
    if len(indices) == 0:
        return None
    i = int(indices[0])
    if i == 0:
        return float(scales[0])
    x0, x1 = np.log(scales[i - 1]), np.log(scales[i])
    y0, y1 = values[i - 1], values[i]
    fraction = -y0 / (y1 - y0)
    return float(math.exp(x0 + fraction * (x1 - x0)))


def first_crossing(scales: np.ndarray, values: np.ndarray, threshold: float) -> float | None:
    indices = np.where(values >= threshold)[0]
    if len(indices) == 0:
        return None
    i = int(indices[0])
    if i == 0:
        return float(scales[0])
    x0, x1 = np.log(scales[i - 1]), np.log(scales[i])
    y0, y1 = values[i - 1], values[i]
    fraction = (threshold - y0) / (y1 - y0)
    return float(math.exp(x0 + fraction * (x1 - x0)))


def run(
    portal_a: float,
    portal_b: float,
    points: int,
    mu_max: float,
    initial_override: dict[str, float] | None = None,
) -> dict[str, object]:
    mu0, v, mh = 173.0, 246.22, 125.25
    initial = {
        "g1": 0.3583, "g2": 0.6478, "g3": 1.1666,
        "yt": 0.9369, "yb": 0.0164, "ytau": 0.0102,
        "lambda_H": mh**2 / (2 * v**2),
        "lambda_A": 0.20, "lambda_B": 0.25,
        "lambda_HA": portal_a, "lambda_HB": portal_b, "lambda_AB": 0.10,
        "muH2": mh**2 / 2,
        "mA2": 180.0**2 - 0.5 * portal_a * v**2,
        "mB2": 400.0**2 - 0.5 * portal_b * v**2,
        "muA": 60.0, "muB": 90.0,
    }
    if initial_override:
        unknown = set(initial_override) - set(initial)
        if unknown:
            raise KeyError(f"unknown initial RGE parameters: {sorted(unknown)}")
        initial.update(initial_override)
    y0 = np.array([initial[name] for name in NAMES])
    t0, t1 = math.log(mu0), math.log(mu_max)
    sol = solve_ivp(
        beta,
        (t0, t1),
        y0,
        events=perturbativity_event,
        dense_output=True,
        max_step=(t1 - t0) / 2500,
        rtol=2e-10,
        atol=1e-10,
        method="DOP853",
    )
    end_t = float(sol.t_events[0][0]) if len(sol.t_events[0]) else float(sol.t[-1])
    grid_t = np.linspace(t0, end_t, points)
    trajectories = sol.sol(grid_t)
    scales = np.exp(grid_t)

    diagnostics = [bfb_and_global_margins(unpack(column)) for column in trajectories.T]
    radii = np.array([
        dimensionless.unitary_radius(unpack(column)) for column in trajectories.T
    ])
    margin_keys = [
        "BFB_margin", "global_margin_muH2", "global_margin_mA2",
        "global_margin_mB2", "global_margin_portal_min",
        "global_margin_A_cubic", "global_margin_B_cubic",
    ]
    zero_crossings = {
        key: first_downward_zero(scales, np.array([float(row[key]) for row in diagnostics]))
        for key in margin_keys
    }
    finite_crossings = {key: value for key, value in zero_crossings.items() if value is not None}
    first_global_scale = min(finite_crossings.values()) if finite_crossings else None
    first_global_conditions = (
        sorted(key for key, value in finite_crossings.items()
               if math.isclose(value, first_global_scale, rel_tol=1e-7))
        if first_global_scale is not None else []
    )
    final = unpack(trajectories[:, -1])
    minimum_margins = {
        key: float(min(float(row[key]) for row in diagnostics))
        for key in diagnostics[0]
        if key.endswith("margin") or key.startswith("global_margin_")
    }
    return {
        "schema_version": 1,
        "mu0_GeV": mu0,
        "requested_mu_max_GeV": mu_max,
        "last_integrated_scale_GeV": float(scales[-1]),
        "stopped_at_four_pi_boundary": bool(len(sol.t_events[0])),
        "solver_success": bool(sol.success),
        "solver_message": sol.message,
        "rtol": 2e-10,
        "atol": 1e-10,
        "initial": initial,
        "final": final,
        "first_BFB_failure_GeV": zero_crossings["BFB_margin"],
        "first_sufficient_global_EW_failure_GeV": first_global_scale,
        "first_sufficient_global_EW_failure_conditions": first_global_conditions,
        "sampled_first_failure_details": first_failure_details(scales, diagnostics),
        "unitarity_boundary_GeV": first_crossing(scales, radii, 8 * math.pi),
        "four_pi_boundary_GeV": float(scales[-1]) if len(sol.t_events[0]) else None,
        "minimum_margins": minimum_margins,
        "sample_points": points,
        "scope": "One-loop MS-bar running with no threshold matching or two-loop terms. Running sufficient tree-level inequalities are diagnostics, not an RG-improved tunnelling calculation.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--points", type=int, default=6000)
    parser.add_argument("--mu-max", type=float, default=2.435e18)
    parser.add_argument("--lambda-ha", type=float, default=0.020)
    parser.add_argument("--lambda-hb", type=float, default=0.030)
    args = parser.parse_args()
    payload = run(args.lambda_ha, args.lambda_hb, args.points, args.mu_max)
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
