import random
import unittest

from arrays.contains_sorted_matrix_value import contains_sorted_matrix_value


class TestContainsSortedMatrixValue(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(contains_sorted_matrix_value([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 6))

    def test_edges(self):
        self.assertFalse(contains_sorted_matrix_value([], 1))
        self.assertFalse(contains_sorted_matrix_value([[1, 3], [2, 4]], 5))
        with self.assertRaises(ValueError): contains_sorted_matrix_value([[1], []], 1)

    def test_against_reference(self):
        rng = random.Random(247)
        for _ in range(160):
            r, c = rng.randrange(8), rng.randrange(8)
            a = []
            for i in range(r):
                row = []
                for j in range(c):
                    lower = max(row[j-1] if j else -10, a[i-1][j] if i else -10)
                    row.append(lower+rng.randrange(4))
                a.append(row)
            target = rng.randrange(-12, 25)
            self.assertEqual(contains_sorted_matrix_value(a, target), any(target in row for row in a))
