import random
import unittest

from arrays.count_target_submatrices import count_target_submatrices


class TestCountTargetSubmatrices(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_target_submatrices([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0), 4)

    def test_edges(self):
        self.assertEqual(count_target_submatrices([[], []], 0), 0)
        self.assertEqual(count_target_submatrices([[0, 0], [0, 0]], 0), 9)
        with self.assertRaises(ValueError): count_target_submatrices([[1], []], 0)

    def test_against_reference(self):
        rng = random.Random(237)
        for _ in range(100):
            r, c = rng.randrange(6), rng.randrange(6)
            a = [[rng.randrange(-3, 4) for _ in range(c)] for _ in range(r)]
            target = rng.randrange(-6, 7)
            expected = sum(sum(a[i][j] for i in range(top, bottom) for j in range(left, right)) == target for top in range(r) for bottom in range(top+1, r+1) for left in range(c) for right in range(left+1, c+1))
            self.assertEqual(count_target_submatrices(a, target), expected)
