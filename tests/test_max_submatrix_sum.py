import random
import unittest

from arrays.max_submatrix_sum import max_submatrix_sum


class TestMaxSubmatrixSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_submatrix_sum([[1, -2], [3, 4]]), 7)

    def test_edges(self):
        self.assertIsNone(max_submatrix_sum([]))
        self.assertEqual(max_submatrix_sum([[-5, -2], [-3, -7]]), -2)
        with self.assertRaises(ValueError): max_submatrix_sum([[1], []])

    def test_against_reference(self):
        rng = random.Random(238)
        for _ in range(100):
            r, c = rng.randrange(6), rng.randrange(6)
            a = [[rng.randrange(-5, 6) for _ in range(c)] for _ in range(r)]
            expected = max((sum(a[i][j] for i in range(top, bottom) for j in range(left, right)) for top in range(r) for bottom in range(top+1, r+1) for left in range(c) for right in range(left+1, c+1)), default=None)
            self.assertEqual(max_submatrix_sum(a), expected)
