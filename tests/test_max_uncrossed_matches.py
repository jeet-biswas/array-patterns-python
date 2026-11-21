import random
import unittest

from arrays.max_uncrossed_matches import max_uncrossed_matches


class TestMaxUncrossedMatches(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_uncrossed_matches([1, 4, 2], [1, 2, 4]), 2)

    def test_edges(self):
        self.assertEqual(max_uncrossed_matches([], [1]), 0)
        self.assertEqual(max_uncrossed_matches([2, 2, 2], [2, 2]), 2)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(162)
        for _ in range(100):
            a = [rng.randrange(4) for _ in range(rng.randrange(8))]
            b = [rng.randrange(4) for _ in range(rng.randrange(8))]
            expected = 0
            for k in range(1, min(len(a), len(b))+1):
                if set(combinations(a, k)) & set(combinations(b, k)): expected = k
            self.assertEqual(max_uncrossed_matches(a, b), expected)
