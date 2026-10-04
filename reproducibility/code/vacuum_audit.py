#!/usr/bin/env python3
"""Tree-level vacuum and boundedness audit for the TP-1 scalar sector.

Conventions
-----------
H^dagger H = h^2/2, |S| = s/sqrt(2), |chi| = x/sqrt(2), h,s,x >= 0.
After minimizing the only physical phase, the radial potential is

 V = -muH2 h^2/2 + lamH h^4/4
     -muS2 s^2/2 + lamS s^4/4
     +muc2 x^2/2 + lamc x^4/4
     +lamHS h^2 s^2/4 + lamHc h^2 x^2/4
     +lamSc s^2 x^2/4 - kappa s x^3/2.

The script enumerates all non-degenerate radial stationary branches for
kappa > 0.  Mixed branches reduce to a cubic equation for t=s/x.  It also
performs a direct numerical cross-check and a bounded-from-below scan.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
import json
import math
from typing import Dict, List, Tuple

import numpy as np
from scipy.optimize import differential_evolution, minimize


@dataclass(frozen=True)
class Parameters:
    muH2: float
    muS2: float
    muc2: float
    lamH: float
    lamS: float
    lamc: float
    lamHS: float
    lamHc: float
    lamSc: float
    kappa: float


def potential(y: np.ndarray, p: Parameters) -> float:
    h, s, x = y
    return (
        -0.5 * p.muH2 * h * h
        + 0.25 * p.lamH * h**4
        - 0.5 * p.muS2 * s * s
        + 0.25 * p.lamS * s**4
        + 0.5 * p.muc2 * x * x
        + 0.25 * p.lamc * x**4
        + 0.25 * p.lamHS * h * h * s * s
        + 0.25 * p.lamHc * h * h * x * x
        + 0.25 * p.lamSc * s * s * x * x
        - 0.5 * p.kappa * s * x**3
    )


def gradient(y: np.ndarray, p: Parameters) -> np.ndarray:
    h, s, x = y
    return np.array(
        [
            h
            * (
                -p.muH2
                + p.lamH * h * h
                + 0.5 * p.lamHS * s * s
                + 0.5 * p.lamHc * x * x
            ),
            -p.muS2 * s
            + p.lamS * s**3
            + 0.5 * p.lamHS * h * h * s
            + 0.5 * p.lamSc * s * x * x
            - 0.5 * p.kappa * x**3,
            x
            * (
                p.muc2
                + p.lamc * x * x
                + 0.5 * p.lamHc * h * h
                + 0.5 * p.lamSc * s * s
                - 1.5 * p.kappa * s * x
            ),
        ]
    )


def hessian(y: np.ndarray, p: Parameters) -> np.ndarray:
    h, s, x = y
    return np.array(
        [
            [
                -p.muH2
                + 3 * p.lamH * h * h
                + 0.5 * p.lamHS * s * s
                + 0.5 * p.lamHc * x * x,
                p.lamHS * h * s,
                p.lamHc * h * x,
            ],
            [
                p.lamHS * h * s,
                -p.muS2
                + 3 * p.lamS * s * s
                + 0.5 * p.lamHS * h * h
                + 0.5 * p.lamSc * x * x,
                p.lamSc * s * x - 1.5 * p.kappa * x * x,
            ],
            [
                p.lamHc * h * x,
                p.lamSc * s * x - 1.5 * p.kappa * x * x,
                p.muc2
                + 3 * p.lamc * x * x
                + 0.5 * p.lamHc * h * h
                + 0.5 * p.lamSc * s * s
                - 3 * p.kappa * s * x,
            ],
        ]
    )


def add_candidate(
    out: List[Dict[str, object]], name: str, y: Tuple[float, float, float], p: Parameters
) -> None:
    point = np.array(y, dtype=float)
    residual = float(np.linalg.norm(gradient(point, p), ord=np.inf))
    scale = max(1.0, abs(p.muH2), abs(p.muS2), abs(p.muc2)) * max(
        1.0, float(np.max(point))
    )
    eig = np.linalg.eigvalsh(hessian(point, p))
    out.append(
        {
            "branch": name,
            "h": float(point[0]),
            "s": float(point[1]),
            "x": float(point[2]),
            "V": float(potential(point, p)),
            "stationarity_relative_residual": residual / scale,
            "radial_hessian_eigenvalues": [float(v) for v in eig],
            "radial_local_minimum": bool(np.min(eig) >= -1e-7 * max(1.0, np.max(abs(eig)))),
        }
    )


def positive_real_roots(coeff: List[float]) -> List[float]:
    # Remove numerically vanishing leading coefficients, then select simple
    # positive real roots. Degenerate polynomial cases are reported by omission.
    scale = max(1.0, max(abs(c) for c in coeff))
    while len(coeff) > 1 and abs(coeff[0]) < 1e-13 * scale:
        coeff = coeff[1:]
    roots = np.roots(coeff)
    vals = sorted(float(r.real) for r in roots if abs(r.imag) < 1e-9 and r.real > 1e-12)
    dedup: List[float] = []
    for val in vals:
        if not dedup or abs(val - dedup[-1]) > 1e-7 * max(1.0, val):
            dedup.append(val)
    return dedup


def mixed_branch(
    p: Parameters,
    h_active: bool,
) -> List[Tuple[float, float, float]]:
    if h_active:
        # Minimize analytically over h before solving the (s,x) stationary
        # system. Bars denote the Schur-complement parameters.
        muS2 = p.muS2 - p.lamHS * p.muH2 / (2 * p.lamH)
        muc2 = p.muc2 + p.lamHc * p.muH2 / (2 * p.lamH)
        lamS = p.lamS - p.lamHS**2 / (4 * p.lamH)
        lamc = p.lamc - p.lamHc**2 / (4 * p.lamH)
        lamSc = p.lamSc - p.lamHS * p.lamHc / (2 * p.lamH)
    else:
        muS2, muc2 = p.muS2, p.muc2
        lamS, lamc, lamSc = p.lamS, p.lamc, p.lamSc

    # muS2*t*B(t) + muc2*A(t) = 0, with
    # A=lamS*t^3 + lamSc*t/2 - kappa/2 and
    # B=lamc + lamSc*t^2/2 - 3*kappa*t/2.
    coeff = [
        0.5 * muS2 * lamSc + muc2 * lamS,
        -1.5 * p.kappa * muS2,
        muS2 * lamc + 0.5 * muc2 * lamSc,
        -0.5 * p.kappa * muc2,
    ]

    points: List[Tuple[float, float, float]] = []
    for t in positive_real_roots(coeff):
        A = lamS * t**3 + 0.5 * lamSc * t - 0.5 * p.kappa
        B = lamc + 0.5 * lamSc * t**2 - 1.5 * p.kappa * t
        x2_candidates = []
        if abs(A) > 1e-12:
            x2_candidates.append(muS2 * t / A)
        if abs(B) > 1e-12:
            x2_candidates.append(-muc2 / B)
        x2_candidates = [z for z in x2_candidates if z > 0 and math.isfinite(z)]
        if not x2_candidates:
            continue
        x2 = float(np.mean(x2_candidates))
        if len(x2_candidates) == 2 and abs(x2_candidates[0] - x2_candidates[1]) > 1e-6 * max(x2_candidates):
            continue
        x, s = math.sqrt(x2), t * math.sqrt(x2)
        if h_active:
            h2 = (
                p.muH2 - 0.5 * p.lamHS * s * s - 0.5 * p.lamHc * x * x
            ) / p.lamH
            if h2 <= 0:
                continue
            h = math.sqrt(h2)
        else:
            h = 0.0
        points.append((h, s, x))
    return points


def enumerate_stationary_points(p: Parameters) -> List[Dict[str, object]]:
    if p.kappa <= 0:
        raise ValueError("This generic-branch enumerator assumes kappa > 0 after rephasing.")
    out: List[Dict[str, object]] = []
    add_candidate(out, "origin", (0.0, 0.0, 0.0), p)

    if p.muH2 > 0 and p.lamH > 0:
        add_candidate(out, "H", (math.sqrt(p.muH2 / p.lamH), 0.0, 0.0), p)
    if p.muS2 > 0 and p.lamS > 0:
        add_candidate(out, "S", (0.0, math.sqrt(p.muS2 / p.lamS), 0.0), p)

    matrix = np.array([[p.lamH, 0.5 * p.lamHS], [0.5 * p.lamHS, p.lamS]])
    if abs(np.linalg.det(matrix)) > 1e-14:
        h2, s2 = np.linalg.solve(matrix, np.array([p.muH2, p.muS2]))
        if h2 > 0 and s2 > 0:
            add_candidate(out, "HS-inert", (math.sqrt(h2), math.sqrt(s2), 0.0), p)

    for idx, point in enumerate(mixed_branch(p, h_active=False), start=1):
        add_candidate(out, f"Schi-{idx}", point, p)
    for idx, point in enumerate(mixed_branch(p, h_active=True), start=1):
        add_candidate(out, f"HSchi-{idx}", point, p)

    out.sort(key=lambda row: float(row["V"]))
    return out


def quartic_q(u: float, t: float, p: Parameters) -> float:
    # Four times V4/x^4 for x>0, with u=h/x and t=s/x.
    return (
        p.lamH * u**4
        + p.lamS * t**4
        + p.lamc
        + p.lamHS * u * u * t * t
        + p.lamHc * u * u
        + p.lamSc * t * t
        - 2 * p.kappa * t
    )


def reduced_bfb_function(t: float, p: Parameters) -> float:
    # Exact minimization over z=u^2 >= 0.
    P = p.lamS * t**4 + p.lamSc * t * t - 2 * p.kappa * t + p.lamc
    B = p.lamHS * t * t + p.lamHc
    return P if B >= 0 else P - B * B / (4 * p.lamH)


def bfb_numerical_check(p: Parameters) -> Dict[str, float | bool]:
    hs_boundary = p.lamHS + 2 * math.sqrt(p.lamH * p.lamS)
    result = differential_evolution(
        lambda z: reduced_bfb_function(math.exp(float(z[0])), p),
        bounds=[(-16.0, 16.0)],
        tol=1e-12,
        polish=True,
        seed=20260915,
    )
    tmin = math.exp(float(result.x[0]))
    qmin = float(result.fun)
    return {
        "lambdaH_positive": p.lamH > 0,
        "lambdaS_positive": p.lamS > 0,
        "lambdaChi_positive": p.lamc > 0,
        "HS_boundary_margin": hs_boundary,
        "reduced_min_t": tmin,
        "reduced_min_value": qmin,
        "passes_exact_radial_test_numerically": bool(
            p.lamH > 0
            and p.lamS > 0
            and p.lamc > 0
            and hs_boundary > 0
            and qmin > 0
        ),
    }


def direct_minimum_check(p: Parameters, upper: float) -> Dict[str, object]:
    result = differential_evolution(
        lambda y: potential(y, p),
        bounds=[(0, upper), (0, upper), (0, upper)],
        seed=20260915,
        tol=1e-11,
        polish=True,
    )
    local = minimize(
        lambda y: potential(y, p),
        result.x,
        method="L-BFGS-B",
        jac=lambda y: gradient(y, p),
        bounds=[(0, upper), (0, upper), (0, upper)],
        options={"ftol": 1e-14, "gtol": 1e-10, "maxiter": 5000},
    )
    return {
        "point": [float(v) for v in local.x],
        "V": float(local.fun),
        "gradient_inf_norm": float(np.linalg.norm(gradient(local.x, p), ord=np.inf)),
        "optimizer_success": bool(local.success),
        "search_upper_bound": upper,
    }


def benchmark() -> Parameters:
    v = 246.0
    f = 1000.0
    mchi = 500.0
    lamH, lamS, lamc = 0.13, 0.30, 0.25
    lamHS, lamHc, lamSc, kappa = 0.02, 0.05, 0.08, 0.05
    muH2 = lamH * v * v + 0.5 * lamHS * f * f
    muS2 = lamS * f * f + 0.5 * lamHS * v * v
    muc2 = mchi * mchi - 0.5 * lamHc * v * v - 0.5 * lamSc * f * f
    return Parameters(muH2, muS2, muc2, lamH, lamS, lamc, lamHS, lamHc, lamSc, kappa)


def main() -> None:
    p = benchmark()
    candidates = enumerate_stationary_points(p)
    report = {
        "conventions": "Natural units; all dimensionful inputs in GeV or GeV^2.",
        "parameters": asdict(p),
        "boundedness": bfb_numerical_check(p),
        "stationary_points": candidates,
        "enumerated_global_candidate": candidates[0],
        "direct_global_search": direct_minimum_check(p, upper=3000.0),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
