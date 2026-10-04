#!/usr/bin/env python3
"""First phenomenological prefilter for TP-D/TP-G0.

This is not a relic-density calculation.  It derives:
  * exact tree-level Higgs-mediated nucleon cross sections;
  * exact kernel selection for the open B -> A+h channel;
  * the generic-Z3 decay coefficient for an off-diagonal Higgs portal;
  * kinematic accessibility of the new parent-state decays.

The output is designed to identify fatal or repairable benchmark issues before
undertaking coupled Boltzmann and collider scans.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


GEV2_TO_CM2 = 0.389379338e-27


def kallen(a: float, b: float, c: float) -> float:
    return a*a + b*b + c*c - 2*a*b - 2*a*c - 2*b*c


def sigma_si(mass: float, portal: float, f_n: float = 0.30,
             nucleon_mass: float = 0.938272, higgs_mass: float = 125.25) -> float:
    """Complex-scalar per-nucleon SI cross section in cm^2.

    Convention: V contains lambda_HS (H^dag H)|S|^2, hence the hSS vertex is
    lambda_HS*v.  The formula is
      lambda_HS^2 f_N^2 mu_N^2 m_N^2 /(4*pi*m_h^4*m_S^2).
    """
    reduced = mass * nucleon_mass / (mass + nucleon_mass)
    gev2 = portal**2 * f_n**2 * reduced**2 * nucleon_mass**2 / (
        4 * math.pi * higgs_mass**4 * mass**2
    )
    return gev2 * GEV2_TO_CM2


def generic_offdiagonal_width_coefficient(m_parent: float, m_daughter: float,
                                          m_higgs: float, vev: float) -> float:
    """Return Gamma/|eta|^2 for eta(HdagH) A^dag B+h.c., in GeV."""
    if m_parent <= m_daughter + m_higgs:
        return 0.0
    phase = math.sqrt(kallen(1.0, (m_daughter/m_parent)**2, (m_higgs/m_parent)**2))
    return vev**2 * phase / (16 * math.pi * m_parent)


def vector_to_complex_scalar_width(m_vector: float, m_scalar: float,
                                   gauge_coupling: float, charge: float = 1.0) -> float:
    if m_vector <= 2 * m_scalar:
        return 0.0
    phase = (1 - 4 * m_scalar**2 / m_vector**2)**1.5
    return gauge_coupling**2 * charge**2 * m_vector * phase / (48 * math.pi)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    v, mh = 246.22, 125.25
    ma, mb = 180.0, 400.0
    mrho, mx = 632.4555320336759, 900.0
    width_per_eta2 = generic_offdiagonal_width_coefficient(mb, ma, mh, v)
    hbar_gev_s = 6.582119569e-25

    payload = {
        "schema_version": 1,
        "benchmark": "B0 low spectrum plus TP-G0 parent spectrum",
        "exact_TP_D_selection": {
            "B_to_A_h_kinematically_open": mb > ma + mh,
            "initial_charge": [0, 1],
            "final_charge": [1, 0],
            "amplitude": 0,
            "reason": "Separate Z3_m and Z3_E charge conservation",
            "stable_species": ["A", "B"],
            "allowed_pair_conversion": "B Bdag <-> A Adag through lambda_AB",
            "allowed_self_semiannihilation": ["A A -> Adag h", "B B -> Bdag h"],
        },
        "generic_projected_Z3_comparator": {
            "operator": "eta_HAB (HdagH) Adag B + h.c.",
            "B_to_A_h_width_GeV": "|eta_HAB|^2 * coefficient",
            "width_coefficient_GeV": width_per_eta2,
            "proper_decay_length_m": "hbar*c/(coefficient*|eta_HAB|^2)",
            "example_widths_and_ctau": {
                str(eta): {
                    "width_GeV": width_per_eta2 * eta**2,
                    "lifetime_s": hbar_gev_s / (width_per_eta2 * eta**2),
                    "ctau_m": 299792458.0 * hbar_gev_s / (width_per_eta2 * eta**2),
                }
                for eta in (1e-2, 1e-5, 1e-7, 1e-9)
            },
        },
        "spin_independent_direct_detection": {
            "formula": "sigma_i=lambda_Hi^2*f_N^2*mu_Ni^2*m_N^2/(4*pi*m_h^4*m_i^2)",
            "f_N": 0.30,
            "A_sigma_cm2": sigma_si(ma, 0.020),
            "B_sigma_cm2": sigma_si(mb, 0.030),
            "multicomponent_rescaling": "Compare xi_i*sigma_i with the experimental single-component limit, where xi_i=Omega_i/Omega_DM.",
            "status": "No exclusion verdict is assigned until the coupled relic fractions and the experiment likelihood/limit at each mass are evaluated.",
        },
        "parent_tree_decay_prefilter": {
            "rho_m_to_3A": {
                "open": mrho > 3 * ma,
                "threshold_GeV": 3 * ma,
            },
            "rho_E_to_3B": {
                "open": mrho > 3 * mb,
                "threshold_GeV": 3 * mb,
            },
            "rho_E_to_B_Bdag_via_modulus_portal": {
                "open": mrho > 2 * mb,
                "threshold_GeV": 2 * mb,
                "matching_portal": 0.0,
            },
            "rho_E_to_X_E_X_E": {
                "open": mrho > 2 * mx,
                "threshold_GeV": 2 * mx,
            },
            "X_m_to_A_Adag_width_GeV": vector_to_complex_scalar_width(mx, ma, 0.30),
            "X_E_to_B_Bdag_width_GeV": vector_to_complex_scalar_width(mx, mb, 0.30),
            "rho_E_tree_status": "No open two- or three-body decay in the frozen factorized TP-G0 benchmark. It is an unintended additional stable/long-lived state unless an allowed portal, different hierarchy, or loop-induced decay is quantified.",
        },
        "scope_warning": "No annihilation, semi-annihilation, coupled Boltzmann, collider production, or indirect-detection calculation is included.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
