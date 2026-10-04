#!/usr/bin/env python3
"""Leading one-loop dimensionless running of the TP-G0 parent benchmark.

The calculation matches the standalone TP-D dimensionless system to the
parent at a common 1 TeV scale, then evolves:
  * SM gauge and third-family Yukawa couplings;
  * g_m and g_E on the protected zero-kinetic-mixing slice;
  * all 17 parent scalar quartics.

Scalar pieces are imported from the exact two-method derivation in
tpd_parent_scalar_rge.py.  New-Abelian gauge terms are evaluated directly.
This is a leading step-function threshold treatment, not precision matching.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import tpd_gauge_high_energy_unitarity as unitarity
import tpd_parent_scalar_rge as parent_scalar
import tpd_quartic_rge_running as low_running


LOOP = 16 * math.pi**2
SM_NAMES = ("g1", "g2", "g3", "yt", "yb", "ytau")
PARENT_NAMES = parent_scalar.COUPLINGS
NAMES = SM_NAMES + ("g_m", "g_E") + PARENT_NAMES


def build_scalar_betas():
    poly = parent_scalar.potential()
    return parent_scalar.project_hessian(parent_scalar.beta_potential(poly))


SCALAR_BETAS = build_scalar_betas()


def unpack(y: np.ndarray) -> dict[str, float]:
    return dict(zip(NAMES, map(float, y)))


def evaluate(expression, point: dict[str, float]) -> float:
    return sum(float(coefficient) * point[left] * point[right]
               for (left, right), coefficient in expression.items())


def sm_initial_at_1tev(low_override: dict[str, float] | None = None) -> dict[str, float]:
    low_initial = {
        "g1": 0.3583, "g2": 0.6478, "g3": 1.1666,
        "yt": 0.9369, "yb": 0.0164, "ytau": 0.0102,
        "lambda_H": 125.25**2 / (2 * 246.22**2),
        "lambda_A": 0.20, "lambda_B": 0.25,
        "lambda_HA": 0.020, "lambda_HB": 0.030, "lambda_AB": 0.10,
    }
    if low_override:
        unknown = set(low_override) - set(low_initial)
        if unknown:
            raise KeyError(f"unknown low-energy initial parameters: {sorted(unknown)}")
        low_initial.update(low_override)
    y0 = np.array([low_initial[name] for name in low_running.NAMES])
    solution = solve_ivp(
        low_running.beta,
        (math.log(173.0), math.log(1000.0)),
        y0,
        rtol=2e-12,
        atol=1e-14,
        method="DOP853",
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    return dict(zip(low_running.NAMES, map(float, solution.y[:, -1])))


def initial_point(
    low_override: dict[str, float] | None = None,
    parent_override: dict[str, float] | None = None,
) -> dict[str, float]:
    low = sm_initial_at_1tev(low_override)
    f = 1000.0
    point = {name: low[name] for name in SM_NAMES}
    point.update({
        "g_m": 0.30,
        "g_E": 0.30,
        "lambda_H": low["lambda_H"],
        "lambda_A": low["lambda_A"],
        "lambda_B": low["lambda_B"],
        "lambda_Phi_m": 0.20,
        "lambda_Phi_E": 0.20,
        "lambda_HA": low["lambda_HA"],
        "lambda_HB": low["lambda_HB"],
        "lambda_HPhi_m": 0.0,
        "lambda_HPhi_E": 0.0,
        "lambda_AB": low["lambda_AB"],
        "lambda_APhi_m": 0.0,
        "lambda_APhi_E": 0.0,
        "lambda_BPhi_m": 0.0,
        "lambda_BPhi_E": 0.0,
        "lambda_Phi_mPhi_E": 0.0,
        "kappa_m": math.sqrt(2) * 60.0 / (3 * f),
        "kappa_E": math.sqrt(2) * 90.0 / (3 * f),
    })
    if parent_override:
        unknown = set(parent_override) - set(point)
        if unknown:
            raise KeyError(f"unknown parent initial parameters: {sorted(unknown)}")
        point.update(parent_override)
    return point


def beta_numerator(y: np.ndarray) -> np.ndarray:
    p = unpack(y)
    g1, g2, g3 = p["g1"], p["g2"], p["g3"]
    yt, yb, ytau = p["yt"], p["yb"], p["ytau"]
    gm, ge = p["g_m"], p["g_E"]
    trace_y = 3 * yt**2 + 3 * yb**2 + ytau**2
    trace_y4 = 3 * yt**4 + 3 * yb**4 + ytau**4
    out = {
        "g1": 41 * g1**3 / 6,
        "g2": -19 * g2**3 / 6,
        "g3": -7 * g3**3,
        "yt": yt * (1.5 * (yt**2 - yb**2) + trace_y - 17 * g1**2 / 12 - 9 * g2**2 / 4 - 8 * g3**2),
        "yb": yb * (1.5 * (yb**2 - yt**2) + trace_y - 5 * g1**2 / 12 - 9 * g2**2 / 4 - 8 * g3**2),
        "ytau": ytau * (1.5 * ytau**2 + trace_y - 15 * g1**2 / 4 - 9 * g2**2 / 4),
        "g_m": (10 / 3) * gm**3,
        "g_E": (10 / 3) * ge**3,
    }
    for coupling in PARENT_NAMES:
        out[coupling] = evaluate(SCALAR_BETAS[coupling], p)

    # Standard-Model contributions.
    lh = p["lambda_H"]
    out["lambda_H"] += (
        4 * lh * trace_y - 2 * trace_y4
        - (9 * g2**2 + 3 * g1**2) * lh
        + 9 * g2**4 / 8 + 3 * g2**2 * g1**2 / 4 + 3 * g1**4 / 8
    )
    for portal in ("lambda_HA", "lambda_HB", "lambda_HPhi_m", "lambda_HPhi_E"):
        out[portal] += p[portal] * (
            2 * trace_y - 9 * g2**2 / 2 - 3 * g1**2 / 2
        )

    # New-Abelian wave-function and pure-gauge contributions.
    out["lambda_A"] += -12 * gm**2 * p["lambda_A"] + 6 * gm**4
    out["lambda_B"] += -12 * ge**2 * p["lambda_B"] + 6 * ge**4
    out["lambda_Phi_m"] += -108 * gm**2 * p["lambda_Phi_m"] + 486 * gm**4
    out["lambda_Phi_E"] += -108 * ge**2 * p["lambda_Phi_E"] + 486 * ge**4
    charged_portals = {
        "lambda_HA": (-6 * gm**2, 0.0),
        "lambda_HB": (-6 * ge**2, 0.0),
        "lambda_HPhi_m": (-54 * gm**2, 0.0),
        "lambda_HPhi_E": (-54 * ge**2, 0.0),
        "lambda_AB": (-6 * (gm**2 + ge**2), 0.0),
        "lambda_APhi_m": (-60 * gm**2, 108 * gm**4),
        "lambda_APhi_E": (-6 * gm**2 - 54 * ge**2, 0.0),
        "lambda_BPhi_m": (-54 * gm**2 - 6 * ge**2, 0.0),
        "lambda_BPhi_E": (-60 * ge**2, 108 * ge**4),
        "lambda_Phi_mPhi_E": (-54 * (gm**2 + ge**2), 0.0),
    }
    for coupling, (wave, pure) in charged_portals.items():
        out[coupling] += wave * p[coupling] + pure
    out["kappa_m"] += -36 * gm**2 * p["kappa_m"]
    out["kappa_E"] += -36 * ge**2 * p["kappa_E"]
    return np.array([out[name] for name in NAMES])


def beta(_t: float, y: np.ndarray) -> np.ndarray:
    return beta_numerator(y) / LOOP


def perturbativity_event(_t: float, y: np.ndarray) -> float:
    # Gauge, Yukawa, and scalar dimensionless couplings all count.
    return 4 * math.pi - float(np.max(np.abs(y)))


perturbativity_event.terminal = True
perturbativity_event.direction = -1


def sufficient_bfb(point: dict[str, float]) -> tuple[bool, dict[str, float]]:
    self_margins = {name: point[name] for name in parent_scalar.SELF.values()}
    portal_margins = {name: point[name] for name in parent_scalar.PORTALS.values()}

    def phase_margin(lambda_dark: float, lambda_phi: float, kappa: float) -> float:
        if lambda_phi <= 0:
            return -math.inf
        t = (abs(kappa) / (2 * lambda_phi)) ** (1 / 3)
        return lambda_dark - 1.5 * abs(kappa) * t

    phase = {
        "phase_m": phase_margin(point["lambda_A"], point["lambda_Phi_m"], point["kappa_m"]),
        "phase_E": phase_margin(point["lambda_B"], point["lambda_Phi_E"], point["kappa_E"]),
    }
    margins = {**self_margins, **portal_margins, **phase}
    # This certificate is sufficient because all modulus portals are required
    # nonnegative and the two independent phase-sensitive sectors pass their
    # exact two-field positivity test.
    return all(value >= 0 for value in margins.values()), margins


def first_crossing(scales: np.ndarray, values: np.ndarray, threshold: float, upward: bool = True):
    hits = np.where(values >= threshold)[0] if upward else np.where(values < threshold)[0]
    if len(hits) == 0:
        return None
    i = int(hits[0])
    if i == 0:
        return float(scales[0])
    x0, x1 = np.log(scales[i - 1]), np.log(scales[i])
    y0, y1 = values[i - 1], values[i]
    fraction = (threshold - y0) / (y1 - y0)
    return float(math.exp(x0 + fraction * (x1 - x0)))


def refined_crossing(grid_t: np.ndarray, sampled: np.ndarray, threshold: float,
                     function, upward: bool = True):
    hits = np.where(sampled >= threshold)[0] if upward else np.where(sampled < threshold)[0]
    if len(hits) == 0:
        return None
    i = int(hits[0])
    if i == 0:
        return float(math.exp(grid_t[0]))
    root = brentq(lambda t: function(t) - threshold, grid_t[i - 1], grid_t[i],
                  xtol=1e-12, rtol=1e-12)
    return float(math.exp(root))


def run(
    points: int,
    mu_max: float,
    low_override: dict[str, float] | None = None,
    parent_override: dict[str, float] | None = None,
) -> dict[str, object]:
    initial = initial_point(low_override, parent_override)
    y0 = np.array([initial[name] for name in NAMES])
    t0, t1 = math.log(1000.0), math.log(mu_max)
    solution = solve_ivp(
        beta,
        (t0, t1),
        y0,
        dense_output=True,
        events=perturbativity_event,
        max_step=(t1 - t0) / 2500,
        rtol=2e-10,
        atol=1e-11,
        method="DOP853",
    )
    end_t = float(solution.t_events[0][0]) if len(solution.t_events[0]) else float(solution.t[-1])
    grid_t = np.linspace(t0, end_t, points)
    trajectory = solution.sol(grid_t)
    scales = np.exp(grid_t)
    bfb_passes = []
    minimum_margins = []
    unity_radii = []
    for column in trajectory.T:
        point = unpack(column)
        passed, margins = sufficient_bfb(point)
        bfb_passes.append(passed)
        minimum_margins.append(min(margins.values()))
        unity_couplings = {name: point[name] for name in PARENT_NAMES}
        unity_radii.append(float(np.max(np.abs(np.linalg.eigvalsh(unitarity.matrix(unity_couplings))))))

    radii = np.asarray(unity_radii)
    margins = np.asarray(minimum_margins)
    final = unpack(trajectory[:, -1])
    def bfb_margin_at(t: float) -> float:
        _passed, local_margins = sufficient_bfb(unpack(solution.sol(t)))
        return min(local_margins.values())

    def unitarity_radius_at(t: float) -> float:
        point = unpack(solution.sol(t))
        couplings = {name: point[name] for name in PARENT_NAMES}
        return float(np.max(np.abs(np.linalg.eigvalsh(unitarity.matrix(couplings)))))

    first_negative = refined_crossing(grid_t, margins, 0.0, bfb_margin_at, upward=False)
    first_unitarity = refined_crossing(grid_t, radii, 8 * math.pi, unitarity_radius_at)
    at_unitarity_boundary = (
        unpack(solution.sol(math.log(first_unitarity)))
        if first_unitarity is not None else None
    )
    portal_values = {
        name: {
            "at_1_TeV": initial[name],
            "at_10_TeV": float(solution.sol(math.log(1e4))[NAMES.index(name)]) if end_t >= math.log(1e4) else None,
            "at_last_scale": final[name],
        }
        for name in parent_scalar.PORTALS.values()
    }
    return {
        "schema_version": 1,
        "matching_scale_GeV": 1000.0,
        "threshold_scheme": "Single step at 1 TeV; finite threshold corrections and the 0.63/0.90 TeV mass splitting are neglected.",
        "initial": initial,
        "last_integrated_scale_GeV": float(scales[-1]),
        "stopped_at_four_pi_boundary": bool(len(solution.t_events[0])),
        "solver_success": bool(solution.success),
        "solver_message": solution.message,
        "first_sufficient_BFB_certificate_failure_GeV": first_negative,
        "minimum_sufficient_BFB_margin": float(np.min(margins)),
        "high_energy_scalar_unitarity_boundary_GeV": first_unitarity,
        "couplings_at_scalar_unitarity_boundary": at_unitarity_boundary,
        "four_pi_boundary_GeV": float(scales[-1]) if len(solution.t_events[0]) else None,
        "maximum_scalar_scattering_eigenvalue": float(np.max(radii)),
        "final": final,
        "portal_generation": portal_values,
        "sample_points": points,
        "rtol": 2e-10,
        "atol": 1e-11,
        "scope_warning": "Leading one-loop dimensionless, zero-kinetic-mixing result. Dimensionful running, exact multi-field vacuum tracking, finite threshold corrections, two-loop terms, and full gauge-sector finite-energy unitarity remain open.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--points", type=int, default=1600)
    parser.add_argument("--mu-max", type=float, default=2.435e18)
    args = parser.parse_args()
    payload = run(args.points, args.mu_max)
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
