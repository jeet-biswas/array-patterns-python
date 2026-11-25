import random
import unittest

from arrays.kth_smallest_sorted_matrix import kth_smallest_sorted_matrix


class TestKthSmallestSortedMatrix(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_smallest_sorted_matrix([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13)

    def test_edges(self):
        self.assertEqual(kth_smallest_sorted_matrix([[2, 2]], 2), 2)
        with self.assertRaises(ValueError): kth_smallest_sorted_matrix([], 1)
        with self.assertRaises(ValueError): kth_smallest_sorted_matrix([[1], []], 1)
        with self.assertRaises(ValueError): kth_smallest_sorted_matrix([[1], [0]], 1)
        with self.assertRaises(ValueError): kth_smallest_sorted_matrix([[1]], 2)

    def test_against_reference(self):
        rng = random.Random(230)
        for _ in range(120):
            rows, columns = rng.randrange(1, 8), rng.randrange(1, 8)
            matrix = []
            for i in range(rows):
                row = []
                for j in range(columns):
                    lower = max(row[j-1] if j else -10, matrix[i-1][j] if i else -10)
                    row.append(lower+rng.randrange(4))
                matrix.append(row)
            ordered = sorted(x for row in matrix for x in row)
            for k in {1, len(ordered), rng.randrange(1, len(ordered)+1)}:
                self.assertEqual(kth_smallest_sorted_matrix(matrix, k), ordered[k-1])
