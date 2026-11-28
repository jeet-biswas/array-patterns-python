import random
import unittest

from arrays.count_pairs_xor_interval import count_pairs_xor_interval


class TestCountPairsXorInterval(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_pairs_xor_interval([1, 4, 2, 7], 2, 6), 6)

    def test_edges(self):
        self.assertEqual(count_pairs_xor_interval([0, 0, 0], 0, 0), 3)
        self.assertEqual(count_pairs_xor_interval([], 0, 10**30), 0)
        with self.assertRaises(ValueError): count_pairs_xor_interval([1], 3, 2)
        with self.assertRaises(ValueError): count_pairs_xor_interval([-1], 0, 1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(313)
        for _ in range(170):
            a = [rng.randrange(128) for _ in range(rng.randrange(35))]
            low, high = sorted((rng.randrange(200), rng.randrange(200)))
            self.assertEqual(count_pairs_xor_interval(a, low, high), sum(low <= x ^ y <= high for x, y in combinations(a, 2)))
