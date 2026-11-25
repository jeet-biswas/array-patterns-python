import random
import unittest

from arrays.zero_matrix_rows_columns import zero_matrix_rows_columns


class TestZeroMatrixRowsColumns(unittest.TestCase):
    def test_examples(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.assertIsNone(zero_matrix_rows_columns(matrix))
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_edges(self):
        matrix = [[], []]
        zero_matrix_rows_columns(matrix)
        self.assertEqual(matrix, [[], []])
        matrix = [[0, 1], [2]]
        with self.assertRaises(ValueError): zero_matrix_rows_columns(matrix)
        self.assertEqual(matrix, [[0, 1], [2]])

    def test_against_reference(self):
        rng = random.Random(233)
        for _ in range(150):
            rows, columns = rng.randrange(9), rng.randrange(9)
            matrix = [[rng.randrange(-2, 4) for _ in range(columns)] for _ in range(rows)]
            original = [row[:] for row in matrix]
            row_ids = [id(row) for row in matrix]
            zeros = [(i, j) for i in range(rows) for j in range(columns) if original[i][j] == 0]
            expected = [[0 if any(i == a or j == b for a, b in zeros) else original[i][j] for j in range(columns)] for i in range(rows)]
            zero_matrix_rows_columns(matrix)
            self.assertEqual(matrix, expected)
            self.assertEqual([id(row) for row in matrix], row_ids)
