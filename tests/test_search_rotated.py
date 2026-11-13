import random
import unittest

from arrays.search_rotated import search_rotated


class TestSearchRotated(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_edges(self):
        self.assertEqual(search_rotated([], 1), -1)
        self.assertEqual(search_rotated([1], 1), 0)
        self.assertEqual(search_rotated([1], 0), -1)
        self.assertEqual(search_rotated([1, 2, 3], 3), 2)

    def test_every_small_rotation(self):
        for n in range(1, 20):
            ordered = list(range(-n, n, 2))
            for k in range(n):
                values = ordered[k:] + ordered[:k]
                for target in range(-n-1, n+1):
                    expected = values.index(target) if target in values else -1
                    self.assertEqual(search_rotated(values, target), expected)
