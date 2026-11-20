import random
import unittest

from arrays.count_pair_sums import count_pair_sums


class TestCountPairSums(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_pair_sums([1, 5, 7, -1, 5], 6), 3)
        self.assertEqual(count_pair_sums([3, 3, 3, 3], 6), 6)

    def test_edges(self):
        self.assertEqual(count_pair_sums([], 0), 0)
        self.assertEqual(count_pair_sums([3], 6), 0)
        self.assertEqual(count_pair_sums([0, 0, 0], 0), 3)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(132)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(25))]
            target = rng.randrange(-15, 16)
            self.assertEqual(count_pair_sums(values, target), sum(a+b == target for a, b in combinations(values, 2)))
