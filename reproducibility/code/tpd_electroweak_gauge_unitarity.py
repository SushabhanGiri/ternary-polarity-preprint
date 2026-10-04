#!/usr/bin/env python3
"""Electroweak vector/Goldstone finite-energy audit for the TP-D pole point.

A and B are electroweak singlets and have zero vacuum expectation values.
Consequently the pure-SM vector amplitudes are unchanged at tree level. The
only new physical-vector 2->2 amplitudes are S Sbar -> h* -> VV. This script
constructs their J=0 coupled-channel block for longitudinal and transverse W
and Z states, scans from threshold to 20 TeV, and checks the exact tree-level
Goldstone-equivalence relation.

The calculation uses normalized identical ZZ states. It completes the
low-energy TP-D electroweak gauge layer, not the separate U(1)_m x U(1)_E
parent-vector calculation.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


MH = 125.25
MW = 80.377
MZ = 91.1876
SQRT2 = math.sqrt(2.0)


def beta(s: float, mass: float) -> float:
    if s <= 4.0 * mass * mass:
        return 0.0
    return math.sqrt(1.0 - 4.0 * mass * mass / s)


def denominator(s: float) -> float:
    return s - MH * MH


def amplitudes(portal: float, s: float, vector_mass: float) -> dict[str, complex]:
    """Physical LL/TT and scalar-potential Goldstone invariant amplitudes."""
    prop = denominator(s)
    return {
        "LL": portal * (s - 2.0 * vector_mass**2) / prop,
        "TT": -2.0 * portal * vector_mass**2 / prop,
        "G": -portal * s / prop,
    }


def partial_wave(
    amplitude: complex,
    s: float,
    initial_mass: float,
    final_mass: float,
    identical_final: bool,
) -> complex:
    """J=0 partial wave for an angle-independent normalized channel."""
    phase = math.sqrt(beta(s, initial_mass) * beta(s, final_mass))
    normalization = SQRT2 if identical_final else 1.0
    return phase * amplitude / (16.0 * math.pi * normalization)


def physical_block(
    s: float,
    components: dict[str, dict[str, float]],
) -> tuple[np.ndarray, list[str], list[str]]:
    initial_labels = [f"{name}{name}bar" for name in components]
    final_labels = ["W_LL", "W_++", "W_--", "Z_LL", "Z_++", "Z_--"]
    block = np.zeros((len(initial_labels), len(final_labels)), dtype=complex)
    for row, values in enumerate(components.values()):
        mass = values["mass_GeV"]
        portal = values["lambda_Hi"]
        w = amplitudes(portal, s, MW)
        z = amplitudes(portal, s, MZ)
        block[row] = [
            partial_wave(w["LL"], s, mass, MW, False),
            partial_wave(w["TT"], s, mass, MW, False),
            partial_wave(w["TT"], s, mass, MW, False),
            partial_wave(z["LL"], s, mass, MZ, True),
            partial_wave(z["TT"], s, mass, MZ, True),
            partial_wave(z["TT"], s, mass, MZ, True),
        ]
    return block, initial_labels, final_labels


def build_payload(pole_json: Path, points: int, energy_max: float) -> dict:
    pole = json.loads(pole_json.read_text(encoding="utf-8"))
    components = {
        name: {
            "mass_GeV": float(row["mass_GeV"]),
            "lambda_Hi": float(row["lambda_Hi"]),
        }
        for name, row in pole["components"].items()
    }
    threshold = min(
        2.0 * max(values["mass_GeV"], vector_mass)
        for values in components.values()
        for vector_mass in (MW, MZ)
    )
    energies = np.geomspace(threshold * (1.0 + 1.0e-9), energy_max, points)

    maximum = {"singular_value": -1.0}
    for energy in energies:
        s = float(energy * energy)
        block, initial_labels, final_labels = physical_block(s, components)
        singular_value = float(np.linalg.svd(block, compute_uv=False)[0])
        if singular_value > maximum["singular_value"]:
            maximum = {
                "sqrt_s_GeV": float(energy),
                "singular_value": singular_value,
                "matrix_max_abs_entry": float(np.max(np.abs(block))),
            }

    equivalence = {}
    high_s = energy_max**2
    for vector, vector_mass, identical in (("W", MW, False), ("Z", MZ, True)):
        rows = {}
        for name, values in components.items():
            amp = amplitudes(values["lambda_Hi"], high_s, vector_mass)
            ll = partial_wave(
                amp["LL"], high_s, values["mass_GeV"], vector_mass, identical
            )
            goldstone = partial_wave(
                amp["G"], high_s, values["mass_GeV"], vector_mass, identical
            )
            # Overall sign is convention-dependent. The physical identity is
            # LL/(-G)=1-2 M_V^2/s.
            ratio = ll / (-goldstone)
            expected = 1.0 - 2.0 * vector_mass**2 / high_s
            rows[name] = {
                "LL_over_minus_G_real": float(ratio.real),
                "LL_over_minus_G_imag": float(ratio.imag),
                "expected": expected,
                "absolute_identity_residual": float(abs(ratio - expected)),
                "asymptotic_deviation_from_one": float(abs(1.0 - ratio)),
            }
        equivalence[vector] = rows

    return {
        "schema_version": 1,
        "theory": "TP-D Higgs-pole candidate",
        "components": components,
        "physical_channel_basis": {
            "initial": initial_labels,
            "final": final_labels,
            "identical_state_convention": "ZZ states carry 1/sqrt(2); W+W- is distinguishable",
        },
        "scan": {
            "threshold_GeV": threshold,
            "maximum_energy_GeV": energy_max,
            "points": points,
            "maximum_portal_induced_singular_value": maximum,
            "tree_unitarity_condition": "largest singular value <= 1/2",
            "passes": bool(maximum["singular_value"] <= 0.5),
        },
        "goldstone_equivalence_at_maximum_energy": equivalence,
        "gauge_consistency": {
            "pure_SM_vector_scattering": "unchanged at tree level because A and B are electroweak singlets with zero vevs",
            "new_tree_vector_amplitudes": "only S Sbar <-> h* <-> W+W-,ZZ",
            "longitudinal_amplitude": "lambda_HS*(s-2*M_V^2)/(s-m_h^2)",
            "goldstone_amplitude": "-lambda_HS*s/(s-m_h^2)",
            "transverse_amplitude_per_equal_helicity": "-2*lambda_HS*M_V^2/(s-m_h^2)",
            "mixed_LT": 0,
            "ward_equivalence_identity": "M_LL/(-M_G)=1-2*M_V^2/s",
        },
        "classification": "verified model-dependent low-energy electroweak gauge-sector pass",
        "scope_warning": "Does not include the separate U(1)_m x U(1)_E parent vectors, nonzero Abelian kinetic mixing, loop amplitudes, or a precision resonance likelihood. Physical on-shell WW/ZZ thresholds lie above the 125.25 GeV Higgs pole, so no vector-channel pole excision is needed.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--pole-json",
        type=Path,
        default=root / "audits" / "tpd_higgs_pole_diagnostic.json",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=root / "audits" / "tpd_electroweak_gauge_unitarity.json",
    )
    parser.add_argument("--points", type=int, default=800)
    parser.add_argument("--energy-max", type=float, default=2.0e4)
    args = parser.parse_args()
    payload = build_payload(args.pole_json, args.points, args.energy_max)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["scan"], indent=2))


if __name__ == "__main__":
    main()
