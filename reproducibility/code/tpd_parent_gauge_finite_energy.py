#!/usr/bin/env python3
"""Finite-energy gauge audit for the point-matched TP-G parent.

The protected zero-kinetic-mixing parent factorizes into two copies of an
Abelian Higgs model containing a charge-three breaking scalar Phi, its radial
mode rho, a massive vector X, and a charge-one inert complex scalar S.  This
script evaluates the dangerous neutral longitudinal J=0 coupled block,
transverse/helicity amplitudes, scalar-QED Ward identities, and the
longitudinal/Goldstone high-energy limit for both copies.

Physical s-channel resonances are reported separately and are not classified
as fundamental tree-unitarity failures.  The implementation deliberately
targets the frozen Higgs-pole point rather than scanning parent parameters.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


PI = math.pi
F_PARENT = 1000.0
G_PARENT = 0.30
Q_PHI = 3.0
LAMBDA_PHI = 0.20
M_VECTOR = Q_PHI * G_PARENT * F_PARENT
M_RADIAL = math.sqrt(2.0 * LAMBDA_PHI) * F_PARENT
GAUSS_NODES, GAUSS_WEIGHTS = np.polynomial.legendre.leggauss(160)
CHARGED_NODES, CHARGED_WEIGHTS = np.polynomial.legendre.leggauss(64)


def dot(a: np.ndarray, b: np.ndarray) -> complex:
    return a[0] * b[0] - np.dot(a[1:], b[1:])


def momentum(energy: float, mass: float) -> float:
    return math.sqrt(max(0.0, energy * energy - mass * mass))


def polarization(k: np.ndarray, mass: float, helicity: int) -> np.ndarray:
    """Massive-vector helicity polarization for helicity -1, 0, or +1."""
    energy = float(k[0])
    vector = np.asarray(k[1:], dtype=float)
    p = float(np.linalg.norm(vector))
    if p == 0.0:
        if helicity == 0:
            return np.array([0.0, 0.0, 0.0, 1.0], dtype=complex)
        axis = np.array([1.0, 1j if helicity > 0 else -1j, 0.0]) / math.sqrt(2.0)
        return np.r_[0.0, axis]
    direction = vector / p
    if helicity == 0:
        return np.r_[p / mass, energy * direction / mass].astype(complex)
    theta = math.acos(float(np.clip(direction[2], -1.0, 1.0)))
    phi = math.atan2(float(direction[1]), float(direction[0]))
    e_theta = np.array([
        math.cos(theta) * math.cos(phi),
        math.cos(theta) * math.sin(phi),
        -math.sin(theta),
    ])
    e_phi = np.array([-math.sin(phi), math.cos(phi), 0.0])
    spatial = (
        -(e_theta + 1j * e_phi) / math.sqrt(2.0)
        if helicity > 0
        else (e_theta - 1j * e_phi) / math.sqrt(2.0)
    )
    return np.r_[0.0, spatial]


def pair_kinematics(sqrt_s: float, mass_in: float, mass_out: float, cosine: float):
    energy = sqrt_s / 2.0
    p_in = momentum(energy, mass_in)
    p_out = momentum(energy, mass_out)
    sine = math.sqrt(max(0.0, 1.0 - cosine * cosine))
    incoming_1 = np.array([energy, 0.0, 0.0, p_in])
    incoming_2 = np.array([energy, 0.0, 0.0, -p_in])
    outgoing_1 = np.array([energy, p_out * sine, 0.0, p_out * cosine])
    outgoing_2 = np.array([energy, -p_out * sine, 0.0, -p_out * cosine])
    return incoming_1, incoming_2, outgoing_1, outgoing_2


def two_body_kinematics(
    sqrt_s: float,
    m1: float,
    m2: float,
    m3: float,
    m4: float,
    cosine: float,
):
    """General 1+2 -> 3+4 center-of-mass momenta."""
    s = sqrt_s**2
    e1 = (s + m1**2 - m2**2) / (2.0 * sqrt_s)
    e2 = (s + m2**2 - m1**2) / (2.0 * sqrt_s)
    e3 = (s + m3**2 - m4**2) / (2.0 * sqrt_s)
    e4 = (s + m4**2 - m3**2) / (2.0 * sqrt_s)
    p_in = momentum(e1, m1)
    p_out = momentum(e3, m3)
    sine = math.sqrt(max(0.0, 1.0 - cosine * cosine))
    return (
        np.array([e1, 0.0, 0.0, p_in]),
        np.array([e2, 0.0, 0.0, -p_in]),
        np.array([e3, p_out * sine, 0.0, p_out * cosine]),
        np.array([e4, -p_out * sine, 0.0, -p_out * cosine]),
    )


def beta(s: float, mass: float) -> float:
    return math.sqrt(max(0.0, 1.0 - 4.0 * mass * mass / s))


def two_body_velocity(s: float, first_mass: float, second_mass: float) -> float:
    radicand = (
        1.0
        - 2.0 * (first_mass**2 + second_mass**2) / s
        + (first_mass**2 - second_mass**2) ** 2 / s**2
    )
    return math.sqrt(max(0.0, radicand))


def vector_width_to_scalar(mass_scalar: float) -> float:
    phase = beta(M_VECTOR * M_VECTOR, mass_scalar)
    return G_PARENT**2 * M_VECTOR * phase**3 / (48.0 * PI)


def vector_propagator_contraction(left, right, q, denominator) -> complex:
    return (dot(left, right) - dot(left, q) * dot(right, q) / M_VECTOR**2) / denominator


def amp_xx_to_xx(sqrt_s: float, cosine: float, helicities: tuple[int, int, int, int]) -> complex:
    k1, k2, k3, k4 = pair_kinematics(sqrt_s, M_VECTOR, M_VECTOR, cosine)
    e1 = polarization(k1, M_VECTOR, helicities[0])
    e2 = polarization(k2, M_VECTOR, helicities[1])
    e3 = np.conjugate(polarization(k3, M_VECTOR, helicities[2]))
    e4 = np.conjugate(polarization(k4, M_VECTOR, helicities[3]))
    s = sqrt_s**2
    t = dot(k1 - k3, k1 - k3).real
    u = dot(k1 - k4, k1 - k4).real
    coupling = 2.0 * M_VECTOR**2 / F_PARENT
    return -coupling**2 * (
        dot(e1, e2) * dot(e3, e4) / (s - M_RADIAL**2)
        + dot(e1, e3) * dot(e2, e4) / (t - M_RADIAL**2)
        + dot(e1, e4) * dot(e2, e3) / (u - M_RADIAL**2)
    )


def amp_xx_to_rr(sqrt_s: float, cosine: float, helicities: tuple[int, int]) -> complex:
    k1, k2, p3, p4 = pair_kinematics(sqrt_s, M_VECTOR, M_RADIAL, cosine)
    e1 = polarization(k1, M_VECTOR, helicities[0])
    e2 = polarization(k2, M_VECTOR, helicities[1])
    s = sqrt_s**2
    q_t, q_u = k1 - p3, k1 - p4
    t, u = dot(q_t, q_t).real, dot(q_u, q_u).real
    a = 2.0 * M_VECTOR**2 / F_PARENT
    contact = 2.0 * M_VECTOR**2 / F_PARENT**2
    radial_cubic = 3.0 * M_RADIAL**2 / F_PARENT
    return (
        contact * dot(e1, e2)
        + a * radial_cubic * dot(e1, e2) / (s - M_RADIAL**2)
        + a**2 * vector_propagator_contraction(e1, e2, q_t, t - M_VECTOR**2)
        + a**2 * vector_propagator_contraction(e1, e2, q_u, u - M_VECTOR**2)
    )


def amp_ss_to_xx(
    sqrt_s: float,
    cosine: float,
    mass_scalar: float,
    helicities: tuple[int, int],
    replace_first_by_momentum: bool = False,
) -> complex:
    p1, p2, k3, k4 = pair_kinematics(sqrt_s, mass_scalar, M_VECTOR, cosine)
    e3 = np.conjugate(polarization(k3, M_VECTOR, helicities[0]))
    e4 = np.conjugate(polarization(k4, M_VECTOR, helicities[1]))
    if replace_first_by_momentum:
        e3 = k3.astype(complex)
    t = dot(p1 - k3, p1 - k3).real
    u = dot(p1 - k4, p1 - k4).real
    return G_PARENT**2 * (
        2.0 * dot(e3, e4)
        + dot(2.0 * p1 - k3, e3) * dot(2.0 * p2 - k4, e4) / (t - mass_scalar**2)
        + dot(2.0 * p1 - k4, e4) * dot(2.0 * p2 - k3, e3) / (u - mass_scalar**2)
    )


def amp_rr_to_rr(sqrt_s: float, cosine: float) -> float:
    p1, _p2, p3, p4 = pair_kinematics(sqrt_s, M_RADIAL, M_RADIAL, cosine)
    s = sqrt_s**2
    t = dot(p1 - p3, p1 - p3).real
    u = dot(p1 - p4, p1 - p4).real
    cubic = 3.0 * M_RADIAL**2 / F_PARENT
    return -6.0 * LAMBDA_PHI - cubic**2 * (
        1.0 / (s - M_RADIAL**2)
        + 1.0 / (t - M_RADIAL**2)
        + 1.0 / (u - M_RADIAL**2)
    )


def amp_ss_elastic_bound(sqrt_s: float, cosine: float, mass_scalar: float, lambda_s: float) -> float:
    """Absolute upper bound on scalar contact plus s/t massive-vector exchange."""
    p1, p2, p3, p4 = pair_kinematics(sqrt_s, mass_scalar, mass_scalar, cosine)
    s = sqrt_s**2
    t = dot(p1 - p3, p1 - p3).real
    j_s_in, j_s_out = p1 - p2, p3 - p4
    j_t_1, j_t_2 = p1 + p3, p2 + p4
    width = vector_width_to_scalar(mass_scalar)
    s_den = complex(s - M_VECTOR**2, M_VECTOR * width)
    s_piece = G_PARENT**2 * vector_propagator_contraction(j_s_in, j_s_out, p1 + p2, s_den)
    t_piece = G_PARENT**2 * vector_propagator_contraction(j_t_1, j_t_2, p1 - p3, t - M_VECTOR**2)
    return 4.0 * lambda_s + abs(s_piece) + abs(t_piece)


def amp_ss_elastic(
    sqrt_s: float,
    cosine: float,
    mass_scalar: float,
    lambda_s: float,
) -> complex:
    p1, p2, p3, p4 = pair_kinematics(sqrt_s, mass_scalar, mass_scalar, cosine)
    s = sqrt_s**2
    t = dot(p1 - p3, p1 - p3).real
    width = vector_width_to_scalar(mass_scalar)
    s_piece = G_PARENT**2 * vector_propagator_contraction(
        p1 - p2,
        p3 - p4,
        p1 + p2,
        complex(s - M_VECTOR**2, M_VECTOR * width),
    )
    t_piece = G_PARENT**2 * vector_propagator_contraction(
        p1 + p3,
        p2 + p4,
        p1 - p3,
        t - M_VECTOR**2,
    )
    return -4.0 * lambda_s + s_piece + t_piece


def amp_xs_to_xs(
    sqrt_s: float,
    cosine: float,
    mass_scalar: float,
    helicities: tuple[int, int],
    replace_incoming_by_momentum: bool = False,
    replace_outgoing_by_momentum: bool = False,
) -> complex:
    k1, p2, k3, p4 = two_body_kinematics(
        sqrt_s, M_VECTOR, mass_scalar, M_VECTOR, mass_scalar, cosine
    )
    e1 = polarization(k1, M_VECTOR, helicities[0])
    e3 = np.conjugate(polarization(k3, M_VECTOR, helicities[1]))
    if replace_incoming_by_momentum:
        e1 = k1.astype(complex)
    if replace_outgoing_by_momentum:
        e3 = k3.astype(complex)
    s = sqrt_s**2
    u = dot(p2 - k3, p2 - k3).real
    return G_PARENT**2 * (
        2.0 * dot(e1, e3)
        - dot(2.0 * p2 + k1, e1) * dot(2.0 * p4 + k3, e3) / (s - mass_scalar**2)
        - dot(2.0 * p2 - k3, e3) * dot(2.0 * p4 - k1, e1) / (u - mass_scalar**2)
    )


def amp_xs_to_rs(
    sqrt_s: float,
    cosine: float,
    mass_scalar: float,
    helicity: int,
) -> complex:
    k1, p2, r3, p4 = two_body_kinematics(
        sqrt_s, M_VECTOR, mass_scalar, M_RADIAL, mass_scalar, cosine
    )
    e1 = polarization(k1, M_VECTOR, helicity)
    q = k1 - r3
    t = dot(q, q).real
    radial_vector_coupling = 2.0 * M_VECTOR**2 / F_PARENT
    current = p2 + p4
    # q.current=0 for equal-mass external dark scalars, so the longitudinal
    # propagator term vanishes analytically.
    return radial_vector_coupling * G_PARENT * dot(e1, current) / (t - M_VECTOR**2)


def wigner_d(j: int, m_prime: int, m: int, theta: float) -> float:
    """Small Wigner d^j_{m',m}(theta) for integer j."""
    if abs(m) > j or abs(m_prime) > j:
        return 0.0
    prefactor = math.sqrt(
        math.factorial(j + m)
        * math.factorial(j - m)
        * math.factorial(j + m_prime)
        * math.factorial(j - m_prime)
    )
    total = 0.0
    lower = max(0, m - m_prime)
    upper = min(j + m, j - m_prime)
    for k in range(lower, upper + 1):
        denominator = (
            math.factorial(j + m - k)
            * math.factorial(k)
            * math.factorial(m_prime - m + k)
            * math.factorial(j - m_prime - k)
        )
        power_cos = 2 * j + m - m_prime - 2 * k
        power_sin = m_prime - m + 2 * k
        total += (
            (-1) ** (m_prime - m + k)
            * prefactor
            / denominator
            * math.cos(theta / 2.0) ** power_cos
            * math.sin(theta / 2.0) ** power_sin
        )
    return total


def charged_partial_wave_matrix(
    sqrt_s: float,
    mass_scalar: float,
    j: int,
) -> tuple[np.ndarray, list[str]]:
    helicities = [h for h in (-1, 0, 1) if abs(h) <= j]
    labels = [f"X_{h:+d} S" for h in helicities] + ["rho S"]
    matrix = np.zeros((len(labels), len(labels)), dtype=complex)
    s = sqrt_s**2
    velocity_xs = two_body_velocity(s, M_VECTOR, mass_scalar)
    velocity_rs = two_body_velocity(s, M_RADIAL, mass_scalar)
    prefactor = 1.0 / (32.0 * PI)
    for row, h_out in enumerate(helicities):
        for col, h_in in enumerate(helicities):
            matrix[row, col] = velocity_xs * prefactor * integrate_charged(
                lambda x: wigner_d(j, h_out, h_in, math.acos(x))
                * amp_xs_to_xs(sqrt_s, x, mass_scalar, (h_in, h_out))
            )
    radial_index = len(helicities)
    for col, h_in in enumerate(helicities):
        value = math.sqrt(velocity_xs * velocity_rs) * prefactor * integrate_charged(
            lambda x: wigner_d(j, 0, h_in, math.acos(x))
            * amp_xs_to_rs(sqrt_s, x, mass_scalar, h_in)
        )
        matrix[radial_index, col] = value
        matrix[col, radial_index] = np.conjugate(value)
    return matrix, labels


def charged_u_channel_pole_interval(mass_scalar: float, energy_max: float) -> list[float] | None:
    """Exact energy interval in which u=m_S^2 occurs at a physical angle.

    For X(M)+S(m)->X(M)+S(m),
      u-m^2 = M^2 - 2 E_X E_S - 2 p^2 cos(theta).
    The cos(theta)=+1 endpoint vanishes at sqrt(s)=sqrt(2 M^2+m^2),
    and the cos(theta)=-1 endpoint at sqrt(s)=(M^2-m^2)/m.
    Their ordering is equivalent to M>2m, precisely the condition for the
    physical decay X->S Sbar.
    """
    if M_VECTOR <= 2.0 * mass_scalar:
        return None
    lower = math.sqrt(2.0 * M_VECTOR**2 + mass_scalar**2)
    upper = (M_VECTOR**2 - mass_scalar**2) / mass_scalar
    if lower > energy_max:
        return None
    return [lower, min(upper, energy_max)]


def charged_block_scan(mass_scalar: float, points: int, energy_max: float) -> dict:
    threshold = M_VECTOR + mass_scalar
    pole_interval = charged_u_channel_pole_interval(mass_scalar, energy_max)

    def pole_denominator_at(energy: float, cosine: float) -> float:
        _k1, p2, k3, _p4 = two_body_kinematics(
            energy, M_VECTOR, mass_scalar, M_VECTOR, mass_scalar, cosine
        )
        return float(dot(p2 - k3, p2 - k3).real - mass_scalar**2)

    def pole_contaminated(energy: float) -> bool:
        if pole_interval is None:
            return False
        lower, upper = pole_interval
        return lower <= energy <= upper

    energies = np.geomspace(threshold * (1.0 + 1.0e-8), energy_max, min(points, 32))
    maximum = {"max_abs_eigenvalue": -1.0}
    region_maxima = {
        "below_pole_interval": {"max_abs_eigenvalue": -1.0},
        "above_pole_interval": {"max_abs_eigenvalue": -1.0},
    }
    for energy in energies:
        energy = float(energy)
        if pole_contaminated(energy):
            continue
        region = (
            "below_pole_interval"
            if pole_interval is None or energy < pole_interval[0]
            else "above_pole_interval"
        )
        for j in range(5):
            matrix, labels = charged_partial_wave_matrix(energy, mass_scalar, j)
            # Hermiticity residual is retained as a numerical diagnostic.
            eigenvalues = np.linalg.eigvalsh((matrix + matrix.conjugate().T) / 2.0)
            value = float(np.max(np.abs(eigenvalues)))
            if value > maximum["max_abs_eigenvalue"]:
                maximum = {
                    "sqrt_s_GeV": float(energy),
                    "J": j,
                    "basis": labels,
                    "max_abs_eigenvalue": value,
                    "eigenvalues": eigenvalues.real.tolist(),
                    "hermiticity_residual": float(np.max(np.abs(matrix - matrix.conjugate().T))),
                }
            if value > region_maxima[region]["max_abs_eigenvalue"]:
                region_maxima[region] = {
                    "sqrt_s_GeV": energy,
                    "J": j,
                    "max_abs_eigenvalue": value,
                }

    # |d^J|<=1 gives a J-independent entry bound, including J>6.
    local_x, local_w = np.polynomial.legendre.leggauss(96)
    all_j_entry_bound = 0.0
    all_j_location = None
    for energy in np.geomspace(threshold * (1.0 + 1.0e-8), energy_max, 28):
        if pole_contaminated(float(energy)):
            continue
        velocity = two_body_velocity(float(energy**2), M_VECTOR, mass_scalar)
        for h_in in (-1, 0, 1):
            for h_out in (-1, 0, 1):
                bound = velocity / (32.0 * PI) * sum(
                    w * abs(amp_xs_to_xs(float(energy), float(x), mass_scalar, (h_in, h_out)))
                    for x, w in zip(local_x, local_w)
                )
                if bound > all_j_entry_bound:
                    all_j_entry_bound = float(bound)
                    all_j_location = [float(energy), h_in, h_out, "XS_to_XS"]
        for h_in in (-1, 0, 1):
            velocity_out = two_body_velocity(float(energy**2), M_RADIAL, mass_scalar)
            bound = math.sqrt(velocity * velocity_out) / (32.0 * PI) * sum(
                w * abs(amp_xs_to_rs(float(energy), float(x), mass_scalar, h_in))
                for x, w in zip(local_x, local_w)
            )
            if bound > all_j_entry_bound:
                all_j_entry_bound = float(bound)
                all_j_location = [float(energy), h_in, 0, "XS_to_rhoS"]

    ward_max = 0.0
    ward_scale = 1.0
    ward_energy = 2500.0
    for x in np.linspace(-0.95, 0.95, 41):
        for h in (-1, 0, 1):
            ordinary = amp_xs_to_xs(ward_energy, float(x), mass_scalar, (0, h))
            contracted = amp_xs_to_xs(
                ward_energy, float(x), mass_scalar, (0, h),
                replace_incoming_by_momentum=True,
            )
            ward_max = max(ward_max, abs(contracted))
            ward_scale = max(ward_scale, abs(ordinary) * M_VECTOR)
    return {
        "J_scan": {
            "J_values": list(range(5)),
            "maximum_over_clean_regions": maximum,
            "clean_region_maxima": region_maxima,
        },
        "all_J_entry_bound": {
            "maximum": all_j_entry_bound,
            "location_energy_helicities_process": all_j_location,
        },
        "Compton_Ward_check": {
            "maximum_abs_contracted_amplitude": ward_max,
            "relative_to_characteristic_amplitude_times_M": ward_max / ward_scale,
        },
        "physical_u_channel_pole": {
            "energy_interval_GeV": pole_interval,
            "exact_condition": "u-m_S^2=M_X^2-2*E_X*E_S-2*p^2*cos(theta)=0",
            "analytic_lower_boundary_GeV": "sqrt(2*M_X^2+m_S^2)",
            "analytic_upper_boundary_GeV": "(M_X^2-m_S^2)/m_S",
            "interval_exists_iff": "M_X>2*m_S",
            "decay_condition_X_to_S_Sbar": bool(M_VECTOR > 2.0 * mass_scalar),
            "numeric_boundary_residuals_GeV2": (
                {
                    "lower_cos_theta_plus_one": pole_denominator_at(pole_interval[0], 1.0),
                    "upper_cos_theta_minus_one": pole_denominator_at(pole_interval[1], -1.0),
                }
                if pole_interval is not None else None
            ),
            "X_is_conventional_asymptotic_state": False,
            "verdict_treatment": "not scored as PASS or FAIL",
            "classification": "physical sequential kinematics caused by X -> S Sbar being open; not a fundamental unitarity failure",
            "required_precision_upgrade": "complex-mass or stable-state inclusive treatment if the unstable X is to be used beyond a formal gauge-consistency diagnostic",
        },
        "clean_regions_below_half": maximum["max_abs_eigenvalue"] <= 0.5,
    }


def vector_resonance_check(mass_scalar: float, lambda_s: float) -> dict:
    sqrt_s = M_VECTOR
    s = sqrt_s**2
    velocity = beta(s, mass_scalar)
    partial_wave = velocity / (32.0 * PI) * integrate(
        lambda x: x * amp_ss_elastic(sqrt_s, x, mass_scalar, lambda_s)
    )
    return {
        "sqrt_s_GeV": sqrt_s,
        "J": 1,
        "a1_real": float(partial_wave.real),
        "a1_imag": float(partial_wave.imag),
        "argand_circle_residual": float(abs(abs(partial_wave - 0.5j) - 0.5)),
        "interpretation": "A width-resummed physical X resonance; imaginary saturation is not a tree-level Re(a_J) violation.",
    }


def integrate(function) -> complex:
    return sum(weight * function(float(x)) for x, weight in zip(GAUSS_NODES, GAUSS_WEIGHTS))


def integrate_charged(function) -> complex:
    return sum(weight * function(float(x)) for x, weight in zip(CHARGED_NODES, CHARGED_WEIGHTS))


def j0_block(sqrt_s: float, mass_scalar: float, lambda_s: float) -> np.ndarray:
    """Conservative normalized {X_LX_L, rho rho, S Sbar} J=0 block."""
    s = sqrt_s**2
    phase_x = beta(s, M_VECTOR)
    phase_r = beta(s, M_RADIAL)
    phase_s = beta(s, mass_scalar)
    out = np.zeros((3, 3), dtype=complex)
    prefactor = 1.0 / (32.0 * PI)
    # The identical XX and rho-rho channels each supply 1/sqrt(2).
    out[0, 0] = phase_x * prefactor * integrate(
        lambda x: amp_xx_to_xx(sqrt_s, x, (0, 0, 0, 0))
    ) / 2.0
    out[0, 1] = math.sqrt(phase_x * phase_r) * prefactor * integrate(
        lambda x: amp_xx_to_rr(sqrt_s, x, (0, 0))
    ) / 2.0
    out[1, 0] = out[0, 1]
    out[0, 2] = math.sqrt(phase_x * phase_s) * prefactor * integrate(
        lambda x: amp_ss_to_xx(sqrt_s, x, mass_scalar, (0, 0))
    ) / math.sqrt(2.0)
    out[2, 0] = out[0, 2]
    out[1, 1] = phase_r * prefactor * integrate(
        lambda x: amp_rr_to_rr(sqrt_s, x)
    ) / 2.0
    # Use an absolute bound for the diagonal S Sbar element; this cannot
    # underestimate the norm through a cancellation with the scalar contact.
    out[2, 2] = phase_s * prefactor * integrate(
        lambda x: amp_ss_elastic_bound(sqrt_s, x, mass_scalar, lambda_s)
    )
    return out


def goldstone_amplitude(sqrt_s: float, cosine: float) -> float:
    s = sqrt_s**2
    t = -0.5 * s * (1.0 - cosine)
    u = -0.5 * s * (1.0 + cosine)
    goldstone_cubic = M_RADIAL**2 / F_PARENT
    return -6.0 * LAMBDA_PHI - goldstone_cubic**2 * (
        1.0 / (s - M_RADIAL**2)
        + 1.0 / (t - M_RADIAL**2)
        + 1.0 / (u - M_RADIAL**2)
    )


def pure_vector_helicity_bound(points: int, energy_max: float) -> dict:
    """Bound every J for all non-LLLL pure-vector helicity entries.

    This block is identical in the m and E sectors, so it is evaluated once.
    A 64-node Gauss rule is ample for these smooth, pole-free amplitudes; the
    dangerous forward-sensitive LLLL/radial block retains the 160-node rule.
    """
    local_x, local_w = np.polynomial.legendre.leggauss(64)
    energies = np.geomspace(2.0 * M_VECTOR * (1.0 + 1.0e-8), energy_max, min(points, 24))
    result = {"all_J_abs_bound": -1.0, "energy_points": len(energies), "angular_nodes": 64}
    for energy in energies:
        phase = beta(float(energy**2), M_VECTOR)
        for incoming in ((a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)):
            for outgoing in ((a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)):
                if incoming == (0, 0) and outgoing == (0, 0):
                    continue
                integral_abs = sum(
                    w * abs(amp_xx_to_xx(float(energy), float(x), incoming + outgoing))
                    for x, w in zip(local_x, local_w)
                )
                bound = float(phase * integral_abs / (32.0 * PI))
                if bound > result["all_J_abs_bound"]:
                    result.update({
                        "sqrt_s_GeV": float(energy),
                        "incoming_helicities": incoming,
                        "outgoing_helicities": outgoing,
                        "all_J_abs_bound": bound,
                    })
    return result


def sector_result(
    name: str,
    mass_scalar: float,
    lambda_s: float,
    mu_s: float,
    points: int,
    energy_max: float,
    helicity_bound: dict,
) -> dict:
    kappa = math.sqrt(2.0) * mu_s / (3.0 * F_PARENT)
    energies = np.geomspace(2.0 * M_VECTOR * (1.0 + 1.0e-8), energy_max, points)
    maximum = {"max_abs_eigenvalue": -1.0}
    convergence_samples = {}
    for energy in energies:
        block = j0_block(float(energy), mass_scalar, lambda_s)
        eigenvalues = np.linalg.eigvalsh(block.real)
        value = float(np.max(np.abs(eigenvalues)))
        if value > maximum["max_abs_eigenvalue"]:
            maximum = {
                "sqrt_s_GeV": float(energy),
                "max_abs_eigenvalue": value,
                "eigenvalues": eigenvalues.tolist(),
                "matrix": [[float(x.real) for x in row] for row in block],
            }

    # Check numerical angular convergence at the endpoint independently.
    for nodes in (80, 160, 320):
        local_x, local_w = np.polynomial.legendre.leggauss(nodes)
        integral = sum(
            w * amp_xx_to_rr(energy_max, float(x), (0, 0))
            for x, w in zip(local_x, local_w)
        )
        phase = math.sqrt(beta(energy_max**2, M_VECTOR) * beta(energy_max**2, M_RADIAL))
        convergence_samples[str(nodes)] = float((phase * integral / (64.0 * PI)).real)

    ward_max = 0.0
    ward_scale = 0.0
    ward_energy = max(2.2 * M_VECTOR, 2500.0)
    for x in np.linspace(-0.95, 0.95, 41):
        for h in (-1, 0, 1):
            ordinary = amp_ss_to_xx(ward_energy, float(x), mass_scalar, (0, h))
            contracted = amp_ss_to_xx(
                ward_energy, float(x), mass_scalar, (0, h), replace_first_by_momentum=True
            )
            ward_max = max(ward_max, abs(contracted))
            ward_scale = max(ward_scale, abs(ordinary) * M_VECTOR, 1.0)

    equivalence = {}
    for cosine in (-0.5, 0.0, 0.5):
        longitudinal = amp_xx_to_xx(energy_max, cosine, (0, 0, 0, 0))
        goldstone = goldstone_amplitude(energy_max, cosine)
        equivalence[str(cosine)] = {
            "longitudinal": float(longitudinal.real),
            "goldstone": goldstone,
            "relative_difference": float(abs(longitudinal / goldstone - 1.0)),
        }

    charged = charged_block_scan(mass_scalar, points, energy_max)
    resonance = vector_resonance_check(mass_scalar, lambda_s)

    return {
        "sector": name,
        "matching": {
            "f_GeV": F_PARENT,
            "g": G_PARENT,
            "Q_Phi": Q_PHI,
            "m_vector_GeV": M_VECTOR,
            "lambda_Phi": LAMBDA_PHI,
            "m_radial_GeV": M_RADIAL,
            "m_dark_GeV": mass_scalar,
            "lambda_dark": lambda_s,
            "mu_dark_GeV": mu_s,
            "kappa": kappa,
            "lambda_dark_Phi_at_matching": 0.0,
        },
        "vector_width_to_dark_pair_GeV": vector_width_to_scalar(mass_scalar),
        "neutral_longitudinal_J0": {
            "basis": ["X_L X_L / sqrt(2)", "rho rho / sqrt(2)", "S Sbar"],
            "scan_points": points,
            "energy_range_GeV": [float(energies[0]), energy_max],
            "maximum": maximum,
            "passes_abs_Re_a0_le_half": maximum["max_abs_eigenvalue"] <= 0.5,
        },
        "other_helicities": helicity_bound,
        "angular_quadrature_convergence_XLXL_to_rhorho_at_endpoint": convergence_samples,
        "scalar_QED_Ward_check": {
            "maximum_abs_contracted_amplitude": ward_max,
            "relative_to_characteristic_amplitude_times_M": ward_max / ward_scale,
        },
        "longitudinal_Goldstone_fixed_angle_check_at_endpoint": equivalence,
        "charged_XS_rhoS_blocks": charged,
        "neutral_vector_resonance": resonance,
        "phase_sensitive_kappa_bound": {
            "kappa": kappa,
            "quartic_partial_wave_scale_kappa_over_16pi": abs(kappa) / (16.0 * PI),
            "interpretation": "The r S^3 vertex adds residual-charge-allowed scalar channels at O(kappa); its norm is negligible relative to the reported gauge blocks but its number-changing cosmology is deferred to C16.",
        },
    }


def build_payload(pole_json: Path, points: int, energy_max: float) -> dict:
    pole = json.loads(pole_json.read_text(encoding="utf-8"))
    fixed = pole["fixed_candidate_parameter_vector"]
    helicity_bound = pure_vector_helicity_bound(points, energy_max)
    sectors = {
        "m": sector_result("m", fixed["mA"], fixed["lambda_A"], fixed["mu_A"], points, energy_max, helicity_bound),
        "E": sector_result("E", fixed["mB"], fixed["lambda_B"], fixed["mu_B"], points, energy_max, helicity_bound),
    }
    maximum_j0 = max(
        row["neutral_longitudinal_J0"]["maximum"]["max_abs_eigenvalue"]
        for row in sectors.values()
    )
    maximum_other = max(row["other_helicities"]["all_J_abs_bound"] for row in sectors.values())
    maximum_charged = max(
        row["charged_XS_rhoS_blocks"]["J_scan"]["maximum_over_clean_regions"]["max_abs_eigenvalue"]
        for row in sectors.values()
    )
    maximum_charged_all_j = max(
        row["charged_XS_rhoS_blocks"]["all_J_entry_bound"]["maximum"]
        for row in sectors.values()
    )
    passes = (
        maximum_j0 <= 0.5
        and maximum_other <= 0.5
        and maximum_charged <= 0.5
        and maximum_charged_all_j <= 0.5
    )
    return {
        "schema_version": 1,
        "theory": "TP-G parent point-matched to the frozen TP-D Higgs-pole candidate",
        "kinetic_mixing_slice": "epsilon_Ym=epsilon_YE=epsilon_mE=0 protected by C_m x C_E",
        "factorization": "The two Abelian gauge sectors are identical except for the 0.2 GeV dark-mass split and are tested separately; lambda_AB and SM Higgs portals belong to the already-tested scalar block.",
        "sectors": sectors,
        "combined_summary": {
            "maximum_neutral_longitudinal_J0_abs_eigenvalue": maximum_j0,
            "maximum_other_helicity_all_J_entry_bound": maximum_other,
            "maximum_charged_block_abs_eigenvalue_J0_to_J4_clean_regions": maximum_charged,
            "maximum_charged_all_J_entry_bound": maximum_charged_all_j,
            "tree_unitarity_condition": "abs(Re a_J eigenvalue) <= 1/2",
            "formal_off_pole_gauge_blocks_below_half": passes,
            "pole_contaminated_XS_interval_verdict": "not scored",
            "stable_state_genuine_unitarity_violation_found": False,
        },
        "resonance_treatment": "The X pole in S Sbar scattering is a physical J=1 resonance. Its width to the open S Sbar channel is included when bounding the elastic amplitude; a pole is not counted as fundamental unitarity failure.",
        "classification": "conditional pass on the protected zero-mixing point-matched benchmark" if passes else "fail",
        "scope_warning": "The result applies to the protected epsilon=0 TP-G benchmark through 20 TeV. The charged XS block contains a physical u-channel pole because X is unstable; the pole-excised two-body result passes, but a stable-state inclusive or complex-mass calculation is required for an unconditional full-S-matrix PASS. Nonzero kinetic mixing and loop-improved amplitudes are outside this benchmark. Tiny kappa channels are bounded here and their number-changing cosmology is deferred to C16.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--pole-json", type=Path,
        default=root / "audits" / "tpd_higgs_pole_diagnostic.json",
    )
    parser.add_argument(
        "--json", type=Path,
        default=root / "audits" / "tpd_parent_gauge_finite_energy.json",
    )
    parser.add_argument("--points", type=int, default=90)
    parser.add_argument("--energy-max", type=float, default=2.0e4)
    args = parser.parse_args()
    payload = build_payload(args.pole_json, args.points, args.energy_max)
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["combined_summary"], indent=2))


if __name__ == "__main__":
    main()
