import random
import unittest

from arrays.matrix_rectangle_sums import matrix_rectangle_sums


class TestMatrixRectangleSums(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(matrix_rectangle_sums([[1, 2, 3], [4, 5, 6]], [(0, 1, 2, 3), (1, 0, 2, 1)]), [16, 4])

    def test_edges(self):
        self.assertEqual(matrix_rectangle_sums([], [(0, 0, 0, 0)]), [0])
        self.assertEqual(matrix_rectangle_sums([[], []], [(0, 0, 2, 0)]), [0])
        with self.assertRaises(ValueError): matrix_rectangle_sums([[1], []], [])
        with self.assertRaises(IndexError): matrix_rectangle_sums([[1]], [(0, 0, 2, 1)])
        with self.assertRaises(IndexError): matrix_rectangle_sums([[1]], [(1, 0, 0, 1)])

    def test_against_reference(self):
        rng = random.Random(236)
        for _ in range(120):
            rows, columns = rng.randrange(8), rng.randrange(8)
            if rows == 0: columns = 0
            matrix = [[rng.randrange(-9, 10) for _ in range(columns)] for _ in range(rows)]
            queries, expected = [], []
            for _ in range(15):
                top, bottom = sorted((rng.randrange(rows+1), rng.randrange(rows+1)))
                left, right = sorted((rng.randrange(columns+1), rng.randrange(columns+1)))
                queries.append((top, left, bottom, right))
                expected.append(sum(matrix[i][j] for i in range(top, bottom) for j in range(left, right)))
            self.assertEqual(matrix_rectangle_sums(matrix, queries), expected)
