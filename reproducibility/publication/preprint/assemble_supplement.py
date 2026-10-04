#!/usr/bin/env python3
"""Assemble the curated supplement and the frozen validation dossier."""

from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
core = (HERE / "supplement_core.md").read_text(encoding="utf-8")
checkpoint_names = [
    "TP_checkpoint_2_technical_report.md",
    "TP_checkpoint_3_finite_energy_unitarity.md",
    "TP_checkpoint_5_phase_II_distinctness_gate.md",
    "TP_checkpoint_6_EW_vacuum_RGE_unitarity.md",
    "TP_checkpoint_7_dimensionful_RGE_metastability.md",
    "TP_checkpoint_8_minimal_gauge_origin.md",
    "TP_checkpoint_9_parent_RGE.md",
    "TP_checkpoint_11_coupled_relic.md",
    "TP_checkpoint_12_direct_detection_gate.md",
    "TP_checkpoint_15_TPG_parent_gauge.md",
    "TP_checkpoint_16_pole_phenomenology_certification.md",
    "TP_checkpoint_17_cubic_metastability.md",
    "TP_checkpoint_18_parent_cosmology.md",
    "TP_checkpoint_19_adversarial_novelty.md",
    "TP_checkpoint_20_falsifiable_relation.md",
    "TP_checkpoint_21_hostile_referee.md",
    "TP_checkpoint_22_final_regression.md",
]
parts = [core, "\n# Frozen validation dossier\n"]
for index, name in enumerate(checkpoint_names, 1):
    text = (ROOT / "audits" / name).read_text(encoding="utf-8")
    text = text.replace("# ", f"## S{index} ", 1)
    parts.append(text)
(HERE / "supplementary_material.md").write_text(
    "\n\n\\newpage\n\n".join(parts) + "\n", encoding="utf-8"
)
