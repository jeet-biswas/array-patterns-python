import random
import unittest

from arrays.intersect_sorted import intersect_sorted


class TestIntersectSorted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(intersect_sorted([1, 2, 2, 3], [2, 2, 2, 4]), [2, 2])
        self.assertEqual(intersect_sorted([-3, -1, 0], [-3, 0]), [-3, 0])

    def test_edges(self):
        self.assertEqual(intersect_sorted([], [1]), [])
        self.assertEqual(intersect_sorted([1], []), [])
        self.assertEqual(intersect_sorted([1, 2], [3, 4]), [])

    def test_against_multiset(self):
        from collections import Counter
        rng = random.Random(27)
        for _ in range(100):
            left = sorted(rng.randrange(-4, 5) for _ in range(rng.randrange(20)))
            right = sorted(rng.randrange(-4, 5) for _ in range(rng.randrange(20)))
            original = left.copy(), right.copy()
            self.assertEqual(intersect_sorted(left, right), sorted((Counter(left) & Counter(right)).elements()))
            self.assertEqual((left, right), original)
