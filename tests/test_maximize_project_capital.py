import random
import unittest

from arrays.maximize_project_capital import maximize_project_capital


class TestMaximizeProjectCapital(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximize_project_capital([0, 1, 1], [1, 2, 3], 2, 0), 4)

    def test_edges(self):
        self.assertEqual(maximize_project_capital([], [], 3, 5), 5)
        self.assertEqual(maximize_project_capital([2], [8], 1, 0), 0)
        with self.assertRaises(ValueError): maximize_project_capital([1], [], 1, 0)
        with self.assertRaises(ValueError): maximize_project_capital([0], [-1], 1, 0)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(202)
        for _ in range(100):
            n = rng.randrange(8)
            required = [rng.randrange(10) for _ in range(n)]
            profits = [rng.randrange(7) for _ in range(n)]
            k, initial = rng.randrange(5), rng.randrange(5)
            @lru_cache(None)
            def solve(mask, capital, left):
                best = capital
                if left:
                    for i in range(n):
                        if not mask >> i & 1 and required[i] <= capital:
                            best = max(best, solve(mask | (1 << i), capital+profits[i], left-1))
                return best
            self.assertEqual(maximize_project_capital(required, profits, k, initial), solve(0, initial, k))
