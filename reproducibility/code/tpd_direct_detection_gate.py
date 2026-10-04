#!/usr/bin/env python3
"""Deterministic direct-detection gate for the four TP-D relic-scan points.

The LZ WS2024+WS2022 power-constrained 90% C.L. SI curve is taken from the
vector path embedded in Fig. 5 of arXiv:2410.17036v3 / PRL 135, 011802
(2025).  The raw plot coordinates below are the vertices of that path.  Axis
calibration and interpolation are performed in log(m)-log(sigma) space.

This avoids both raster digitisation and repeated access to the blocked
HEPData record.  It is still labelled a figure-extracted curve rather than an
official table; the exclusion margins tested here are much larger than the
plot/interpolation precision.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable

import tpd_phenomenology_prefilter as prefilter


OMEGA_DM_H2 = 0.1200

# Major tick positions in the untransformed vector-graphic coordinate system.
X_LOG10_TICKS = ((83.679661, 1.0), (227.942056, 2.0))
Y_LOG10_TICKS = ((103.109647, -48.0), (170.221130, -47.0))

# Solid black "Power constrained upper limit" path from LZ Fig. 5.
LZ_POWER_CONSTRAINED_PATH = (
    (77.077692, 236.735536),
    (89.650433, 198.522592),
    (100.116345, 175.884834),
    (113.124099, 154.628884),
    (116.928334, 150.278750),
    (123.897079, 142.926170),
    (130.166390, 137.595123),
    (135.864213, 134.251490),
    (143.540921, 130.745794),
    (150.381720, 128.963092),
    (156.557205, 127.299805),
    (163.935374, 126.250655),
    (170.537342, 125.849760),
    (175.066600, 126.327422),
    (179.288789, 126.984207),
    (200.954164, 130.344899),
    (222.030991, 137.143050),
    (243.892548, 144.998881),
    (265.455567, 152.974127),
    (286.830932, 164.275947),
    (308.368362, 172.916507),
    (329.769317, 182.930346),
    (372.699171, 202.778900),
    (415.629026, 221.117701),
    (473.033739, 248.062945),
    (516.458315, 268.670640),
)


def linear_map(value: float, ticks: tuple[tuple[float, float], tuple[float, float]]) -> float:
    (x1, y1), (x2, y2) = ticks
    return y1 + (value - x1) * (y2 - y1) / (x2 - x1)


def lz_curve_anchors() -> list[tuple[float, float]]:
    """Return (mass_GeV, sigma_cm2) vertices from the embedded vector path."""
    return [
        (
            10.0 ** linear_map(x, X_LOG10_TICKS),
            10.0 ** linear_map(y, Y_LOG10_TICKS),
        )
        for x, y in LZ_POWER_CONSTRAINED_PATH
    ]


def loglog_interpolate(mass: float, anchors: Iterable[tuple[float, float]]) -> float:
    points = list(anchors)
    if not points[0][0] <= mass <= points[-1][0]:
        raise ValueError(f"mass {mass} GeV lies outside the LZ curve")
    log_mass = math.log10(mass)
    for (m1, s1), (m2, s2) in zip(points, points[1:]):
        if m1 <= mass <= m2:
            fraction = (log_mass - math.log10(m1)) / (math.log10(m2) - math.log10(m1))
            return 10.0 ** (
                math.log10(s1) + fraction * (math.log10(s2) - math.log10(s1))
            )
    raise RuntimeError("failed to bracket mass")


def audit_point(row: dict, anchors: list[tuple[float, float]]) -> dict:
    components = {}
    for label in ("A", "B"):
        mass = row["parameters"][f"m{label}"]
        omega = row["omega_h2"][label]
        portal = row["parameters"][f"lambda_H{label}"]
        raw_sigma = prefilter.sigma_si(mass, portal)
        stored_sigma = row["direct_detection"][f"sigma_{label}_cm2"]
        if not math.isclose(raw_sigma, stored_sigma, rel_tol=2.0e-14, abs_tol=0.0):
            raise RuntimeError(f"stored sigma mismatch for point {row['sample_index']} {label}")
        xi = omega / OMEGA_DM_H2
        effective_sigma = xi * raw_sigma
        limit = loglog_interpolate(mass, anchors)
        ratio = effective_sigma / limit
        components[label] = {
            "mass_GeV": mass,
            "omega_h2": omega,
            "xi_Omega_i_over_observed_DM": xi,
            "portal_lambda_Hi": portal,
            "sigma_SI_raw_cm2": raw_sigma,
            "sigma_SI_effective_cm2": effective_sigma,
            "LZ_90CL_limit_cm2": limit,
            "R_effective_over_limit": ratio,
            "verdict": "excluded" if ratio > 1.0 else "not_individually_excluded",
        }
    excluding = [label for label, data in components.items() if data["R_effective_over_limit"] > 1.0]
    return {
        "sample_index": row["sample_index"],
        "complete_parameter_vector": row["parameters"],
        "model_total_omega_h2": row["omega_h2"]["total"],
        "components": components,
        "excluding_components": excluding,
        "point_verdict": "excluded" if excluding else "not_excluded_by_componentwise_test",
    }


def build_payload(scan_path: Path) -> dict:
    scan = json.loads(scan_path.read_text(encoding="utf-8"))
    anchors = lz_curve_anchors()
    points = [audit_point(row, anchors) for row in scan["near_relic_points"]]
    excluded = sum(point["point_verdict"] == "excluded" for point in points)
    excluding_ratios = [
        component["R_effective_over_limit"]
        for point in points
        for component in point["components"].values()
        if component["R_effective_over_limit"] > 1.0
    ]
    return {
        "schema_version": 1,
        "status": "direct-detection gate complete for the four leading-order relic-compatible scan points",
        "observed_dark_matter_density": {
            "Omega_DM_h2": OMEGA_DM_H2,
            "usage": "xi_i = Omega_i h^2 / 0.1200; not Omega_i divided by the model point's own total",
        },
        "experimental_limit": {
            "experiment": "LUX-ZEPLIN (LZ)",
            "analysis": "combined WS2024+WS2022, 4.2 tonne-years, 280 live days",
            "observable": "spin-independent WIMP-nucleon cross section",
            "confidence_level": "90% C.L.",
            "statistical_curve": "minus-one-sigma power-constrained upper limit",
            "source": "J. Aalbers et al. (LZ Collaboration), Phys. Rev. Lett. 135, 011802 (2025)",
            "source_arxiv": "arXiv:2410.17036v3",
            "source_version_date": "2025-07-01",
            "hepdata_record": "155182 (blocked by access verification; not retried)",
            "curve_method": "programmatic log-log interpolation of the solid black vector path embedded in Figure 5",
            "curve_precision_note": "figure-extracted rather than official table; adequate here because excluding R values are >= O(10)",
            "minimum_crosscheck": {
                "mass_GeV": 40.0,
                "interpolated_sigma_cm2": loglog_interpolate(40.0, anchors),
                "paper_text_sigma_cm2": 2.2e-48,
            },
            "anchors_mass_sigma": [
                {"mass_GeV": mass, "sigma_cm2": sigma} for mass, sigma in anchors
            ],
        },
        "model_to_limit_mapping": {
            "elastic_scattering": True,
            "spin_independent": True,
            "momentum_independent_at_xenon_recoil_scale": True,
            "approximately_isospin_conserving_Higgs_exchange": True,
            "standard_halo_model_required": True,
            "local_fraction_assumption": "rho_i/rho_DM = Omega_i/Omega_DM",
            "nucleon_matrix_element": "f_N=0.30; hadronic uncertainty cannot bridge the smallest excluding factor",
            "amplitude_interference": "none in the tested minimal TP-D EFT: each component has one diagonal SM-Higgs mediator amplitude",
            "parent_model_caveat": "additional Higgs-radial mixing or kinetic-mixing amplitudes would define a modified TP-G benchmark and require a new likelihood; they are absent in the tested factorized point",
            "multicomponent_logic": "if one positive component rate alone exceeds the single-component limit after local-density rescaling, the combined point is conservatively excluded; a combined likelihood is unnecessary for that conclusion",
        },
        "points": points,
        "gate_summary": {
            "points_tested": len(points),
            "points_excluded": excluded,
            "minimum_excluding_R": min(excluding_ratios),
            "verdict": "all_four_points_robustly_excluded" if excluded == len(points) else "mixed",
            "scope": "rejects these four scan points, not the complete TP-D parameter space",
        },
        "analytic_interpretation": {
            "direct_detection_scaling": "sigma_SI_i is proportional to lambda_Hi^2/m_i^2",
            "portal_freezeout_scaling": "away from poles and thresholds, Higgs-portal annihilation is proportional to lambda_Hi^2, so lowering lambda_Hi raises Omega_i and does not generically lower xi_i*sigma_i",
            "semiannihilation_scaling": "sigma_v(XX->Xbar h) is proportional to mu_i^2*lambda_Hi^2; increasing a vacuum-allowed cubic can reduce the portal needed for freeze-out",
            "conversion_limitation": "BBbar<->AAbar conserves total dark-particle number and cannot alone cure overabundance/direct-detection tension",
            "physical_reason": "the four random-scan solutions obtain adequate depletion using Higgs portals large enough to generate xenon recoil rates tens to hundreds of times above LZ",
        },
        "next_targeted_directions": [
            {
                "priority": 1,
                "region": "Higgs resonance m_i approximately m_h/2",
                "reason": "resonant annihilation can reduce the portal without a corresponding zero-momentum direct-detection enhancement",
                "required_upgrade": "thermal averaging with the finite Higgs width; the existing threshold solver is not valid on the pole",
            },
            {
                "priority": 2,
                "region": "semi-annihilation-dominated, near-maximal vacuum-safe cubic with small Higgs portal",
                "reason": "mu_i supplies an independent depletion lever while sigma_SI remains controlled by lambda_Hi",
                "required_upgrade": "targeted scan with exact vacuum and finite-energy unitarity filters; reject rapidly nonperturbative self-couplings",
            },
            {
                "priority": 3,
                "region": "secluded TP-G annihilation into lighter dark vectors or radials",
                "reason": "dark-sector final states can decouple freeze-out from Higgs exchange",
                "required_upgrade": "repair the accidental rho_E relic and complete parent matching/kinetic-mixing constraints first",
            },
            {
                "priority": 4,
                "region": "scalar-mediator interference blind spot",
                "reason": "amplitude cancellation is possible only after adding quantified Higgs-radial mixing",
                "required_upgrade": "treat as a modified parent model with added parameters, tuning cost, and loop stability audit",
            },
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--scan",
        type=Path,
        default=root / "audits" / "tpd_relic_parameter_scan.json",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=root / "audits" / "tpd_direct_detection_gate.json",
    )
    args = parser.parse_args()
    payload = build_payload(args.scan)
    rendered = json.dumps(payload, indent=2)
    args.json.write_text(rendered + "\n", encoding="utf-8")
    print(json.dumps(payload["gate_summary"], indent=2))


if __name__ == "__main__":
    main()
