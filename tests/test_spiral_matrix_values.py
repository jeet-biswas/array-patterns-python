import random
import unittest

from arrays.spiral_matrix_values import spiral_matrix_values


class TestSpiralMatrixValues(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(spiral_matrix_values([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_edges(self):
        self.assertEqual(spiral_matrix_values([]), [])
        self.assertEqual(spiral_matrix_values([[], []]), [])
        self.assertEqual(spiral_matrix_values([[1], [2], [3]]), [1, 2, 3])
        with self.assertRaises(ValueError): spiral_matrix_values([[1], []])

    def test_against_reference(self):
        for rows in range(8):
            for columns in range(8):
                matrix = [[i*columns+j for j in range(columns)] for i in range(rows)]
                visited = set()
                expected = []
                i = j = direction = 0
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for _ in range(rows*columns):
                    expected.append(matrix[i][j])
                    visited.add((i, j))
                    di, dj = directions[direction]
                    if not (0 <= i+di < rows and 0 <= j+dj < columns) or (i+di, j+dj) in visited:
                        direction = (direction+1) % 4
                        di, dj = directions[direction]
                    i, j = i+di, j+dj
                self.assertEqual(spiral_matrix_values(matrix), expected)
