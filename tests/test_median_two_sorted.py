import random
import unittest

from arrays.median_two_sorted import median_two_sorted


class TestMedianTwoSorted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(median_two_sorted([1, 3], [2]), 2.0)
        self.assertEqual(median_two_sorted([1, 2], [3, 4]), 2.5)

    def test_edges(self):
        self.assertEqual(median_two_sorted([], [-3, -1]), -2.0)
        self.assertEqual(median_two_sorted([0, 0], [0]), 0.0)
        with self.assertRaises(ValueError):
            median_two_sorted([], [])

    def test_against_reference(self):
        from statistics import median
        rng = random.Random(52)
        for _ in range(150):
            left = sorted(rng.randrange(-15, 16) for _ in range(rng.randrange(20)))
            right = sorted(rng.randrange(-15, 16) for _ in range(rng.randrange(1, 20)))
            original = left.copy(), right.copy()
            self.assertEqual(median_two_sorted(left, right), median(left+right))
            self.assertEqual((left, right), original)
