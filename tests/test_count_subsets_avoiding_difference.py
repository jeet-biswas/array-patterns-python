import random
import unittest

from arrays.count_subsets_avoiding_difference import count_subsets_avoiding_difference


class TestCountSubsetsAvoidingDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subsets_avoiding_difference([2, 4, 6], 2), 4)
        self.assertEqual(count_subsets_avoiding_difference([1, 1, 3], 2), 4)

    def test_edges(self):
        self.assertEqual(count_subsets_avoiding_difference([], 1), 0)
        self.assertEqual(count_subsets_avoiding_difference([-2, -2], 1), 3)
        with self.assertRaises(ValueError): count_subsets_avoiding_difference([], 0)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(285)
        for _ in range(130):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(12))]
            k = rng.randrange(1, 6)
            expected = 0
            for mask in range(1, 1 << len(a)):
                s = [x for i, x in enumerate(a) if mask >> i & 1]
                expected += all(abs(x-y) != k for x, y in combinations(s, 2))
            self.assertEqual(count_subsets_avoiding_difference(a, k), expected)
