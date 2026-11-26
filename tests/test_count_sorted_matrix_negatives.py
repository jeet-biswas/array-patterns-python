import random
import unittest

from arrays.count_sorted_matrix_negatives import count_sorted_matrix_negatives


class TestCountSortedMatrixNegatives(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_sorted_matrix_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]), 8)

    def test_edges(self):
        self.assertEqual(count_sorted_matrix_negatives([]), 0)
        self.assertEqual(count_sorted_matrix_negatives([[0, 0], [0, -1]]), 1)
        with self.assertRaises(ValueError): count_sorted_matrix_negatives([[1], []])

    def test_against_reference(self):
        rng = random.Random(246)
        for _ in range(160):
            r, c = rng.randrange(9), rng.randrange(9)
            a = []
            for i in range(r):
                row = []
                for j in range(c):
                    upper = min(row[j-1] if j else 8, a[i-1][j] if i else 8)
                    row.append(upper-rng.randrange(5))
                a.append(row)
            self.assertEqual(count_sorted_matrix_negatives(a), sum(x < 0 for row in a for x in row))
