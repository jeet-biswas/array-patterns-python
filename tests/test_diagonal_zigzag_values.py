import random
import unittest

from arrays.diagonal_zigzag_values import diagonal_zigzag_values


class TestDiagonalZigzagValues(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(diagonal_zigzag_values([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 4, 7, 5, 3, 6, 8, 9])

    def test_edges(self):
        self.assertEqual(diagonal_zigzag_values([]), [])
        self.assertEqual(diagonal_zigzag_values([[1], [2], [3]]), [1, 2, 3])
        with self.assertRaises(ValueError): diagonal_zigzag_values([[1], []])

    def test_against_reference(self):
        for r in range(9):
            for c in range(9):
                a = [[i*c+j for j in range(c)] for i in range(r)]
                coordinates = sorted(((i, j) for i in range(r) for j in range(c)), key=lambda p: (sum(p), p[0] if sum(p) % 2 else -p[0]))
                self.assertEqual(diagonal_zigzag_values(a), [a[i][j] for i, j in coordinates])
