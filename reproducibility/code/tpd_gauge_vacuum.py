#!/usr/bin/env python3
"""Vacuum and BFB audit for a minimal scalar-only TP-G0 benchmark.

The benchmark chooses f_m=f_E=1 TeV, vanishing modulus portals involving the
parent Higgs fields, and the low-energy B0 parameters.  Nonnegative H-A, H-B,
and A-B portals then allow the global proof to factor into the SM Higgs
direction and two (Phi, dark scalar) sectors.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial import Polynomial


def sector_audit(name: str, f: float, lambda_phi: float, mass2: float,
                 lambda_dark: float, kappa: float) -> dict[str, object]:
    # V4*4/a^4 = lambda_phi*t^4 + lambda_dark - 2*kappa*t.
    t_min = (kappa / (2 * lambda_phi)) ** (1 / 3)
    bfb_margin = lambda_dark - 1.5 * kappa * t_min

    # For an interior stationary point with x=a^2>0,
    # phi=2(m^2+lambda_dark*x)/(3*kappa*sqrt(x)).  Eliminating phi gives
    # 4 lambda_phi M(4 M^2-9 kappa^2 f^2 x)-27 kappa^4 x^3=0.
    x = Polynomial([0.0, 1.0])
    m = Polynomial([mass2, lambda_dark])
    polynomial = 4 * lambda_phi * m * (4 * m * m - 9 * kappa**2 * f**2 * x) - 27 * kappa**4 * x**3
    roots = polynomial.roots()
    stationary = []
    for root in roots:
        if abs(root.imag) > 1e-7 or root.real <= 0:
            continue
        x_value = float(root.real)
        a = math.sqrt(x_value)
        phi = 2 * (mass2 + lambda_dark * x_value) / (3 * kappa * a)
        delta_v = (
            lambda_phi * (phi**2 - f**2)**2 / 4
            + mass2 * a**2 / 2
            + lambda_dark * a**4 / 4
            - kappa * phi * a**3 / 2
        )
        stationary.append({"phi_GeV": phi, "dark_radial_GeV": a, "DeltaV_GeV4": delta_v})
    return {
        "sector": name,
        "f_GeV": f,
        "lambda_phi": lambda_phi,
        "mass2_GeV2": mass2,
        "lambda_dark": lambda_dark,
        "kappa": kappa,
        "quartic_BFB_margin": bfb_margin,
        "quartic_BFB_pass": bfb_margin >= 0,
        "stationary_polynomial_coefficients_ascending": polynomial.coef.tolist(),
        "all_stationary_polynomial_roots": [[float(root.real), float(root.imag)] for root in roots],
        "positive_interior_stationary_points": stationary,
        "global_sector_vacuum_certified": bfb_margin >= 0 and all(row["DeltaV_GeV4"] >= 0 for row in stationary),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    v, mh, f = 246.22, 125.25, 1000.0
    lambda_h = mh**2 / (2 * v**2)
    lambda_phi = 0.20
    g_m = g_e = 0.30
    lambda_ha, lambda_hb, lambda_ab = 0.020, 0.030, 0.10
    mass_a2 = 180.0**2 - 0.5 * lambda_ha * v**2
    mass_b2 = 400.0**2 - 0.5 * lambda_hb * v**2
    mu_a, mu_b = 60.0, 90.0
    kappa_a = math.sqrt(2) * mu_a / (3 * f)
    kappa_b = math.sqrt(2) * mu_b / (3 * f)
    sector_m = sector_audit("m", f, lambda_phi, mass_a2, 0.20, kappa_a)
    sector_e = sector_audit("E", f, lambda_phi, mass_b2, 0.25, kappa_b)
    payload = {
        "schema_version": 1,
        "benchmark": "TP-G0",
        "parameters": {
            "f_m_GeV": f, "f_E_GeV": f,
            "g_m": g_m, "g_E": g_e,
            "lambda_Phi_m": lambda_phi, "lambda_Phi_E": lambda_phi,
            "lambda_H": lambda_h,
            "lambda_A": 0.20, "lambda_B": 0.25,
            "lambda_HA": lambda_ha, "lambda_HB": lambda_hb, "lambda_AB": lambda_ab,
            "kappa_m": kappa_a, "kappa_E": kappa_b,
            "all_other_modulus_portals": 0.0,
            "all_abelian_kinetic_mixings": 0.0
        },
        "extra_symmetry_for_zero_kinetic_mixing": "independent C_m and C_E charge conjugations",
        "spectrum_GeV": {
            "rho_m": math.sqrt(2 * lambda_phi) * f,
            "rho_E": math.sqrt(2 * lambda_phi) * f,
            "X_m": 3 * g_m * f,
            "X_E": 3 * g_e * f,
            "A": 180.0,
            "B": 400.0,
            "h": mh
        },
        "matching": {
            "mu_A_GeV": 3 * kappa_a * f / math.sqrt(2),
            "mu_B_GeV": 3 * kappa_b * f / math.sqrt(2)
        },
        "sector_audits": [sector_m, sector_e],
        "global_tree_vacuum_certified": (
            lambda_h > 0 and min(lambda_ha, lambda_hb, lambda_ab) >= 0
            and sector_m["global_sector_vacuum_certified"]
            and sector_e["global_sector_vacuum_certified"]
        ),
        "proof_scope": "For this factorized benchmark only: all omitted modulus portals vanish and the retained cross portals are nonnegative. Radiative stability of the chosen zero portals is not claimed.",
        "phenomenology_warning": "No collider, precision, relic-density, cosmic-string, or threshold-RGE viability is implied."
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
