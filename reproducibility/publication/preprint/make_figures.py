#!/usr/bin/env python3
"""Create deterministic publication figures from the frozen audit records."""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle


ROOT = Path(__file__).resolve().parents[2]
AUDITS = ROOT / "audits"
OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name: str) -> None:
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def projection_kernel() -> None:
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    points = {
        "(0,0)": (1.2, 3.0), "(1,0) A": (3.2, 4.5), "(0,1) B": (3.2, 1.5),
        "projected charge 0": (8.2, 3.0), "projected charge 1": (8.2, 4.5),
        "kernel distinguishes A and B": (8.2, 1.3),
    }
    for label, (x, y) in points.items():
        circle = Circle((x, y), 0.56 if x < 5 else 0.78, facecolor="#F4F6F8",
                        edgecolor="#1F2933", linewidth=1.2)
        ax.add_patch(circle)
        ax.text(x, y, label, ha="center", va="center", fontsize=9)
    for src, dst in [
        ("(1,0) A", "projected charge 1"),
        ("(0,1) B", "projected charge 1"),
        ("(0,0)", "projected charge 0"),
    ]:
        x1, y1 = points[src]; x2, y2 = points[dst]
        ax.add_patch(FancyArrowPatch((x1 + 0.6, y1), (x2 - 0.85, y2),
                                    arrowstyle="->", mutation_scale=12,
                                    linewidth=1.1, color="#425A70"))
    ax.add_patch(FancyArrowPatch((3.2, 4.0), (7.4, 1.65),
                                arrowstyle="-|>", mutation_scale=12,
                                linewidth=1.0, linestyle="--", color="#8A3B3B"))
    ax.add_patch(FancyArrowPatch((3.2, 2.0), (7.4, 1.45),
                                arrowstyle="-|>", mutation_scale=12,
                                linewidth=1.0, linestyle="--", color="#8A3B3B"))
    ax.text(5.0, 5.55, r"$\pi(q_m,q_E)=q_m+q_E\ {\rm mod}\ 3$",
            ha="center", fontsize=13)
    ax.text(5.0, 0.35, r"$K={\rm diag}(\omega,\omega^2)$ acts differently on $A$ and $B$",
            ha="center", fontsize=11)
    save(fig, "figure_1_projection_kernel")


def direct_detection_tension() -> None:
    data = json.loads((AUDITS / "tpd_direct_detection_gate.json").read_text())
    xs, ys, labels = [], [], []
    for point in data["points"]:
        for label, row in point["components"].items():
            xs.append(row["mass_GeV"])
            ys.append(row["R_effective_over_limit"])
            labels.append(f"{point['sample_index']}{label}")
    thermal = json.loads((AUDITS / "tpd_pole_thermal_certification.json").read_text())
    for label, row in thermal["two_component_direct_detection"]["components"].items():
        xs.append(row["mass_GeV"]); ys.append(row["R"]); labels.append(f"P0{label}")
    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    colors = ["#9B2C2C" if y > 1 else "#276749" for y in ys]
    ax.scatter(xs, ys, c=colors, s=48, edgecolor="black", linewidth=0.5, zorder=3)
    for x, y, label in zip(xs, ys, labels):
        ax.annotate(label, (x, y), xytext=(4, 4), textcoords="offset points", fontsize=7)
    ax.axhline(1.0, color="black", linewidth=1.1, linestyle="--", label="exclusion threshold")
    ax.set_yscale("log")
    ax.set_xlabel("Dark component mass [GeV]")
    ax.set_ylabel(r"$R_i=\xi_i\sigma_i^{\rm SI}/\sigma_{\rm lim}$")
    ax.set_title("Abundance-weighted LZ comparison")
    ax.grid(True, which="both", color="#D9E2EC", linewidth=0.6)
    ax.legend(frameon=False)
    save(fig, "figure_2_direct_detection")


def rg_scales() -> None:
    data = json.loads((AUDITS / "tpd_cubic_metastability.json").read_text())
    row = data["point_matched_parent_running"]
    values = [
        row["first_sufficient_BFB_failure_GeV"],
        row["high_energy_scalar_unitarity_boundary_GeV"],
        row["four_pi_boundary_GeV"],
    ]
    labels = ["Higgs-direction BFB loss", "scalar partial-wave boundary", r"$4\pi$ coupling boundary"]
    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    logs = [math.log10(v) for v in values]
    bars = ax.barh(labels, logs, color=["#B7791F", "#2B6CB0", "#718096"])
    ax.set_xlim(0, 19)
    ax.set_xlabel(r"$\log_{10}(\mu/{\rm GeV})$")
    ax.set_title("Point-matched leading one-loop scales")
    ax.grid(axis="x", color="#D9E2EC", linewidth=0.6)
    for bar, value, logv in zip(bars, values, logs):
        ax.text(logv + 0.25, bar.get_y() + bar.get_height()/2,
                f"{value:.3e} GeV", va="center", fontsize=8)
    save(fig, "figure_3_rg_scales")


def sequential_intervals() -> None:
    data = json.loads((AUDITS / "tpd_parent_gauge_finite_energy.json").read_text())
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    ymap = {"m": 1.0, "E": 0.0}
    for sector, y in ymap.items():
        row = data["sectors"][sector]["charged_XS_rhoS_blocks"]["physical_u_channel_pole"]
        low, high = row["energy_interval_GeV"]
        ax.plot([0.9, low/1000], [y, y], color="#276749", linewidth=7, solid_capstyle="butt")
        ax.plot([low/1000, high/1000], [y, y], color="#B7791F", linewidth=7, solid_capstyle="butt")
        ax.plot([high/1000, 20], [y, y], color="#276749", linewidth=7, solid_capstyle="butt")
        ax.text(low/1000, y + 0.17, f"{low/1000:.3f}", ha="center", fontsize=8)
        ax.text(high/1000, y + 0.17, f"{high/1000:.3f}", ha="center", fontsize=8)
    ax.set_yticks([0, 1], ["E sector", "m sector"])
    ax.set_xlim(0.9, 20)
    ax.set_xlabel(r"$\sqrt{s}$ [TeV]")
    ax.set_title("Clean regions and physical sequential-kinematics intervals")
    ax.grid(axis="x", color="#D9E2EC", linewidth=0.6)
    ax.text(16.5, 1.45, "green: clean two-body audit", color="#276749", fontsize=9)
    ax.text(16.5, 1.18, "amber: unscored unstable-X interval", color="#8A5A00", fontsize=9)
    save(fig, "figure_4_sequential_intervals")


if __name__ == "__main__":
    plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False,
                         "axes.spines.right": False})
    projection_kernel()
    direct_detection_tension()
    rg_scales()
    sequential_intervals()
