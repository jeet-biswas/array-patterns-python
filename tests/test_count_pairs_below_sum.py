import random
import unittest

from arrays.count_pairs_below_sum import count_pairs_below_sum


class TestCountPairsBelowSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_pairs_below_sum([-1, 1, 2, 3, 1], 2), 3)
        self.assertEqual(count_pairs_below_sum([1, 1, 1], 3), 3)

    def test_edges(self):
        self.assertEqual(count_pairs_below_sum([], 1), 0)
        self.assertEqual(count_pairs_below_sum([1], 3), 0)
        self.assertEqual(count_pairs_below_sum([1, 2], 3), 0)
        self.assertEqual(count_pairs_below_sum([-3, -2], -4), 1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(133)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(25))]
            threshold = rng.randrange(-15, 16)
            original = values.copy()
            self.assertEqual(count_pairs_below_sum(values, threshold), sum(a+b < threshold for a, b in combinations(values, 2)))
            self.assertEqual(values, original)
