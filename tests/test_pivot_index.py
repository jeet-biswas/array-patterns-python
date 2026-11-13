import random
import unittest

from arrays.pivot_index import pivot_index


class TestPivotIndex(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(pivot_index([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(pivot_index([2, 1, -1]), 0)

    def test_edges(self):
        self.assertEqual(pivot_index([]), -1)
        self.assertEqual(pivot_index([9]), 0)
        self.assertEqual(pivot_index([0, 0, 0]), 0)
        self.assertEqual(pivot_index([1, 2, 3]), -1)

    def test_against_brute_force(self):
        rng = random.Random(26)
        for _ in range(100):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(20))]
            expected = next((i for i in range(len(values)) if sum(values[:i]) == sum(values[i+1:])), -1)
            self.assertEqual(pivot_index(values), expected)
