import random
import unittest

from arrays.count_grid_paths_obstacles import count_grid_paths_obstacles


class TestCountGridPathsObstacles(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_grid_paths_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)

    def test_edges(self):
        self.assertEqual(count_grid_paths_obstacles([]), 0)
        self.assertEqual(count_grid_paths_obstacles([[1]]), 0)
        self.assertEqual(count_grid_paths_obstacles([[0]]), 1)
        with self.assertRaises(ValueError): count_grid_paths_obstacles([[2]])

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(241)
        for _ in range(130):
            r, c = rng.randrange(1, 7), rng.randrange(1, 7)
            a = [[int(rng.randrange(4) == 0) for _ in range(c)] for _ in range(r)]
            @lru_cache(None)
            def walk(i, j):
                if i >= r or j >= c or a[i][j]: return 0
                if i == r-1 and j == c-1: return 1
                return walk(i+1, j)+walk(i, j+1)
            self.assertEqual(count_grid_paths_obstacles(a), walk(0, 0))
