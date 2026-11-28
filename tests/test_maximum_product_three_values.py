import random
import unittest

from arrays.maximum_product_three_values import maximum_product_three_values


class TestMaximumProductThreeValues(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximum_product_three_values([-10, -10, 1, 3, 2]), 300)

    def test_edges(self):
        self.assertEqual(maximum_product_three_values([-5, -4, -3]), -60)
        self.assertEqual(maximum_product_three_values([0, 0, 0]), 0)
        with self.assertRaises(ValueError): maximum_product_three_values([1, 2])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(320)
        for _ in range(180):
            a = [rng.randrange(-20, 21) for _ in range(rng.randrange(3, 20))]
            self.assertEqual(maximum_product_three_values(a), max(x*y*z for x, y, z in combinations(a, 3)))
