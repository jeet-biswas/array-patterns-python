import random
import unittest

from arrays.merge_sorted import merge_sorted


class TestMergeSorted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(merge_sorted([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted([1, 1], [1]), [1, 1, 1])

    def test_edges(self):
        self.assertEqual(merge_sorted([], []), [])
        self.assertEqual(merge_sorted([], [-1, 2]), [-1, 2])
        self.assertEqual(merge_sorted([2], []), [2])

    def test_against_sort(self):
        rng = random.Random(6)
        for _ in range(100):
            left = sorted(rng.randrange(-5, 6) for _ in range(rng.randrange(15)))
            right = sorted(rng.randrange(-5, 6) for _ in range(rng.randrange(15)))
            originals = left.copy(), right.copy()
            self.assertEqual(merge_sorted(left, right), sorted(left + right))
            self.assertEqual((left, right), originals)
