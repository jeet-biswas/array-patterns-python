import random
import unittest

from arrays.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 4], 2), 1)
        self.assertEqual(binary_search([-3, 0, 9], 9), 2)

    def test_edges(self):
        self.assertEqual(binary_search([], 1), -1)
        self.assertEqual(binary_search([2], 2), 0)
        self.assertEqual(binary_search([2], 1), -1)
        self.assertEqual(binary_search([2], 3), -1)

    def test_against_linear_search(self):
        rng = random.Random(19)
        for _ in range(100):
            values = sorted(rng.randrange(-10, 11) for _ in range(rng.randrange(25)))
            target = rng.randrange(-12, 13)
            expected = values.index(target) if target in values else -1
            self.assertEqual(binary_search(values, target), expected)
