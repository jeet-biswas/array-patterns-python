import random
import unittest

from arrays.rotate_square_clockwise import rotate_square_clockwise


class TestRotateSquareClockwise(unittest.TestCase):
    def test_examples(self):
        matrix = [[1, 2], [3, 4]]
        self.assertIsNone(rotate_square_clockwise(matrix))
        self.assertEqual(matrix, [[3, 1], [4, 2]])

    def test_edges(self):
        matrix = []
        rotate_square_clockwise(matrix)
        self.assertEqual(matrix, [])
        matrix = [[1, 2], [3]]
        with self.assertRaises(ValueError): rotate_square_clockwise(matrix)
        self.assertEqual(matrix, [[1, 2], [3]])

    def test_against_reference(self):
        rng = random.Random(232)
        for n in range(12):
            matrix = [[rng.randrange(-9, 10) for _ in range(n)] for _ in range(n)]
            original = [row[:] for row in matrix]
            row_ids = [id(row) for row in matrix]
            expected = [[original[n-1-j][i] for j in range(n)] for i in range(n)]
            rotate_square_clockwise(matrix)
            self.assertEqual(matrix, expected)
            self.assertEqual([id(row) for row in matrix], row_ids)
            for _ in range(3): rotate_square_clockwise(matrix)
            self.assertEqual(matrix, original)
