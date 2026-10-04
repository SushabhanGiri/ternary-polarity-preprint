#!/usr/bin/env python3
"""Cross-artifact numerical and claim regression for the TP-D v0.3 freeze."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def close(a: float, b: float, rel: float = 1e-9) -> bool:
    return math.isclose(a, b, rel_tol=rel, abs_tol=0.0)


def run(root: Path) -> dict:
    audits = root / "audits"
    load = lambda name: json.loads((audits / name).read_text(encoding="utf-8"))
    dd = load("tpd_direct_detection_gate.json")
    pole = load("tpd_higgs_pole_diagnostic.json")
    thermal = load("tpd_pole_thermal_certification.json")
    ew = load("tpd_electroweak_gauge_unitarity.json")
    parent = load("tpd_parent_gauge_finite_energy.json")
    meta = load("tpd_cubic_metastability.json")
    cosmo = load("tpd_parent_extra_state_cosmology.json")
    ledger = load("TP_D_dependency_ledger_v0.2.json")

    checks: dict[str, bool] = {}
    checks["four_original_points_excluded"] = (
        dd["gate_summary"]["points_tested"] == 4
        and dd["gate_summary"]["points_excluded"] == 4
        and dd["gate_summary"]["minimum_excluding_R"] > 37.0
    )
    fixed = pole["fixed_candidate_parameter_vector"]
    checks["pole_vector_preserved"] = (
        fixed["mA"] == 62.0 and fixed["mB"] == 62.2
        and close(fixed["lambda_HA"], 0.0005539381702448959)
        and close(fixed["lambda_HB"], 0.0004917087212953458)
    )
    checks["precision_thermal_relic_near_target"] = (
        abs(thermal["nominal"]["Omega_total_h2"] / 0.12 - 1.0) < 0.011
        and thermal["numerical_relative_difference_total_110_vs_150"] < 1e-4
    )
    components = thermal["two_component_direct_detection"]["components"]
    checks["pole_direct_detection_survives"] = (
        components["A"]["R"] < 1.0 and components["B"]["R"] < 1.0
        and thermal["two_component_direct_detection"]["combined_nearly_degenerate_rate_ratio"] < 0.25
    )
    checks["electroweak_gauge_block_passes"] = (
        ew["scan"]["passes"]
        and ew["scan"]["maximum_portal_induced_singular_value"]["singular_value"] < 1e-3
    )
    summary = parent["combined_summary"]
    checks["sequential_interval_unscored"] = (
        summary["pole_contaminated_XS_interval_verdict"] == "not scored"
        and not summary["stable_state_genuine_unitarity_violation_found"]
    )
    for label in ("m", "E"):
        pole_row = parent["sectors"][label]["charged_XS_rhoS_blocks"]["physical_u_channel_pole"]
        checks[f"{label}_pole_matches_open_decay"] = (
            pole_row["decay_condition_X_to_S_Sbar"]
            and not pole_row["X_is_conventional_asymptotic_state"]
            and pole_row["verdict_treatment"] == "not scored as PASS or FAIL"
        )
    running = meta["point_matched_parent_running"]
    checks["cutoff_ordering"] = (
        running["first_sufficient_BFB_failure_GeV"]
        < running["high_energy_scalar_unitarity_boundary_GeV"]
        < running["four_pi_boundary_GeV"]
    )
    metastability = meta["one_loop_metastability_estimate"]
    checks["bounce_capped_at_unitarity"] = (
        close(
            metastability["bounce_scale_envelope_GeV"],
            running["high_energy_scalar_unitarity_boundary_GeV"],
        )
        and metastability["bounce_action_8pi2_over_3abs_lambda"] > 800.0
        and metastability["cosmological_lifetime_safe_in_this_approximation"]
    )
    checks["parent_states_prompt"] = all(
        sector["vector"]["lifetime_s"] < 1e-10
        and sector["radial"]["lifetime_s"] < 1e-10
        for sector in cosmo["extra_state_decays"].values()
    )
    checks["cmb_injection_safe"] = cosmo["late_time_annihilation"]["ratio_to_limit"] < 0.01
    node_ids = {node["id"] for node in ledger["nodes"]}
    checks["claim_ledger_complete_through_M21"] = all(
        f"M{i}" in node_ids for i in range(13, 22)
    )

    failed = [name for name, passed in checks.items() if not passed]
    return {
        "schema_version": 1,
        "checks": checks,
        "passed": not failed,
        "failed_checks": failed,
        "claim_regression": {
            "surviving_status": "conditionally viable conventional Z3xZ3 scalar EFT benchmark",
            "forbidden_claims": [
                "experimental confirmation",
                "demonstrated broad novelty",
                "three-generation explanation",
                "gravity or quantum-gravity explanation",
                "unification or fundamental-constant derivation",
                "absolute vacuum stability",
                "unconditional unstable-vector S-matrix pass",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument("--json", type=Path, default=root / "audits" / "tpd_final_regression.json")
    args = parser.parse_args()
    payload = run(root)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
