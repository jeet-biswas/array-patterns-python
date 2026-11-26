import random
import unittest

from arrays.minimum_falling_path_sum import minimum_falling_path_sum


class TestMinimumFallingPathSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]), 13)

    def test_edges(self):
        self.assertIsNone(minimum_falling_path_sum([[], []]))
        self.assertEqual(minimum_falling_path_sum([[1], [-2], [3]]), 2)
        with self.assertRaises(ValueError): minimum_falling_path_sum([[1], []])

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(242)
        for _ in range(100):
            r, c = rng.randrange(1, 6), rng.randrange(1, 5)
            a = [[rng.randrange(-7, 8) for _ in range(c)] for _ in range(r)]
            expected = min(sum(a[i][j] for i, j in enumerate(path)) for path in product(range(c), repeat=r) if all(abs(x-y) <= 1 for x, y in zip(path, path[1:])))
            self.assertEqual(minimum_falling_path_sum(a), expected)
