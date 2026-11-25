import random
import unittest

from arrays.max_binary_matrix_rectangle import max_binary_matrix_rectangle


class TestMaxBinaryMatrixRectangle(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_binary_matrix_rectangle([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]), 6)

    def test_edges(self):
        self.assertEqual(max_binary_matrix_rectangle([]), 0)
        self.assertEqual(max_binary_matrix_rectangle([[], []]), 0)
        with self.assertRaises(ValueError): max_binary_matrix_rectangle([[2]])
        with self.assertRaises(ValueError): max_binary_matrix_rectangle([[1], []])

    def test_against_reference(self):
        rng = random.Random(234)
        for _ in range(120):
            rows, columns = rng.randrange(6), rng.randrange(6)
            matrix = [[rng.randrange(2) for _ in range(columns)] for _ in range(rows)]
            expected = max(((bottom-top)*(right-left) for top in range(rows) for bottom in range(top+1, rows+1) for left in range(columns) for right in range(left+1, columns+1) if all(matrix[i][j] for i in range(top, bottom) for j in range(left, right))), default=0)
            self.assertEqual(max_binary_matrix_rectangle(matrix), expected)
