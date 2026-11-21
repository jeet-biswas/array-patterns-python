import random
import unittest

from arrays.max_jump_score import max_jump_score


class TestMaxJumpScore(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_jump_score([1, -1, -2, 4, -7, 3], 2), 7)

    def test_edges(self):
        self.assertEqual(max_jump_score([-5], 1), -5)
        with self.assertRaises(ValueError): max_jump_score([], 1)
        with self.assertRaises(ValueError): max_jump_score([1], 0)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(149)
        for _ in range(120):
            a = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 12))]
            k = rng.randrange(1, 5)
            @lru_cache(None)
            def visit(i):
                if i == len(a)-1: return a[i]
                return a[i] + max(visit(j) for j in range(i+1, min(i+k+1, len(a))))
            self.assertEqual(max_jump_score(a, k), visit(0))
