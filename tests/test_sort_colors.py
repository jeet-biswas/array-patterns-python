import random
import unittest

from arrays.sort_colors import sort_colors


class TestSortColors(unittest.TestCase):
    def test_examples(self):
        values = [2, 0, 2, 1, 1, 0]
        self.assertIsNone(sort_colors(values))
        self.assertEqual(values, [0, 0, 1, 1, 2, 2])

    def test_edges(self):
        for values in ([], [0], [1, 1], [2, 2]):
            original = values.copy()
            sort_colors(values)
            self.assertEqual(values, original)
        values = [2, 0, 4]
        with self.assertRaises(ValueError):
            sort_colors(values)
        self.assertEqual(values, [2, 0, 4])

    def test_against_sort(self):
        rng = random.Random(17)
        for _ in range(100):
            values = [rng.randrange(3) for _ in range(rng.randrange(25))]
            expected = sorted(values)
            sort_colors(values)
            self.assertEqual(values, expected)
