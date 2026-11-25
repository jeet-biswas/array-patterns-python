import random
import unittest

from arrays.minimum_adjacent_k_merge_cost import minimum_adjacent_k_merge_cost


class TestMinimumAdjacentKMergeCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_adjacent_k_merge_cost([3, 2, 4, 1], 2), 20)
        self.assertEqual(minimum_adjacent_k_merge_cost([3, 5, 1, 2, 6], 3), 25)

    def test_edges(self):
        self.assertEqual(minimum_adjacent_k_merge_cost([], 2), 0)
        self.assertIsNone(minimum_adjacent_k_merge_cost([3, 2, 4, 1], 3))
        with self.assertRaises(ValueError): minimum_adjacent_k_merge_cost([1], 1)
        with self.assertRaises(ValueError): minimum_adjacent_k_merge_cost([-1], 2)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(223)
        for _ in range(130):
            a = [rng.randrange(7) for _ in range(rng.randrange(9))]
            k = rng.randrange(2, 5)
            @lru_cache(None)
            def solve(s):
                if len(s) <= 1: return 0
                answers = []
                for i in range(len(s)-k+1):
                    merged = sum(s[i:i+k])
                    later = solve(s[:i]+(merged,)+s[i+k:])
                    if later is not None: answers.append(merged+later)
                return min(answers, default=None)
            self.assertEqual(minimum_adjacent_k_merge_cost(a, k), solve(tuple(a)))
