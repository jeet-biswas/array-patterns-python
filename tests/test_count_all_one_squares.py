import random
import unittest

from arrays.count_all_one_squares import count_all_one_squares


class TestCountAllOneSquares(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_all_one_squares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]), 15)

    def test_edges(self):
        self.assertEqual(count_all_one_squares([]), 0)
        self.assertEqual(count_all_one_squares([[], []]), 0)
        with self.assertRaises(ValueError): count_all_one_squares([[2]])
        with self.assertRaises(ValueError): count_all_one_squares([[1], []])

    def test_against_reference(self):
        rng = random.Random(235)
        for _ in range(140):
            rows, columns = rng.randrange(8), rng.randrange(8)
            matrix = [[rng.randrange(2) for _ in range(columns)] for _ in range(rows)]
            expected = sum(all(matrix[i][j] for i in range(top, top+size) for j in range(left, left+size)) for size in range(1, min(rows, columns)+1) for top in range(rows-size+1) for left in range(columns-size+1))
            self.assertEqual(count_all_one_squares(matrix), expected)
