import random
import unittest

from arrays.matrix_block_sums import matrix_block_sums


class TestMatrixBlockSums(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(matrix_block_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [[12, 21, 16], [27, 45, 33], [24, 39, 28]])

    def test_edges(self):
        self.assertEqual(matrix_block_sums([[], []], 2), [[], []])
        self.assertEqual(matrix_block_sums([[2, -1]], 0), [[2, -1]])
        with self.assertRaises(ValueError): matrix_block_sums([], -1)
        with self.assertRaises(ValueError): matrix_block_sums([[1], []], 1)

    def test_against_reference(self):
        rng = random.Random(245)
        for _ in range(120):
            r, c, k = rng.randrange(8), rng.randrange(8), rng.randrange(10)
            a = [[rng.randrange(-5, 6) for _ in range(c)] for _ in range(r)]
            expected = [[sum(a[x][y] for x in range(r) for y in range(c) if abs(i-x) <= k and abs(j-y) <= k) for j in range(c)] for i in range(r)]
            self.assertEqual(matrix_block_sums(a, k), expected)
