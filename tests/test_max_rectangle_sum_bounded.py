import random
import unittest

from arrays.max_rectangle_sum_bounded import max_rectangle_sum_bounded


class TestMaxRectangleSumBounded(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_rectangle_sum_bounded([[1, 0, 1], [0, -2, 3]], 2), 2)

    def test_edges(self):
        self.assertIsNone(max_rectangle_sum_bounded([[5]], 4))
        self.assertIsNone(max_rectangle_sum_bounded([], 0))
        self.assertEqual(max_rectangle_sum_bounded([[-5, -2]], -3), -5)
        with self.assertRaises(ValueError): max_rectangle_sum_bounded([[1], []], 0)

    def test_against_reference(self):
        rng = random.Random(239)
        for _ in range(100):
            r, c = rng.randrange(5), rng.randrange(5)
            a = [[rng.randrange(-5, 6) for _ in range(c)] for _ in range(r)]
            limit = rng.randrange(-7, 8)
            sums = [sum(a[i][j] for i in range(top, bottom) for j in range(left, right)) for top in range(r) for bottom in range(top+1, r+1) for left in range(c) for right in range(left+1, c+1)]
            self.assertEqual(max_rectangle_sum_bounded(a, limit), max((s for s in sums if s <= limit), default=None))
