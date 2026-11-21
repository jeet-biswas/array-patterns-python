import random
import unittest

from arrays.min_climbing_cost import min_climbing_cost


class TestMinClimbingCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_climbing_cost([10, 15, 20]), 15)

    def test_edges(self):
        self.assertEqual(min_climbing_cost([]), 0)
        self.assertEqual(min_climbing_cost([7]), 0)
        with self.assertRaises(ValueError): min_climbing_cost([-1])

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(148)
        for _ in range(130):
            a = [rng.randrange(10) for _ in range(rng.randrange(12))]
            @lru_cache(None)
            def visit(i):
                if i >= len(a): return 0
                return a[i] + min(visit(i+1), visit(i+2))
            self.assertEqual(min_climbing_cost(a), min(visit(0), visit(1)))
