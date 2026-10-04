#!/usr/bin/env python3
"""Finite-energy physical-scalar partial-wave audit for the TP-1 benchmark.

The calculation includes the two CP-even mass eigenstates and the two real
components of chi.  It includes every quartic contact term and all scalar
s-, t-, and u-channel exchanges among the eight real scalar components.

Gauge bosons, longitudinal-vector external states, and would-be Goldstone
external states are deliberately excluded from this first finite-energy layer.
The output must therefore not be described as the full model unitarity bound.
"""

from __future__ import annotations

import json
import math
from typing import Dict, List, Tuple

import numpy as np
from numpy.polynomial.legendre import leggauss

import scalar_rge_generator as rge
from vacuum_audit import Parameters, benchmark


def quartic_tensor(p: Parameters) -> np.ndarray:
    rge.potential.clear()
    rge.build_potential()
    values = {
        "lamH": p.lamH,
        "lamS": p.lamS,
        "lamc": p.lamc,
        "lamHS": p.lamHS,
        "lamHc": p.lamHc,
        "lamSc": p.lamSc,
        "kappa": p.kappa,
    }
    out = np.zeros((rge.N, rge.N, rge.N, rge.N), dtype=float)
    for a in range(rge.N):
        for b in range(rge.N):
            for c in range(rge.N):
                for d in range(rge.N):
                    out[a, b, c, d] = sum(
                        float(coefficient) * values[name]
                        for name, coefficient in rge.tensor((a, b, c, d)).items()
                    )
    return out


def spectrum_and_couplings(p: Parameters) -> Dict[str, np.ndarray]:
    lam = quartic_tensor(p)
    vev = np.zeros(rge.N)
    vev[0] = 246.0
    vev[4] = 1000.0
    quadratic = np.diag(
        [-p.muH2] * 4 + [-p.muS2] * 2 + [p.muc2] * 2
    )
    mass2 = quadratic + 0.5 * np.einsum("abcd,c,d->ab", lam, vev, vev)
    evals, rotation = np.linalg.eigh(mass2)

    # phi_a = rotation[a,i] eta_i.  All eigenstates are retained internally,
    # because even an unphysical Goldstone can occur as an exchange field in
    # the scalar-potential calculation.  External states are the four positive
    # massive modes only.
    cubic_mass = np.einsum("abcd,ai,bj,ck,d->ijk", lam, rotation, rotation, rotation, vev)
    quartic_mass = np.einsum(
        "abcd,ai,bj,ck,dl->ijkl", lam, rotation, rotation, rotation, rotation
    )
    physical = [i for i, value in enumerate(evals) if value > 1e-5]
    if len(physical) != 4:
        raise RuntimeError(f"Expected four positive massive scalar modes, found {physical} with {evals}")
    return {
        "mass2": evals,
        "masses": np.sqrt(np.clip(evals, 0.0, None)),
        "rotation": rotation,
        "cubic": cubic_mass,
        "quartic": quartic_mass,
        "physical": np.array(physical, dtype=int),
    }


def kallen(a: float, b: float, c: float) -> float:
    return a * a + b * b + c * c - 2 * a * b - 2 * a * c - 2 * b * c


def momentum(s: float, ma: float, mb: float) -> float:
    value = kallen(s, ma * ma, mb * mb)
    return math.sqrt(max(0.0, value)) / (2 * math.sqrt(s))


def energy(s: float, ma: float, mb: float) -> float:
    return (s + ma * ma - mb * mb) / (2 * math.sqrt(s))


def amplitude(
    costh: float,
    s: float,
    channel_in: Tuple[int, int],
    channel_out: Tuple[int, int],
    masses: np.ndarray,
    cubic: np.ndarray,
    quartic: np.ndarray,
) -> float:
    a, b = channel_in
    c, d = channel_out
    ma, mb, mc, md = masses[[a, b, c, d]]
    pin = momentum(s, ma, mb)
    pout = momentum(s, mc, md)
    ea, ec, ed = energy(s, ma, mb), energy(s, mc, md), energy(s, md, mc)
    t = ma * ma + mc * mc - 2 * ea * ec + 2 * pin * pout * costh
    u = ma * ma + md * md - 2 * ea * ed - 2 * pin * pout * costh
    value = -quartic[a, b, c, d]
    for e, me in enumerate(masses):
        me2 = me * me
        # A tiny imaginary width is not inserted.  The scan begins above every
        # two-particle threshold and separately rejects any denominator that
        # approaches a real pole.
        denominators = (s - me2, t - me2, u - me2)
        products = (
            cubic[a, b, e] * cubic[c, d, e],
            cubic[a, c, e] * cubic[b, d, e],
            cubic[a, d, e] * cubic[b, c, e],
        )
        for product_value, denominator in zip(products, denominators):
            if abs(product_value) <= 1e-14:
                continue
            if abs(denominator) < 1e-8 * max(1.0, s):
                raise FloatingPointError("Exchange pole encountered")
            value -= product_value / denominator
    return float(value)


def partial_wave_matrix(
    sqrt_s: float,
    channels: List[Tuple[int, int]],
    masses: np.ndarray,
    cubic: np.ndarray,
    quartic: np.ndarray,
    quadrature_order: int,
) -> np.ndarray:
    s = sqrt_s * sqrt_s
    nodes, weights = leggauss(quadrature_order)
    out = np.zeros((len(channels), len(channels)))
    for i, incoming in enumerate(channels):
        a, b = incoming
        pin = momentum(s, masses[a], masses[b])
        delta_in = 1 if a == b else 0
        for j, outgoing in enumerate(channels):
            c, d = outgoing
            pout = momentum(s, masses[c], masses[d])
            delta_out = 1 if c == d else 0
            integral = 0.0
            for node, weight in zip(nodes, weights):
                integral += weight * amplitude(
                    float(node), s, incoming, outgoing, masses, cubic, quartic
                )
            prefactor = math.sqrt(
                4 * pin * pout / (2**delta_in * 2**delta_out * s)
            ) / (32 * math.pi)
            out[j, i] = prefactor * integral
    # Numerical quadrature and basis ordering can leave roundoff asymmetry.
    return 0.5 * (out + out.T)


def propagator_integral(offset: float, span: float, mass2: float) -> float:
    """Return integral_{-1}^{1} dz /(offset + span*z - mass2)."""
    a = offset - mass2
    if abs(span) < 1e-14 * max(1.0, abs(a)):
        if abs(a) < 1e-14:
            raise FloatingPointError("Degenerate exchange pole")
        return 2.0 / a
    low, high = a - span, a + span
    if low <= 0 <= high:
        raise FloatingPointError("Angular exchange pole")
    return math.log(high / low) / span


def partial_wave_matrix_analytic(
    sqrt_s: float,
    channels: List[Tuple[int, int]],
    masses: np.ndarray,
    cubic: np.ndarray,
    quartic: np.ndarray,
) -> np.ndarray:
    """Analytic angular integration of all scalar exchange diagrams."""
    s = sqrt_s * sqrt_s
    out = np.zeros((len(channels), len(channels)))
    for i, incoming in enumerate(channels):
        a, b = incoming
        pin = momentum(s, masses[a], masses[b])
        delta_in = 1 if a == b else 0
        for j, outgoing in enumerate(channels):
            c, d = outgoing
            pout = momentum(s, masses[c], masses[d])
            delta_out = 1 if c == d else 0
            ma, mb, mc, md = masses[[a, b, c, d]]
            ea, ec, ed = energy(s, ma, mb), energy(s, mc, md), energy(s, md, mc)
            span = 2 * pin * pout
            t0 = ma * ma + mc * mc - 2 * ea * ec
            u0 = ma * ma + md * md - 2 * ea * ed
            integral = -2 * quartic[a, b, c, d]
            for e, me in enumerate(masses):
                me2 = me * me
                sprod = cubic[a, b, e] * cubic[c, d, e]
                tprod = cubic[a, c, e] * cubic[b, d, e]
                uprod = cubic[a, d, e] * cubic[b, c, e]
                if abs(sprod) > 1e-14:
                    if abs(s - me2) < 1e-12 * max(1.0, s):
                        raise FloatingPointError("s-channel exchange pole")
                    integral -= 2 * sprod / (s - me2)
                if abs(tprod) > 1e-14:
                    integral -= tprod * propagator_integral(t0, span, me2)
                if abs(uprod) > 1e-14:
                    # u = u0 - span*z has the same symmetric integral.
                    integral -= uprod * propagator_integral(u0, span, me2)
            prefactor = math.sqrt(
                4 * pin * pout / (2**delta_in * 2**delta_out * s)
            ) / (32 * math.pi)
            out[j, i] = prefactor * integral
    return 0.5 * (out + out.T)


def transfer_ranges(
    s: float,
    channel_in: Tuple[int, int],
    channel_out: Tuple[int, int],
    masses: np.ndarray,
) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    a, b = channel_in
    c, d = channel_out
    ma, mb, mc, md = masses[[a, b, c, d]]
    pin = momentum(s, ma, mb)
    pout = momentum(s, mc, md)
    ea, ec, ed = energy(s, ma, mb), energy(s, mc, md), energy(s, md, mc)
    t0 = ma * ma + mc * mc - 2 * ea * ec
    u0 = ma * ma + md * md - 2 * ea * ed
    span = 2 * pin * pout
    return (t0 - span, t0 + span), (u0 - span, u0 + span)


def has_tu_pole(
    s: float,
    channel_in: Tuple[int, int],
    channel_out: Tuple[int, int],
    masses: np.ndarray,
    cubic: np.ndarray,
) -> bool:
    a, b = channel_in
    c, d = channel_out
    trange, urange = transfer_ranges(s, channel_in, channel_out, masses)
    scale = max(1.0, s)
    for e, me in enumerate(masses):
        me2 = me * me
        tprod = cubic[a, c, e] * cubic[b, d, e]
        uprod = cubic[a, d, e] * cubic[b, c, e]
        if abs(tprod) > 1e-12 * scale and trange[0] <= me2 <= trange[1]:
            return True
        if abs(uprod) > 1e-12 * scale and urange[0] <= me2 <= urange[1]:
            return True
    return False


def near_s_channel_pole(
    s: float,
    channels: List[Tuple[int, int]],
    masses: np.ndarray,
    cubic: np.ndarray,
    c_s: float,
) -> bool:
    for e, me in enumerate(masses):
        if me <= 0:
            continue
        if abs(1.0 - s / (me * me)) > c_s:
            continue
        coupled = any(abs(cubic[a, b, e]) > 1e-10 for a, b in channels)
        if coupled:
            return True
    return False


def scan_open_channels(
    quadrature_order: int = 96,
    points: int = 420,
    c_s: float = 0.25,
) -> Dict[str, object]:
    """Scan from the lightest threshold using explicit pole exclusions.

    The s-channel exclusion follows Goodsell--Staub Eq. (11). For a t/u pole,
    every two-particle state participating in an offending matrix element is
    removed before diagonalisation. This intentionally conservative
    implementation can discard more information than a block-by-block SARAH
    treatment, so its result is reported separately.
    """
    p = benchmark()
    data = spectrum_and_couplings(p)
    masses = data["masses"]
    physical = [int(v) for v in data["physical"]]
    all_channels = [(i, j) for pos, i in enumerate(physical) for j in physical[pos:]]
    thresholds = sorted(set(float(masses[i] + masses[j]) for i, j in all_channels))
    lower = thresholds[0] * (1 + 1e-5)
    upper = 20000.0
    grid = list(np.geomspace(lower, upper, points))
    # Add points just above every threshold so threshold-local effects are not
    # missed by the logarithmic grid.
    for threshold in thresholds:
        for factor in (1.00001, 1.001, 1.01, 1.05, 1.20):
            value = threshold * factor
            if lower <= value <= upper:
                grid.append(value)
    grid = sorted(set(float(v) for v in grid))

    records = []
    skipped_s = 0
    skipped_all_tu = 0
    maximum = {"max_abs_eigenvalue": -1.0}
    for sqrt_s in grid:
        s = sqrt_s * sqrt_s
        channels = [
            pair for pair in all_channels if masses[pair[0]] + masses[pair[1]] <= sqrt_s
        ]
        if not channels:
            continue
        if near_s_channel_pole(s, channels, masses, data["cubic"], c_s):
            skipped_s += 1
            continue

        bad = set()
        for i, incoming in enumerate(channels):
            for j, outgoing in enumerate(channels):
                if has_tu_pole(s, incoming, outgoing, masses, data["cubic"]):
                    bad.add(i)
                    bad.add(j)
        retained = [pair for i, pair in enumerate(channels) if i not in bad]
        if not retained:
            skipped_all_tu += 1
            continue
        matrix = partial_wave_matrix(
            sqrt_s,
            retained,
            masses,
            data["cubic"],
            data["quartic"],
            quadrature_order,
        )
        eig = np.linalg.eigvalsh(matrix)
        value = float(np.max(np.abs(eig)))
        record = {
            "sqrt_s_GeV": sqrt_s,
            "open_channels": len(channels),
            "retained_channels": len(retained),
            "min_eigenvalue": float(eig[0]),
            "max_eigenvalue": float(eig[-1]),
            "max_abs_eigenvalue": value,
        }
        records.append(record)
        if value > maximum["max_abs_eigenvalue"]:
            maximum = record

    return {
        "sqrt_s_range_GeV": [lower, upper],
        "thresholds_GeV": thresholds,
        "grid_points": len(grid),
        "evaluated_points": len(records),
        "s_channel_excision_Cs": c_s,
        "skipped_s_channel_points": skipped_s,
        "skipped_all_channels_due_tu_poles": skipped_all_tu,
        "tu_policy": "Remove every state participating in any detected t/u pole before diagonalisation.",
        "maximum_over_scan": maximum,
        "passes_abs_Re_a0_le_half": bool(maximum["max_abs_eigenvalue"] <= 0.5),
        "sampled_scan": records[:: max(1, len(records) // 30)],
    }


def scan_goldstone_equivalence(
    g_x: float = 0.20,
    points: int = 220,
) -> Dict[str, object]:
    """Finite-energy scalar-potential matrix including would-be Goldstones.

    Feynman-gauge masses are assigned to the four zero modes: two M_W modes,
    one M_Z mode, and one dark-vector mode m_X=3 g_X f. Gauge interactions are
    not included, so this is the gaugeless Goldstone-equivalence layer used in
    scalar-sector unitarity studies, not a full vector-boson calculation.
    """
    p = benchmark()
    data = spectrum_and_couplings(p)
    masses = data["masses"].copy()
    rotation = data["rotation"]
    mw, mz, f = 80.4, 91.2, 1000.0
    dark_goldstone_mass = 3 * g_x * f
    assignments = {}
    for state in range(4):
        source = int(np.argmax(np.abs(rotation[:, state])))
        if source in (1, 2):
            masses[state] = mw
            label = "SM charged Goldstone"
        elif source == 3:
            masses[state] = mz
            label = "SM neutral Goldstone"
        elif source == 5:
            masses[state] = dark_goldstone_mass
            label = "dark Goldstone"
        else:
            raise RuntimeError(f"Unexpected zero-mode source field {source}")
        assignments[str(state)] = {
            "dominant_original_field_index": source,
            "label": label,
            "Feynman_gauge_mass_GeV": float(masses[state]),
        }

    channels = [(i, j) for i in range(rge.N) for j in range(i, rge.N)]
    lower = 2 * float(np.max(masses)) * (1 + 1e-5)
    upper = 20000.0
    energies = np.geomspace(lower, upper, points)
    records = []
    maximum = {"max_abs_eigenvalue": -1.0}
    for sqrt_s in energies:
        s = float(sqrt_s * sqrt_s)
        bad = set()
        for i, incoming in enumerate(channels):
            for j, outgoing in enumerate(channels):
                if has_tu_pole(s, incoming, outgoing, masses, data["cubic"]):
                    bad.add(i)
                    bad.add(j)
        retained = [pair for i, pair in enumerate(channels) if i not in bad]
        if not retained:
            continue
        matrix = partial_wave_matrix_analytic(
            float(sqrt_s), retained, masses, data["cubic"], data["quartic"]
        )
        eig = np.linalg.eigvalsh(matrix)
        value = float(np.max(np.abs(eig)))
        record = {
            "sqrt_s_GeV": float(sqrt_s),
            "min_eigenvalue": float(eig[0]),
            "max_eigenvalue": float(eig[-1]),
            "max_abs_eigenvalue": value,
            "retained_channels": len(retained),
        }
        records.append(record)
        if value > maximum["max_abs_eigenvalue"]:
            maximum = record
    return {
        "method": "Feynman-gauge Goldstone external states with scalar-potential interactions only",
        "gX": g_x,
        "mX_GeV": dark_goldstone_mass,
        "zero_mode_assignments": assignments,
        "channel_count": len(channels),
        "tu_policy": "Remove every state participating in any detected t/u pole before diagonalisation.",
        "sqrt_s_range_GeV": [lower, upper],
        "scan_points": points,
        "maximum_over_scan": maximum,
        "passes_abs_Re_a0_le_half": bool(maximum["max_abs_eigenvalue"] <= 0.5),
        "last_scan_point": records[-1],
        "sampled_scan": records[:: max(1, len(records) // 24)],
        "scope_warning": "Gauge vertices and transverse-vector channels are omitted; gX only fixes the dark Goldstone Feynman-gauge mass.",
    }


def scan(quadrature_order: int = 96, points: int = 180) -> Dict[str, object]:
    p = benchmark()
    data = spectrum_and_couplings(p)
    masses_all = data["masses"]
    physical = [int(v) for v in data["physical"]]
    channels = [(i, j) for pos, i in enumerate(physical) for j in physical[pos:]]
    largest_mass = max(masses_all[i] for i in physical)
    lower = 2 * largest_mass * (1 + 1e-5)
    upper = 20000.0
    energies = np.geomspace(lower, upper, points)
    records = []
    maximum = {"max_abs_eigenvalue": -1.0}
    for sqrt_s in energies:
        try:
            matrix = partial_wave_matrix(
                float(sqrt_s),
                channels,
                masses_all,
                data["cubic"],
                data["quartic"],
                quadrature_order,
            )
        except FloatingPointError:
            continue
        eig = np.linalg.eigvalsh(matrix)
        value = float(np.max(np.abs(eig)))
        record = {
            "sqrt_s_GeV": float(sqrt_s),
            "min_eigenvalue": float(eig[0]),
            "max_eigenvalue": float(eig[-1]),
            "max_abs_eigenvalue": value,
        }
        records.append(record)
        if value > maximum["max_abs_eigenvalue"]:
            maximum = record

    # Contact-only asymptote in the same four-state basis.
    contact = np.zeros((len(channels), len(channels)))
    quartic = data["quartic"]
    for i, (a, b) in enumerate(channels):
        for j, (c, d) in enumerate(channels):
            norm = math.sqrt((2 if a == b else 1) * (2 if c == d else 1))
            contact[j, i] = -quartic[a, b, c, d] / (16 * math.pi * norm)
    contact_eig = np.linalg.eigvalsh(contact)

    return {
        "calculation_scope": "Four massive physical scalars; contact plus all scalar exchanges; all ten channels open.",
        "excluded_scope": "Gauge-boson exchange, longitudinal-vector external states, and Goldstone external states.",
        "quadrature_order": quadrature_order,
        "scan_points": points,
        "sqrt_s_range_GeV": [float(lower), upper],
        "all_scalar_mass2_eigenvalues_GeV2": [float(v) for v in data["mass2"]],
        "massive_external_state_indices": physical,
        "massive_external_masses_GeV": [float(masses_all[i]) for i in physical],
        "channel_count": len(channels),
        "channels_by_mass_index": channels,
        "maximum_over_scan": maximum,
        "passes_abs_Re_a0_le_half": bool(maximum["max_abs_eigenvalue"] <= 0.5),
        "contact_only_asymptotic_eigenvalues": [float(v) for v in contact_eig],
        "last_scan_point": records[-1],
        "sampled_scan": records[:: max(1, len(records) // 24)],
        "warning": "A pass is only a physical-scalar-sector result, not a complete model unitarity certification.",
    }


def convergence_check() -> Dict[str, object]:
    results = {}
    for order in (48, 96, 192):
        result = scan(quadrature_order=order, points=90)
        results[str(order)] = result["maximum_over_scan"]
    values = [float(results[str(order)]["max_abs_eigenvalue"]) for order in (48, 96, 192)]
    return {
        "orders": results,
        "relative_difference_96_to_192": abs(values[1] - values[2]) / max(1e-15, abs(values[2])),
    }


def main() -> None:
    result = scan()
    result["quadrature_convergence"] = convergence_check()
    result["open_channel_scan"] = scan_open_channels()
    result["goldstone_equivalence_scan"] = scan_goldstone_equivalence()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
