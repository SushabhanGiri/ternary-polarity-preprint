#!/usr/bin/env python3
"""One-loop Abelian gauge audit for the scalar-only TP-G0 parent.

This file treats the charge-conjugation-symmetric, zero-kinetic-mixing slice.
It computes the exact one-loop gauge coefficients, gauge contributions to all
17 scalar quartics, and the inhomogeneous sources of the two factorizing
portals lambda_APhi_m and lambda_BPhi_E.

The quartic conventions agree with tpd_parent_scalar_rge.py.  Results are
reported as (16*pi^2) beta.  Standard-Model gauge/Yukawa contributions to
H-containing couplings are outside this focused new-Abelian audit.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


SECTOR_CHARGES = {
    "H": (0, 0),
    "A": (1, 0),
    "B": (0, 1),
    "Phi_m": (3, 0),
    "Phi_E": (0, 3),
}
SELF = {
    "H": "lambda_H",
    "A": "lambda_A",
    "B": "lambda_B",
    "Phi_m": "lambda_Phi_m",
    "Phi_E": "lambda_Phi_E",
}
PORTALS = {
    ("H", "A"): "lambda_HA",
    ("H", "B"): "lambda_HB",
    ("H", "Phi_m"): "lambda_HPhi_m",
    ("H", "Phi_E"): "lambda_HPhi_E",
    ("A", "B"): "lambda_AB",
    ("A", "Phi_m"): "lambda_APhi_m",
    ("A", "Phi_E"): "lambda_APhi_E",
    ("B", "Phi_m"): "lambda_BPhi_m",
    ("B", "Phi_E"): "lambda_BPhi_E",
    ("Phi_m", "Phi_E"): "lambda_Phi_mPhi_E",
}


def polynomial_string(terms: list[tuple[Fraction, str]]) -> str:
    rendered = []
    for coefficient, monomial in terms:
        if coefficient == 0:
            continue
        rendered.append(f"{coefficient}*{monomial}")
    return " + ".join(rendered) if rendered else "0"


def gauge_terms() -> dict[str, str]:
    results: dict[str, str] = {}
    for sector, coupling in SELF.items():
        qm, qe = SECTOR_CHARGES[sector]
        terms = []
        if qm:
            terms.extend([
                (Fraction(-12 * qm * qm), f"g_m^2*{coupling}"),
                (Fraction(6 * qm**4), "g_m^4"),
            ])
        if qe:
            terms.extend([
                (Fraction(-12 * qe * qe), f"g_E^2*{coupling}"),
                (Fraction(6 * qe**4), "g_E^4"),
            ])
        results[coupling] = polynomial_string(terms)

    for (left, right), coupling in PORTALS.items():
        qlm, qle = SECTOR_CHARGES[left]
        qrm, qre = SECTOR_CHARGES[right]
        terms = []
        if qlm or qrm:
            terms.append((Fraction(-6 * (qlm**2 + qrm**2)), f"g_m^2*{coupling}"))
            if qlm and qrm:
                terms.append((Fraction(12 * qlm**2 * qrm**2), "g_m^4"))
        if qle or qre:
            terms.append((Fraction(-6 * (qle**2 + qre**2)), f"g_E^2*{coupling}"))
            if qle and qre:
                terms.append((Fraction(12 * qle**2 * qre**2), "g_E^4"))
        results[coupling] = polynomial_string(terms)

    # One Phi charge 3 plus three dark charges 1 gives sum q_i^2=12.
    results["kappa_m"] = "-36*g_m^2*kappa_m"
    results["kappa_E"] = "-36*g_E^2*kappa_E"
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    # A complex scalar contributes q^2/3 to an Abelian one-loop coefficient.
    b_m = Fraction(1**2 + 3**2, 3)
    b_e = Fraction(1**2 + 3**2, 3)
    gm = ge = 0.30
    km = math.sqrt(2) * 60.0 / 3000.0
    ke = math.sqrt(2) * 90.0 / 3000.0
    loop = 16 * math.pi**2
    source_m = (36 * km**2 + 108 * gm**4) / loop
    source_e = (36 * ke**2 + 108 * ge**4) / loop

    def landau(scale: float, coupling: float, b: Fraction) -> dict[str, object]:
        exponent = 8 * math.pi**2 / (float(b) * coupling**2)
        # The value is too large for a direct exponential; report log10.
        return {
            "reference_scale_GeV": scale,
            "coupling": coupling,
            "ln_Lambda_over_mu": exponent,
            "log10_Lambda_over_GeV": math.log10(scale) + exponent / math.log(10),
        }

    payload = {
        "schema_version": 1,
        "slice": "epsilon_Ym=epsilon_YE=epsilon_mE=0, protected by C_m x C_E",
        "one_loop_gauge_betas": {
            "b_m": str(b_m),
            "b_E": str(b_e),
            "convention": "(16*pi^2) beta_g = b*g^3",
            "derivation": "For each U(1), one complex q=1 scalar and one complex q=3 scalar give b=(1^2+3^2)/3=10/3.",
        },
        "one_loop_kinetic_mixing_sources": {
            "Y-m": 0,
            "Y-E": 0,
            "m-E": 0,
            "reason": "No active field carries both charges in any pair; charge conjugations provide all-orders protection on this slice.",
        },
        "new_abelian_gauge_terms_in_scalar_quartic_betas": gauge_terms(),
        "TP_G0_factorization_failure": {
            "beta_lambda_APhi_m_at_zero_per_log_mu": source_m,
            "beta_lambda_BPhi_E_at_zero_per_log_mu": source_e,
            "scalar_source_terms_16pi2": {
                "lambda_APhi_m": "36*kappa_m^2",
                "lambda_BPhi_E": "36*kappa_E^2",
            },
            "gauge_source_terms_16pi2": {
                "lambda_APhi_m": "108*g_m^4",
                "lambda_BPhi_E": "108*g_E^4",
            },
            "interpretation": "The factorized zero-portal benchmark is not an RG-invariant surface. Positive portals are generated immediately above the parent threshold.",
        },
        "one_loop_abelian_landau_estimates": {
            "m": landau(1000.0, gm, b_m),
            "E": landau(1000.0, ge, b_e),
            "warning": "Formal one-loop estimates far above the Planck scale have no physical EFT significance; they only show that g=0.30 is not the first perturbative obstruction.",
        },
        "scope_warning": "This is not the full TP-G parent RGE system. SM gauge/Yukawa terms, dimensionful parameters, threshold matching, and nonzero kinetic mixing remain open.",
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
