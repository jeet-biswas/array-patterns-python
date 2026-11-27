import random
import unittest

from arrays.closest_subset_sum_difference import closest_subset_sum_difference


class TestClosestSubsetSumDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(closest_subset_sum_difference([5, -7, 3, 5], 6), 0)
        self.assertEqual(closest_subset_sum_difference([7, -9, 15, -2], -5), 1)

    def test_edges(self):
        self.assertEqual(closest_subset_sum_difference([], -7), 7)
        self.assertEqual(closest_subset_sum_difference([0, 0], 3), 3)

    def test_against_reference(self):
        rng = random.Random(282)
        for _ in range(120):
            a = [rng.randrange(-15, 16) for _ in range(rng.randrange(14))]
            target = rng.randrange(-40, 41)
            expected = min(abs(sum(x for i, x in enumerate(a) if mask >> i & 1)-target) for mask in range(1 << len(a)))
            self.assertEqual(closest_subset_sum_difference(a, target), expected)
