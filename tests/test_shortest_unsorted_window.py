import random
import unittest

from arrays.shortest_unsorted_window import shortest_unsorted_window


class TestShortestUnsortedWindow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_unsorted_window([2, 6, 4, 8, 10, 9, 15]), 5)
        self.assertEqual(shortest_unsorted_window([1, 3, 2, 2, 2]), 4)

    def test_edges(self):
        for values in ([], [1], [1, 2, 3], [2, 2]):
            self.assertEqual(shortest_unsorted_window(values), 0)
        self.assertEqual(shortest_unsorted_window([3, 2, 1]), 3)

    def test_against_reference(self):
        rng = random.Random(46)
        for _ in range(150):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(20))]
            original = values.copy()
            wrong = [i for i, (a, b) in enumerate(zip(values, sorted(values))) if a != b]
            expected = wrong[-1] - wrong[0] + 1 if wrong else 0
            self.assertEqual(shortest_unsorted_window(values), expected)
            self.assertEqual(values, original)
