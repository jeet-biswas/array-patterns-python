import random
import unittest

from arrays.count_pairs_difference import count_pairs_difference


class TestCountPairsDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_pairs_difference([1, 2, 2, 1], 1), 4)
        self.assertEqual(count_pairs_difference([1, 3, 5, 7], 2), 3)

    def test_edges(self):
        self.assertEqual(count_pairs_difference([], 0), 0)
        self.assertEqual(count_pairs_difference([2, 2, 2], 0), 3)
        self.assertEqual(count_pairs_difference([-2, 0, 2], 2), 2)
        with self.assertRaises(ValueError):
            count_pairs_difference([1], -1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(131)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(25))]
            difference = rng.randrange(10)
            self.assertEqual(count_pairs_difference(values, difference), sum(abs(a-b) == difference for a, b in combinations(values, 2)))
