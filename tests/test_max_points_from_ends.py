import random
import unittest

from arrays.max_points_from_ends import max_points_from_ends


class TestMaxPointsFromEnds(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_points_from_ends([1, 2, 3, 4, 5, 6, 1], 3), 12)
        self.assertEqual(max_points_from_ends([-5, -1, -3], 2), -4)

    def test_edges(self):
        self.assertEqual(max_points_from_ends([], 0), 0)
        self.assertEqual(max_points_from_ends([2, 3], 2), 5)
        self.assertEqual(max_points_from_ends([2, 3], 0), 0)
        for k in (-1, 3):
            with self.assertRaises(ValueError):
                max_points_from_ends([1, 2], k)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(120)
        for _ in range(100):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(15))]
            k = rng.randrange(len(values)+1)
            @lru_cache(None)
            def choose(start, stop, remaining):
                if remaining == 0:
                    return 0
                return max(values[start]+choose(start+1, stop, remaining-1),
                           values[stop-1]+choose(start, stop-1, remaining-1))
            self.assertEqual(max_points_from_ends(values, k), choose(0, len(values), k))
