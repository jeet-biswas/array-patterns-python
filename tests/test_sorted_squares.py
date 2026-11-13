import random
import unittest

from arrays.sorted_squares import sorted_squares


class TestSortedSquares(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sorted_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(sorted_squares([-5, -3, -1]), [1, 9, 25])

    def test_edges(self):
        self.assertEqual(sorted_squares([]), [])
        self.assertEqual(sorted_squares([-2]), [4])
        self.assertEqual(sorted_squares([-2, -2, 2]), [4, 4, 4])

    def test_against_sort(self):
        rng = random.Random(21)
        for _ in range(100):
            values = sorted(rng.randrange(-20, 21) for _ in range(rng.randrange(25)))
            original = values.copy()
            self.assertEqual(sorted_squares(values), sorted(x*x for x in values))
            self.assertEqual(values, original)
