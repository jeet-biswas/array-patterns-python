import random
import unittest

from arrays.minimize_max_pair_difference import minimize_max_pair_difference


class TestMinimizeMaxPairDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimize_max_pair_difference([10, 1, 2, 7, 1, 3], 2), 1)

    def test_edges(self):
        self.assertEqual(minimize_max_pair_difference([], 0), 0)
        with self.assertRaises(ValueError): minimize_max_pair_difference([1], 1)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(210)
        for _ in range(100):
            a = [rng.randrange(-7, 8) for _ in range(rng.randrange(9))]
            pairs = rng.randrange(len(a)//2+1)
            @lru_cache(None)
            def solve(s, left):
                if left == 0: return 0
                if len(s) < 2*left: return float('inf')
                best = solve(s[1:], left)
                for j in range(1, len(s)):
                    best = min(best, max(abs(s[0]-s[j]), solve(s[1:j]+s[j+1:], left-1)))
                return best
            self.assertEqual(minimize_max_pair_difference(a, pairs), solve(tuple(a), pairs))
