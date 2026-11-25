import random
import unittest

from arrays.minimum_triangulation_score import minimum_triangulation_score


class TestMinimumTriangulationScore(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_triangulation_score([1, 3, 1, 4, 1, 5]), 13)

    def test_edges(self):
        self.assertEqual(minimum_triangulation_score([]), 0)
        self.assertEqual(minimum_triangulation_score([2, 3, 4]), 24)
        with self.assertRaises(ValueError): minimum_triangulation_score([-1])

    def test_against_reference(self):
        from functools import lru_cache
        @lru_cache(None)
        def clip_ears(s):
            if len(s) < 3: return 0
            if len(s) == 3: return s[0]*s[1]*s[2]
            return min(s[i-1]*s[i]*s[(i+1) % len(s)]+clip_ears(s[:i]+s[i+1:]) for i in range(len(s)))
        rng = random.Random(222)
        for _ in range(100):
            a = [rng.randrange(6) for _ in range(rng.randrange(8))]
            self.assertEqual(minimum_triangulation_score(a), clip_ears(tuple(a)))
