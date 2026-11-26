import random
import unittest

from arrays.longest_increasing_matrix_path import longest_increasing_matrix_path


class TestLongestIncreasingMatrixPath(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_increasing_matrix_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)

    def test_edges(self):
        self.assertEqual(longest_increasing_matrix_path([]), 0)
        self.assertEqual(longest_increasing_matrix_path([[2, 2], [2, 2]]), 1)
        with self.assertRaises(ValueError): longest_increasing_matrix_path([[1], []])

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(243)
        for _ in range(120):
            r, c = rng.randrange(1, 6), rng.randrange(1, 6)
            a = [[rng.randrange(-5, 6) for _ in range(c)] for _ in range(r)]
            @lru_cache(None)
            def walk(i, j):
                return 1+max((walk(x, y) for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)) if 0 <= x < r and 0 <= y < c and a[x][y] > a[i][j]), default=0)
            self.assertEqual(longest_increasing_matrix_path(a), max(walk(i, j) for i in range(r) for j in range(c)))
