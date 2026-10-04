#!/usr/bin/env python3
"""Regression tests for the TP-D electroweak vacuum, RGEs, and unitarity."""

from __future__ import annotations

import math
import unittest
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np

import tpd_ew_vacuum as vacuum
import tpd_dimensionful_rge as dimensionful_rge
import tpd_finite_energy_unitarity as finite
import tpd_full_rge_running as full_running
import tpd_gauge_origin_audit as gauge_origin
import tpd_gauge_high_energy_unitarity as gauge_unitarity
import tpd_gauge_vacuum as gauge_vacuum
import tpd_high_energy_unitarity as unitarity
import tpd_parent_gauge_rge as parent_gauge_rge
import tpd_parent_gauge_finite_energy as parent_gauge_finite
import tpd_parent_extra_state_cosmology as parent_cosmology
import tpd_parent_rge_running as parent_running
import tpd_parent_scalar_rge as parent_scalar_rge
import tpd_phenomenology_prefilter as pheno_prefilter
import tpd_coupled_relic as coupled_relic
import tpd_coupled_relic_crosscheck as coupled_relic_crosscheck
import tpd_cubic_metastability as cubic_metastability
import tpd_direct_detection_gate as direct_detection
import tpd_electroweak_gauge_unitarity as ew_gauge
import tpd_higgs_pole_diagnostic as higgs_pole
import tpd_scalar_rge as rge
import tpd_soft_breaking_sum_rule as soft_sum_rule
import finite_energy_unitarity as finite_engine


def benchmark(portal: float = 0.02) -> vacuum.Parameters:
    v, mh = 246.22, 125.25
    lambda_h = mh**2 / (2 * v**2)
    lambda_ha = portal
    lambda_hb = 0.03 if portal == 0.02 else portal
    return vacuum.Parameters(
        mu_h2=lambda_h * v**2,
        m_a2=180.0**2 - 0.5 * lambda_ha * v**2,
        m_b2=400.0**2 - 0.5 * lambda_hb * v**2,
        mu_a=60.0,
        mu_b=90.0,
        lambda_h=lambda_h,
        lambda_a=0.20,
        lambda_b=0.25,
        lambda_ha=lambda_ha,
        lambda_hb=lambda_hb,
        lambda_ab=0.10,
    )


class ElectroweakVacuumTests(unittest.TestCase):
    def test_stationarity_and_physical_radial_masses(self) -> None:
        p = benchmark()
        ew = np.array([246.22, 0.0, 0.0])
        self.assertLess(np.linalg.norm(vacuum.gradient(ew, p), ord=np.inf), 1e-8)
        expected = np.array([125.25**2, 180.0**2, 400.0**2])
        actual = np.linalg.eigvalsh(vacuum.hessian(ew, p))
        np.testing.assert_allclose(actual, expected, rtol=1e-12, atol=1e-8)

    def test_exact_copositivity_and_global_sufficient_conditions(self) -> None:
        p = benchmark()
        self.assertTrue(vacuum.copositive_bfb(p)["passes"])
        self.assertTrue(all(vacuum.sufficient_global_ew(p).values()))


class ScalarRGETests(unittest.TestCase):
    def test_independent_exact_derivations_agree(self) -> None:
        rge.build_potential()
        self.assertEqual(rge.projections_tensor(), rge.projections_hessian())

    def test_decoupled_o4_and_o2_limits(self) -> None:
        rge.build_potential()
        betas = rge.projections_tensor()
        self.assertEqual(betas["lambda_H"][("lambda_H", "lambda_H")], 24)
        self.assertEqual(betas["lambda_A"][("lambda_A", "lambda_A")], 20)
        self.assertEqual(betas["lambda_B"][("lambda_B", "lambda_B")], 20)

    def test_dimensionful_independent_derivations_and_z3_structure(self) -> None:
        potential = dimensionful_rge.build_potential()
        effective = dimensionful_rge.project_effective(
            dimensionful_rge.effective_beta_potential(potential)
        )
        tensors = dimensionful_rge.project_tensors(potential)
        self.assertEqual(effective, tensors)
        self.assertEqual(tensors["kA"], {("kA", "lambda_A"): 12})
        self.assertEqual(tensors["kB"], {("kB", "lambda_B"): 12})
        self.assertEqual(tensors["mA2"][("kA", "kA")], 8)

    def test_full_running_dimensionful_normalization(self) -> None:
        p = finite.benchmark()
        dimensionless_initial = {
            "g1": 0.3583, "g2": 0.6478, "g3": 1.1666,
            "yt": 0.9369, "yb": 0.0164, "ytau": 0.0102,
            "lambda_H": p.lambda_h, "lambda_A": p.lambda_a,
            "lambda_B": p.lambda_b, "lambda_HA": p.lambda_ha,
            "lambda_HB": p.lambda_hb, "lambda_AB": p.lambda_ab,
            "muH2": p.mu_h2, "mA2": p.m_a2, "mB2": p.m_b2,
            "muA": p.mu_a, "muB": p.mu_b,
        }
        vector = np.array([dimensionless_initial[name] for name in full_running.NAMES])
        beta = dict(zip(full_running.NAMES, full_running.beta_numerator(vector)))
        expected_m_a = (
            8 * p.lambda_a * p.m_a2 + 2 * p.lambda_ab * p.m_b2
            - 4 * p.lambda_ha * p.mu_h2 + 4 * p.mu_a**2
        )
        self.assertAlmostEqual(beta["mA2"], expected_m_a, places=9)


class HighEnergyUnitarityTests(unittest.TestCase):
    def test_tensor_matrix_matches_analytic_spectrum(self) -> None:
        rge.build_potential()
        p = benchmark()
        couplings = {
            "lambda_H": p.lambda_h,
            "lambda_A": p.lambda_a,
            "lambda_B": p.lambda_b,
            "lambda_HA": p.lambda_ha,
            "lambda_HB": p.lambda_hb,
            "lambda_AB": p.lambda_ab,
        }
        direct = np.linalg.eigvalsh(unitarity.matrix(couplings))
        predicted = unitarity.analytic_spectrum(couplings)
        np.testing.assert_allclose(direct, predicted, rtol=1e-12, atol=1e-12)
        self.assertLess(np.max(np.abs(direct)), 8 * math.pi)


class FiniteEnergyUnitarityTests(unittest.TestCase):
    def test_inert_spectrum_and_angular_integration(self) -> None:
        data = finite.tensors(finite.benchmark())
        masses = data["masses"]
        np.testing.assert_allclose(
            masses[list(finite.PHYSICAL)],
            [125.25, 180.0, 180.0, 400.0, 400.0],
            rtol=1e-12,
            atol=1e-10,
        )
        channels = list(combinations_with_replacement(finite.PHYSICAL, 2))
        analytic = finite_engine.partial_wave_matrix_analytic(
            3000.0, channels, masses, data["cubic"], data["quartic"]
        )
        numeric = finite_engine.partial_wave_matrix(
            3000.0, channels, masses, data["cubic"], data["quartic"], 192
        )
        np.testing.assert_allclose(analytic, numeric, rtol=1e-10, atol=1e-12)


class GaugeOriginTests(unittest.TestCase):
    def test_complete_scalar_invariant_counts(self) -> None:
        operators = gauge_origin.invariants()
        self.assertEqual(len(operators["1"]), 0)
        self.assertEqual(len(operators["2"]), 4)
        self.assertEqual(len(operators["3"]), 0)
        self.assertEqual(len(operators["4"]), 14)
        labels = {row["monomial"] for row in operators["4"]}
        self.assertIn("Phi_m_dag A^3", labels)
        self.assertIn("Phi_E_dag B^3", labels)

    def test_kinetic_mixing_mass_formula(self) -> None:
        for mm2, me2, epsilon in ((9.0, 25.0, 0.0), (9.0, 25.0, 0.3), (100.0, 3.0, -0.7)):
            predicted = gauge_origin.analytic_mass_eigenvalues(mm2, me2, epsilon)
            direct = gauge_origin.numerical_mass_eigenvalues(mm2, me2, epsilon)
            np.testing.assert_allclose(predicted, direct, rtol=1e-12, atol=1e-12)

    def test_parent_sector_vacuum_certificates(self) -> None:
        f = 1000.0
        first = gauge_vacuum.sector_audit(
            "m", f, 0.20, 180.0**2 - 0.01 * 246.22**2,
            0.20, math.sqrt(2) * 60.0 / (3 * f)
        )
        second = gauge_vacuum.sector_audit(
            "E", f, 0.20, 400.0**2 - 0.015 * 246.22**2,
            0.25, math.sqrt(2) * 90.0 / (3 * f)
        )
        self.assertTrue(first["global_sector_vacuum_certified"])
        self.assertTrue(second["global_sector_vacuum_certified"])
        self.assertEqual(first["positive_interior_stationary_points"], [])
        self.assertEqual(second["positive_interior_stationary_points"], [])

    def test_parent_high_energy_matrix_contains_low_energy_matrix(self) -> None:
        v, mh, f = 246.22, 125.25, 1000.0
        couplings = {
            "lambda_H": mh**2 / (2 * v**2),
            "lambda_A": 0.20, "lambda_B": 0.25,
            "lambda_HA": 0.020, "lambda_HB": 0.030, "lambda_AB": 0.10,
            "lambda_Phi_m": 0.20, "lambda_Phi_E": 0.20,
            "kappa_m": math.sqrt(2) * 60.0 / (3 * f),
            "kappa_E": math.sqrt(2) * 90.0 / (3 * f),
        }
        parent = gauge_unitarity.matrix(couplings)
        positions = [position for position, pair in enumerate(gauge_unitarity.PAIRS) if pair[1] < 8]
        principal = parent[np.ix_(positions, positions)]
        rge.build_potential()
        low = unitarity.matrix({name: couplings[name] for name in rge.NAMES})
        np.testing.assert_allclose(principal, low, rtol=1e-13, atol=1e-13)
        self.assertLess(np.max(np.abs(np.linalg.eigvalsh(parent))), 8 * math.pi)

    def test_parent_scalar_rge_independent_projections(self) -> None:
        poly = parent_scalar_rge.potential()
        projected = parent_scalar_rge.project_hessian(
            parent_scalar_rge.beta_potential(poly)
        )
        self.assertTrue(all(parent_scalar_rge.tensor_cross_checks(poly, projected).values()))
        self.assertEqual(
            projected["lambda_APhi_m"][("kappa_m", "kappa_m")], 36
        )
        self.assertEqual(
            projected["lambda_BPhi_E"][("kappa_E", "kappa_E")], 36
        )

    def test_parent_factorized_portals_are_radiatively_generated(self) -> None:
        point = parent_running.initial_point()
        vector = np.array([point[name] for name in parent_running.NAMES])
        beta = dict(zip(parent_running.NAMES, parent_running.beta_numerator(vector)))
        self.assertGreater(beta["lambda_APhi_m"], 0)
        self.assertGreater(beta["lambda_BPhi_E"], 0)
        expected_m = 36 * point["kappa_m"]**2 + 108 * point["g_m"]**4
        expected_e = 36 * point["kappa_E"]**2 + 108 * point["g_E"]**4
        self.assertAlmostEqual(beta["lambda_APhi_m"], expected_m, places=12)
        self.assertAlmostEqual(beta["lambda_BPhi_E"], expected_e, places=12)

    def test_parent_abelian_gauge_coefficients(self) -> None:
        terms = parent_gauge_rge.gauge_terms()
        self.assertEqual(terms["lambda_APhi_m"], "-60*g_m^2*lambda_APhi_m + 108*g_m^4")
        self.assertEqual(terms["kappa_m"], "-36*g_m^2*kappa_m")


class PhenomenologyPrefilterTests(unittest.TestCase):
    def test_kernel_forbidden_decay_is_kinematically_open(self) -> None:
        coefficient = pheno_prefilter.generic_offdiagonal_width_coefficient(
            400.0, 180.0, 125.25, 246.22
        )
        self.assertGreater(coefficient, 0)
        self.assertAlmostEqual(coefficient, 1.9302394118070445, places=12)

    def test_soft_breaking_sum_rule_and_generic_residual(self) -> None:
        theta, la, lb, eta, v = 0.21, 0.02, 0.03, 0.004, 246.22
        matrix = soft_sum_rule.higgs_matrix(theta, la, lb, eta, v)
        self.assertAlmostEqual(
            soft_sum_rule.residual(theta, matrix), 2 * v * eta, places=12
        )
        minimal = soft_sum_rule.higgs_matrix(theta, la, lb, 0.0, v)
        self.assertAlmostEqual(soft_sum_rule.residual(theta, minimal), 0.0, places=12)

    def test_parent_E_radial_has_no_frozen_tree_decay(self) -> None:
        self.assertLess(632.4555320336759, 2 * 400.0)
        self.assertLess(632.4555320336759, 3 * 400.0)
        self.assertLess(632.4555320336759, 2 * 900.0)

    def test_coupled_collision_terms_obey_detailed_balance(self) -> None:
        rates = {
            "ann_A": 1.1,
            "semi_A": 0.7,
            "ann_B": 0.4,
            "semi_B": 0.2,
            "conversion_B_to_A": 2.3,
        }
        ca, cb = coupled_relic.collision_polynomials(0.03, 0.007, 0.03, 0.007, rates)
        self.assertAlmostEqual(ca, 0.0, places=16)
        self.assertAlmostEqual(cb, 0.0, places=16)

    def test_conversion_conserves_total_dark_particle_number(self) -> None:
        rates = {
            "ann_A": 0.0,
            "semi_A": 0.0,
            "ann_B": 0.0,
            "semi_B": 0.0,
            "conversion_B_to_A": 2.3,
        }
        ca, cb = coupled_relic.collision_polynomials(0.02, 0.009, 0.03, 0.007, rates)
        self.assertAlmostEqual(ca + cb, 0.0, places=16)

    def test_b0_leading_relic_diagnostic_overcloses(self) -> None:
        params = {
            "mA": 180.0, "mB": 400.0, "mu_A": 60.0, "mu_B": 90.0,
            "lambda_HA": 0.020, "lambda_HB": 0.030, "lambda_AB": 0.10,
        }
        result = coupled_relic.solve_coupled_freezeout(params, x_final=1.0e3)
        self.assertGreater(result["omega_h2"]["total"], 1.0)

    def test_total_yield_relic_crosscheck(self) -> None:
        params = {
            "mA": 180.0, "mB": 400.0, "mu_A": 60.0, "mu_B": 90.0,
            "lambda_HA": 0.020, "lambda_HB": 0.030, "lambda_AB": 0.10,
        }
        per_charge = coupled_relic.solve_coupled_freezeout(params, x_final=1.0e3)
        total = coupled_relic_crosscheck.solve_total_yields(params, x_final=1.0e3)
        relative = abs(
            total["omega_h2"]["total"] / per_charge["omega_h2"]["total"] - 1.0
        )
        self.assertLess(relative, 3.0e-5)

    def test_lz_vector_curve_calibration(self) -> None:
        anchors = direct_detection.lz_curve_anchors()
        interpolated = direct_detection.loglog_interpolate(40.0, anchors)
        self.assertLess(abs(interpolated / 2.2e-48 - 1.0), 0.02)

    def test_four_relic_scan_points_fail_direct_detection(self) -> None:
        root = Path(__file__).resolve().parents[1]
        payload = direct_detection.build_payload(
            root / "audits" / "tpd_relic_parameter_scan.json"
        )
        self.assertEqual(payload["gate_summary"]["points_tested"], 4)
        self.assertEqual(payload["gate_summary"]["points_excluded"], 4)
        self.assertGreater(payload["gate_summary"]["minimum_excluding_R"], 30.0)

    def test_higgs_pole_narrow_width_against_finite_width(self) -> None:
        for mass in (62.0, 62.2):
            nwa = higgs_pole.sigma_v_nwa_unit_portal(mass, 20.0)
            finite = higgs_pole.sigma_v_finite_width_unit_portal(mass, 20.0)
            self.assertLess(abs(nwa / finite - 1.0), 0.002)
        self.assertGreater(higgs_pole.sigma_v_finite_width_unit_portal(62.0, 1000.0), 0.0)

    def test_pole_candidate_electroweak_vector_unitarity(self) -> None:
        pole_json = Path(__file__).resolve().parents[1] / "audits" / "tpd_higgs_pole_diagnostic.json"
        payload = ew_gauge.build_payload(pole_json, points=120, energy_max=2.0e4)
        self.assertTrue(payload["scan"]["passes"])
        self.assertLess(
            payload["scan"]["maximum_portal_induced_singular_value"]["singular_value"],
            1.0e-3,
        )
        for vector_rows in payload["goldstone_equivalence_at_maximum_energy"].values():
            for row in vector_rows.values():
                self.assertLess(row["absolute_identity_residual"], 1.0e-12)

    def test_parent_gauge_point_matched_core_blocks(self) -> None:
        block = parent_gauge_finite.j0_block(2.0e4, 62.0, 0.10)
        self.assertLess(float(np.max(np.abs(np.linalg.eigvalsh(block.real)))), 0.25)
        charged, _labels = parent_gauge_finite.charged_partial_wave_matrix(
            2.0e4, 62.0, 0
        )
        self.assertLess(float(np.max(np.abs(np.linalg.eigvalsh(charged.real)))), 0.10)
        self.assertAlmostEqual(
            parent_gauge_finite.wigner_d(1, 0, 0, 0.73),
            math.cos(0.73),
            places=13,
        )
        ward_in = parent_gauge_finite.amp_xs_to_xs(
            2500.0, 0.2, 62.0, (0, 1), replace_incoming_by_momentum=True
        )
        ward_out = parent_gauge_finite.amp_xs_to_xs(
            2500.0, 0.2, 62.0, (1, 0), replace_outgoing_by_momentum=True
        )
        self.assertLess(abs(ward_in), 1.0e-10)
        self.assertLess(abs(ward_out), 1.0e-10)

    def test_pole_cubic_rates_and_point_matched_running(self) -> None:
        root = Path(__file__).resolve().parents[1]
        payload = cubic_metastability.build_payload(
            root / "audits" / "tpd_higgs_pole_diagnostic.json"
        )
        self.assertFalse(
            payload["cubic_processes"]["semiannihilation_SS_to_Sbar_h"]["A_open"]
        )
        self.assertLess(
            payload["cubic_processes"]["maximum_rate_over_Hubble"], 1.0e-6
        )
        self.assertGreater(
            payload["one_loop_metastability_estimate"]
            ["bounce_action_8pi2_over_3abs_lambda"],
            400.0,
        )
        self.assertTrue(
            payload["one_loop_metastability_estimate"]
            ["cosmological_lifetime_safe_in_this_approximation"]
        )

    def test_pole_parent_extra_states_decay_before_bbn(self) -> None:
        root = Path(__file__).resolve().parents[1]
        payload = parent_cosmology.build_payload(
            root / "audits" / "tpd_pole_thermal_certification.json"
        )
        for sector in payload["extra_state_decays"].values():
            self.assertLess(sector["vector"]["lifetime_s"], 1.0e-10)
            self.assertTrue(sector["radial"]["open"])
            self.assertLess(sector["radial"]["lifetime_s"], 1.0e-10)
        self.assertLess(payload["late_time_annihilation"]["ratio_to_limit"], 0.01)


if __name__ == "__main__":
    unittest.main()
