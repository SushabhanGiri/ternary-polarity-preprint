#!/usr/bin/env python3
"""Independent total-yield cross-check of the TP-D freeze-out normalization."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import tpd_coupled_relic as primary


def solve_total_yields(params: dict, gstar: float = 90.0, x_final: float = 1.0e4) -> dict:
    m_a, m_b = params["mA"], params["mB"]
    rates = {
        "ann_A": primary.sigma_v_ann_to_sm(m_a, params["lambda_HA"])
        + primary.sigma_v_ann_to_hh(m_a, params["lambda_HA"]),
        "semi_A": primary.sigma_v_semi(m_a, params["lambda_HA"], params["mu_A"]),
        "ann_B": primary.sigma_v_ann_to_sm(m_b, params["lambda_HB"])
        + primary.sigma_v_ann_to_hh(m_b, params["lambda_HB"]),
        "semi_B": primary.sigma_v_semi(m_b, params["lambda_HB"], params["mu_B"]),
        "conversion": primary.sigma_v_conversion_heavy_to_light(
            m_b, m_a, params["lambda_AB"]
        ),
    }

    def rhs(log_x: float, total_yields: np.ndarray) -> np.ndarray:
        x = math.exp(log_x)
        temperature = m_a / x
        entropy = 2.0 * math.pi**2 / 45.0 * gstar * temperature**3
        hubble = 1.66 * math.sqrt(gstar) * temperature**2 / primary.MPL
        total_a, total_b = np.maximum(total_yields, 0.0)
        eq_a = 2.0 * primary.yield_equilibrium_per_charge(m_a, temperature, gstar)
        eq_b = 2.0 * primary.yield_equilibrium_per_charge(m_b, temperature, gstar)
        ratio_sq = (eq_b / eq_a) ** 2 if eq_a > 0.0 else 0.0

        annihilation_a = 0.5 * rates["ann_A"] * (total_a**2 - eq_a**2)
        semi_a = 0.25 * rates["semi_A"] * (total_a**2 - total_a * eq_a)
        annihilation_b = 0.5 * rates["ann_B"] * (total_b**2 - eq_b**2)
        semi_b = 0.25 * rates["semi_B"] * (total_b**2 - total_b * eq_b)
        conversion = 0.5 * rates["conversion"] * (
            total_b**2 - ratio_sq * total_a**2
        )
        return -(entropy / hubble) * np.array(
            [annihilation_a + semi_a - conversion, annihilation_b + semi_b + conversion]
        )

    initial_temperature = m_a
    initial = np.array(
        [
            2.0 * primary.yield_equilibrium_per_charge(m_a, initial_temperature, gstar),
            2.0 * primary.yield_equilibrium_per_charge(m_b, initial_temperature, gstar),
        ]
    )
    solution = solve_ivp(
        rhs,
        (0.0, math.log(x_final)),
        initial,
        method="BDF",
        rtol=5.0e-9,
        atol=2.0e-16,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    total_a, total_b = solution.y[:, -1]
    return {
        "method": "independent total-yield convention; BDF in log(x)",
        "late_total_yields": {"A_plus_Abar": float(total_a), "B_plus_Bbar": float(total_b)},
        "omega_h2": {
            "A": float(primary.OMEGA_FACTOR * m_a * total_a),
            "B": float(primary.OMEGA_FACTOR * m_b * total_b),
            "total": float(primary.OMEGA_FACTOR * (m_a * total_a + m_b * total_b)),
        },
        "nfev": solution.nfev,
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
    independent = solve_total_yields(params)
    first = primary.solve_coupled_freezeout(params)
    independent["relative_difference_from_primary_total"] = (
        independent["omega_h2"]["total"] / first["omega_h2"]["total"] - 1.0
    )
    output = Path(__file__).resolve().parents[1] / "audits" / "tpd_coupled_relic_crosscheck.json"
    output.write_text(json.dumps(independent, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(independent, indent=2))


if __name__ == "__main__":
    main()
