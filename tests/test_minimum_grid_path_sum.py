import random
import unittest

from arrays.minimum_grid_path_sum import minimum_grid_path_sum


class TestMinimumGridPathSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_grid_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)

    def test_edges(self):
        self.assertIsNone(minimum_grid_path_sum([]))
        self.assertEqual(minimum_grid_path_sum([[-2, 1, -4]]), -5)
        with self.assertRaises(ValueError): minimum_grid_path_sum([[1], []])

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(240)
        for _ in range(120):
            r, c = rng.randrange(1, 7), rng.randrange(1, 7)
            a = [[rng.randrange(-5, 8) for _ in range(c)] for _ in range(r)]
            @lru_cache(None)
            def walk(i, j):
                if i == r-1 and j == c-1: return a[i][j]
                options = []
                if i+1 < r: options.append(walk(i+1, j))
                if j+1 < c: options.append(walk(i, j+1))
                return a[i][j]+min(options)
            self.assertEqual(minimum_grid_path_sum(a), walk(0, 0))
