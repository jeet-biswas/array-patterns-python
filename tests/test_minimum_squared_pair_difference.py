import random
import unittest

from arrays.minimum_squared_pair_difference import minimum_squared_pair_difference


class TestMinimumSquaredPairDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_squared_pair_difference([1, 2, 3, 4], [2, 10, 20, 19], 0), 579)
        self.assertEqual(minimum_squared_pair_difference([1, 4, 10, 12], [5, 8, 6, 9], 2), 43)

    def test_edges(self):
        self.assertEqual(minimum_squared_pair_difference([], [], 3), 0)
        self.assertEqual(minimum_squared_pair_difference([1], [3], 10), 0)
        with self.assertRaises(ValueError): minimum_squared_pair_difference([1], [], 0)
        with self.assertRaises(ValueError): minimum_squared_pair_difference([], [], -1)

    def test_against_reference(self):
        from functools import lru_cache
        @lru_cache(None)
        def solve(differences, remaining):
            best = sum(d*d for d in differences)
            if remaining:
                for i, d in enumerate(differences):
                    if d:
                        following = list(differences)
                        following[i] -= 1
                        best = min(best, solve(tuple(sorted(following)), remaining-1))
            return best
        rng = random.Random(319)
        for _ in range(100):
            n = rng.randrange(7)
            a = [rng.randrange(-3, 4) for _ in range(n)]
            b = [rng.randrange(-3, 4) for _ in range(n)]
            budget = rng.randrange(9)
            expected = solve(tuple(sorted(abs(x-y) for x, y in zip(a, b))), budget)
            self.assertEqual(minimum_squared_pair_difference(a, b, budget), expected)
