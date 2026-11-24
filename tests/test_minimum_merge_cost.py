import random
import unittest

from arrays.minimum_merge_cost import minimum_merge_cost


class TestMinimumMergeCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_merge_cost([4, 3, 2, 6]), 29)

    def test_edges(self):
        self.assertEqual(minimum_merge_cost([]), 0)
        self.assertEqual(minimum_merge_cost([5]), 0)
        self.assertEqual(minimum_merge_cost([0, 0]), 0)
        with self.assertRaises(ValueError): minimum_merge_cost([-1])

    def test_against_reference(self):
        from functools import lru_cache
        @lru_cache(None)
        def reference(weights):
            if len(weights) <= 1: return 0
            return min(weights[i]+weights[j]+reference(tuple(sorted([x for k, x in enumerate(weights) if k not in (i, j)]+[weights[i]+weights[j]]))) for i in range(len(weights)) for j in range(i+1, len(weights)))
        rng = random.Random(201)
        for _ in range(80):
            a = [rng.randrange(7) for _ in range(rng.randrange(7))]
            self.assertEqual(minimum_merge_cost(a), reference(tuple(sorted(a))))
