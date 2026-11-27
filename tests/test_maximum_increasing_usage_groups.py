import random
import unittest

from arrays.maximum_increasing_usage_groups import maximum_increasing_usage_groups


class TestMaximumIncreasingUsageGroups(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximum_increasing_usage_groups([1, 2, 5]), 3)

    def test_edges(self):
        self.assertEqual(maximum_increasing_usage_groups([]), 0)
        self.assertEqual(maximum_increasing_usage_groups([0, 0, 10]), 1)
        with self.assertRaises(ValueError): maximum_increasing_usage_groups([-1])

    def test_against_reference(self):
        from itertools import combinations
        from functools import lru_cache
        @lru_cache(None)
        def feasible(capacities, size):
            if size == 0: return True
            available = [i for i, x in enumerate(capacities) if x]
            for members in combinations(available, size):
                following = list(capacities)
                for i in members: following[i] -= 1
                if feasible(tuple(sorted(following)), size-1): return True
            return False
        rng = random.Random(276)
        for _ in range(130):
            a = [rng.randrange(5) for _ in range(rng.randrange(7))]
            expected = max(k for k in range(len(a)+1) if feasible(tuple(sorted(a)), k))
            self.assertEqual(maximum_increasing_usage_groups(a), expected)
