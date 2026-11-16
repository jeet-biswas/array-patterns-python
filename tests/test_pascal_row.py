import random
import unittest

from arrays.pascal_row import pascal_row


class TestPascalRow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(pascal_row(3), [1, 3, 3, 1])
        self.assertEqual(pascal_row(5), [1, 5, 10, 10, 5, 1])

    def test_edges(self):
        self.assertEqual(pascal_row(0), [1])
        self.assertEqual(pascal_row(1), [1, 1])
        with self.assertRaises(ValueError):
            pascal_row(-1)

    def test_against_reference(self):
        from math import comb
        for index in range(50):
            row = pascal_row(index)
            self.assertEqual(row, [comb(index, j) for j in range(index+1)])
            self.assertEqual(sum(row), 2**index)
