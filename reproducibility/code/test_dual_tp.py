#!/usr/bin/env python3
"""Regression tests for the TP-D Phase-II calculations."""

from __future__ import annotations

import math
import unittest

import numpy as np

import dual_tp_operator_enumerator as operators
import dual_tp_validation as validation


class DualTPOperatorTests(unittest.TestCase):
    def test_complete_counts_by_dimension(self):
        rows = operators.enumerate_nonderivative()
        counts = {
            dimension: sum(row.dimension == dimension for row in rows)
            for dimension in range(1, 5)
        }
        self.assertEqual(counts, {1: 0, 2: 3, 3: 4, 4: 6})

    def test_comparator_only_counts(self):
        rows = operators.enumerate_nonderivative()
        counts = {
            dimension: sum(row.dimension == dimension and row.comparator_only for row in rows)
            for dimension in range(1, 5)
        }
        self.assertEqual(counts, {1: 0, 2: 1, 3: 2, 4: 3})

    def test_dual_subset_is_projected_invariant(self):
        for row in operators.enumerate_nonderivative():
            if row.dual_z3:
                self.assertEqual(row.q_p, 0)


class DualTPUnitarityTests(unittest.TestCase):
    def test_analytic_spectrum_random_points(self):
        rng = np.random.default_rng(1701)
        for _ in range(100):
            la, lb, lab = rng.uniform(-1.0, 1.0, size=3)
            _, _, matrix = validation.unitarity_matrix(la, lb, lab)
            numeric = np.linalg.eigvalsh(matrix)
            radical = math.sqrt(4 * (la - lb) ** 2 + lab**2)
            analytic = np.sort(
                np.array(
                    [
                        *([2 * la] * 2),
                        *([2 * lb] * 2),
                        *([lab] * 4),
                        2 * (la + lb) - radical,
                        2 * (la + lb) + radical,
                    ]
                )
            )
            self.assertTrue(np.allclose(numeric, analytic, rtol=1e-12, atol=1e-12))

    def test_mass_formula_random_points(self):
        rng = np.random.default_rng(2718)
        for _ in range(100):
            ma2, mb2 = rng.uniform(1.0, 1e6, size=2)
            dre, dim = rng.uniform(-1e4, 1e4, size=2)
            result = validation.mass_mixing(ma2, mb2, dre, dim)
            self.assertLess(result["max_abs_difference"], 1e-8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
