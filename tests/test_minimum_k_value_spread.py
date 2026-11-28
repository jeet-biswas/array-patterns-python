import random
import unittest

from arrays.minimum_k_value_spread import minimum_k_value_spread


class TestMinimumKValueSpread(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_k_value_spread([9, 4, 1, 7], 2), 2)

    def test_edges(self):
        self.assertEqual(minimum_k_value_spread([], 0), 0)
        self.assertEqual(minimum_k_value_spread([2, 2], 2), 0)
        with self.assertRaises(ValueError): minimum_k_value_spread([1], 2)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(324)
        for _ in range(150):
            a = [rng.randrange(-20, 21) for _ in range(rng.randrange(12))]
            k = rng.randrange(len(a)+1)
            expected = min((max(s)-min(s) if s else 0 for s in combinations(a, k)))
            self.assertEqual(minimum_k_value_spread(a, k), expected)
