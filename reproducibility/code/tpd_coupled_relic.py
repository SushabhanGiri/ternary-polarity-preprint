#!/usr/bin/env python3
"""Leading coupled freeze-out diagnostic for the exact TP-D benchmark.

The evolved yields are per charge state: Y_A = n_A/s = n_Abar/s and
Y_B = n_B/s = n_Bbar/s.  The final energy density therefore contains an
explicit factor two.  Cross sections are threshold, tree-level estimates;
g_* and g_*s are held fixed.  This is a rejection/triage calculation, not a
precision relic-density prediction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import kn


PI = math.pi
MPL = 1.2209e19  # GeV, unreduced Planck mass for H=1.66 sqrt(g*) T^2/Mpl
VEV = 246.22
MH = 125.25
MW = 80.377
MZ = 91.1876
MT = 172.5
MBOTTOM = 4.18
MCHARM = 1.27
MTAU = 1.77686
GF = 1.1663787e-5
GEV2_TO_CM3_S = 0.389379338e-27 * 2.99792458e10
OMEGA_FACTOR = 2.742e8  # Omega h^2 = factor * sum_i m_i Y_i(total)


def kallen_bar(s: float, m1sq: float, m2sq: float) -> float:
    """Dimensionless lambda(1,m1^2/s,m2^2/s)."""
    x, y = m1sq / s, m2sq / s
    return max(0.0, 1.0 + x * x + y * y - 2.0 * x - 2.0 * y - 2.0 * x * y)


def width_vector(q: float, mass: float, identical: bool) -> float:
    if q <= 2.0 * mass:
        return 0.0
    x = mass * mass / (q * q)
    prefactor = GF * q**3 / (8.0 * PI * math.sqrt(2.0))
    if identical:
        prefactor *= 0.5
    return prefactor * math.sqrt(1.0 - 4.0 * x) * (1.0 - 4.0 * x + 12.0 * x * x)


def width_fermion(q: float, mass: float, colour: int) -> float:
    if q <= 2.0 * mass:
        return 0.0
    x = mass * mass / (q * q)
    return (
        colour
        * GF
        * mass**2
        * q
        / (4.0 * PI * math.sqrt(2.0))
        * (1.0 - 4.0 * x) ** 1.5
    )


def offshell_sm_width_without_hh(q: float) -> float:
    """Tree-level SM Higgs width at virtual mass q, excluding h*h*."""
    return (
        width_vector(q, MW, identical=False)
        + width_vector(q, MZ, identical=True)
        + width_fermion(q, MT, 3)
        + width_fermion(q, MBOTTOM, 3)
        + width_fermion(q, MCHARM, 3)
        + width_fermion(q, MTAU, 1)
    )


def sigma_v_ann_to_sm(mass: float, portal: float) -> float:
    """XXbar -> SM except hh, through an s-channel Higgs at s=4m^2."""
    q = 2.0 * mass
    s = q * q
    width = offshell_sm_width_without_hh(q)
    denominator = (s - MH * MH) ** 2  # width is negligible far from the pole here
    return 2.0 * portal**2 * VEV**2 * width / (q * denominator)


def sigma_v_ann_to_hh(mass: float, portal: float) -> float:
    """Threshold XXbar -> hh including contact, s-, t-, and u-channel graphs."""
    if mass <= MH:
        return 0.0
    s = 4.0 * mass * mass
    t_minus_m2 = MH * MH - 2.0 * mass * mass
    amplitude = (
        -portal * (1.0 + 3.0 * MH * MH / (s - MH * MH))
        - 2.0 * portal**2 * VEV**2 / t_minus_m2
    )
    beta = math.sqrt(1.0 - MH * MH / (mass * mass))
    return beta * amplitude**2 / (64.0 * PI * mass * mass)


def sigma_v_semi(mass: float, portal: float, cubic_mu: float) -> float:
    """Threshold XX -> Xbar h from the three external-leg emission graphs.

    The potential convention is mu/3 (X^3 + h.c.), so the XXX rule is
    -2 i mu and the h X Xbar rule is -i lambda_HX v.
    """
    if mass <= MH:
        return 0.0
    s = 4.0 * mass * mass
    t_minus_m2 = 0.5 * (MH * MH - 3.0 * mass * mass)
    propagator_sum = 1.0 / (3.0 * mass * mass) + 2.0 / t_minus_m2
    amplitude = 2.0 * cubic_mu * portal * VEV * propagator_sum
    phase = math.sqrt(kallen_bar(s, mass * mass, MH * MH))
    return phase * amplitude**2 / (32.0 * PI * mass * mass)


def sigma_v_conversion_heavy_to_light(m_heavy: float, m_light: float, portal: float) -> float:
    """Threshold B Bbar -> A Abar from -lambda_AB |A|^2 |B|^2."""
    if m_heavy <= m_light:
        return 0.0
    beta = math.sqrt(1.0 - (m_light / m_heavy) ** 2)
    return beta * portal**2 / (32.0 * PI * m_heavy * m_heavy)


def yield_equilibrium_per_charge(mass: float, temperature: float, gstar_s: float) -> float:
    z = mass / temperature
    if z > 700.0:
        return 0.0
    return 45.0 / (4.0 * PI**4) * z * z * float(kn(2, z)) / gstar_s


def collision_polynomials(
    ya: float, yb: float, ya_eq: float, yb_eq: float, rates: dict
) -> tuple[float, float]:
    """Return charge-state collision polynomials C_A,C_B before s/(Hx).

    Positive C_i depletes species i in dY_i/dx=-s C_i/(Hx).  Conversion
    cancels in C_A+C_B, as required because BBbar <-> AAbar conserves the
    total number of dark particles.
    """
    ann_a = rates["ann_A"] * (ya * ya - ya_eq * ya_eq)
    semi_a = 0.5 * rates["semi_A"] * (ya * ya - ya * ya_eq)
    ann_b = rates["ann_B"] * (yb * yb - yb_eq * yb_eq)
    semi_b = 0.5 * rates["semi_B"] * (yb * yb - yb * yb_eq)
    equilibrium_ratio_sq = (yb_eq / ya_eq) ** 2 if ya_eq > 0.0 else 0.0
    conversion = rates["conversion_B_to_A"] * (
        yb * yb - equilibrium_ratio_sq * ya * ya
    )
    return ann_a + semi_a - conversion, ann_b + semi_b + conversion


def solve_coupled_freezeout(
    params: dict,
    gstar: float = 90.0,
    x_final: float = 1.0e4,
    rate_scales: dict | None = None,
) -> dict:
    m_a, m_b = params["mA"], params["mB"]
    m_ref = m_a
    rates = {
        "ann_A_SM": sigma_v_ann_to_sm(m_a, params["lambda_HA"]),
        "ann_A_hh": sigma_v_ann_to_hh(m_a, params["lambda_HA"]),
        "semi_A": sigma_v_semi(m_a, params["lambda_HA"], params["mu_A"]),
        "ann_B_SM": sigma_v_ann_to_sm(m_b, params["lambda_HB"]),
        "ann_B_hh": sigma_v_ann_to_hh(m_b, params["lambda_HB"]),
        "semi_B": sigma_v_semi(m_b, params["lambda_HB"], params["mu_B"]),
        "conversion_B_to_A": sigma_v_conversion_heavy_to_light(
            m_b, m_a, params["lambda_AB"]
        ),
    }
    rates["ann_A"] = rates["ann_A_SM"] + rates["ann_A_hh"]
    rates["ann_B"] = rates["ann_B_SM"] + rates["ann_B_hh"]
    rate_scales = rate_scales or {}
    for key, scale in rate_scales.items():
        if key not in rates:
            raise KeyError(f"unknown rate key: {key}")
        rates[key] *= scale
    if "ann_A_SM" in rate_scales or "ann_A_hh" in rate_scales:
        rates["ann_A"] = rates["ann_A_SM"] + rates["ann_A_hh"]
    if "ann_B_SM" in rate_scales or "ann_B_hh" in rate_scales:
        rates["ann_B"] = rates["ann_B_SM"] + rates["ann_B_hh"]

    def rhs(log_x: float, y: np.ndarray) -> np.ndarray:
        x = math.exp(log_x)
        temperature = m_ref / x
        entropy = 2.0 * PI**2 / 45.0 * gstar * temperature**3
        hubble = 1.66 * math.sqrt(gstar) * temperature**2 / MPL
        prefactor = entropy / hubble  # x*dY/dx = -s/H * collision polynomial
        ya, yb = max(y[0], 0.0), max(y[1], 0.0)
        ya_eq = yield_equilibrium_per_charge(m_a, temperature, gstar)
        yb_eq = yield_equilibrium_per_charge(m_b, temperature, gstar)

        ca, cb = collision_polynomials(ya, yb, ya_eq, yb_eq, rates)
        return -prefactor * np.array([ca, cb])

    x_initial = 1.0
    t_span = (math.log(x_initial), math.log(x_final))
    temperature_initial = m_ref / x_initial
    y0 = np.array(
        [
            yield_equilibrium_per_charge(m_a, temperature_initial, gstar),
            yield_equilibrium_per_charge(m_b, temperature_initial, gstar),
        ]
    )
    solution = solve_ivp(
        rhs,
        t_span,
        y0,
        method="Radau",
        rtol=2.0e-8,
        atol=1.0e-15,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    ya, yb = solution.y[:, -1]
    omega_a = OMEGA_FACTOR * 2.0 * m_a * ya
    omega_b = OMEGA_FACTOR * 2.0 * m_b * yb
    omega_total = omega_a + omega_b
    return {
        "assumptions": {
            "yield_convention": "per charge state; antiparticle density equal",
            "tree_level": True,
            "threshold_cross_sections": True,
            "constant_gstar": gstar,
            "thermal_averaging": False,
            "higgs_width_order": "tree level; hh treated as full separate 2-to-2 amplitude",
        },
        "parameters": params,
        "rates_GeV_minus2": rates,
        "rates_cm3_s": {key: value * GEV2_TO_CM3_S for key, value in rates.items()},
        "solver": {
            "method": "Radau in log(x), x=mA/T",
            "rtol": 2.0e-8,
            "atol": 1.0e-15,
            "x_initial": x_initial,
            "x_final": x_final,
            "nfev": solution.nfev,
            "rate_scales": rate_scales,
        },
        "late_yields_per_charge": {"A": float(ya), "B": float(yb)},
        "omega_h2": {
            "A": float(omega_a),
            "B": float(omega_b),
            "total": float(omega_total),
            "fraction_A": float(omega_a / omega_total),
            "fraction_B": float(omega_b / omega_total),
        },
    }


def main() -> None:
    params = {
        "mA": 180.0,
        "mB": 400.0,
        "mu_A": 60.0,
        "mu_B": 90.0,
        "lambda_HA": 0.020,
        "lambda_HB": 0.030,
        "lambda_AB": 0.10,
    }
    nominal = solve_coupled_freezeout(params)
    m_a_bare_sq = params["mA"] ** 2 - 0.5 * params["lambda_HA"] * VEV**2
    m_b_bare_sq = params["mB"] ** 2 - 0.5 * params["lambda_HB"] * VEV**2
    max_certificate_params = dict(params)
    max_certificate_params["mu_A"] = 0.99 * math.sqrt(9.0 * 0.20 * m_a_bare_sq)
    max_certificate_params["mu_B"] = 0.99 * math.sqrt(9.0 * 0.25 * m_b_bare_sq)
    diagnostics = {
        "gstar_80": solve_coupled_freezeout(params, gstar=80.0)["omega_h2"],
        "gstar_100": solve_coupled_freezeout(params, gstar=100.0)["omega_h2"],
        "x_final_1e3": solve_coupled_freezeout(params, x_final=1.0e3)["omega_h2"],
        "x_final_1e5": solve_coupled_freezeout(params, x_final=1.0e5)["omega_h2"],
        "no_conversion": solve_coupled_freezeout(
            params, rate_scales={"conversion_B_to_A": 0.0}
        )["omega_h2"],
        "no_semiannihilation": solve_coupled_freezeout(
            params, rate_scales={"semi_A": 0.0, "semi_B": 0.0}
        )["omega_h2"],
        "all_number_changing_rates_times_2": solve_coupled_freezeout(
            params,
            rate_scales={
                "ann_A_SM": 2.0,
                "ann_A_hh": 2.0,
                "semi_A": 2.0,
                "ann_B_SM": 2.0,
                "ann_B_hh": 2.0,
                "semi_B": 2.0,
            },
        )["omega_h2"],
        "all_number_changing_rates_times_10": solve_coupled_freezeout(
            params,
            rate_scales={
                "ann_A_SM": 10.0,
                "ann_A_hh": 10.0,
                "semi_A": 10.0,
                "ann_B_SM": 10.0,
                "ann_B_hh": 10.0,
                "semi_B": 10.0,
            },
        )["omega_h2"],
        "cubics_at_99_percent_of_simple_global_certificate": {
            "parameters": max_certificate_params,
            "omega_h2": solve_coupled_freezeout(max_certificate_params)["omega_h2"],
        },
    }
    result = {"nominal": nominal, "diagnostics": diagnostics}
    output = Path(__file__).resolve().parents[1] / "audits" / "tpd_coupled_relic.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
