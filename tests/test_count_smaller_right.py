import random
import unittest

from arrays.count_smaller_right import count_smaller_right


class TestCountSmallerRight(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_smaller_right([5, 2, 6, 1]), [2, 1, 1, 0])
        self.assertEqual(count_smaller_right([-1, -2, -1]), [1, 0, 0])

    def test_edges(self):
        self.assertEqual(count_smaller_right([]), [])
        self.assertEqual(count_smaller_right([2, 2, 2]), [0, 0, 0])
        self.assertEqual(count_smaller_right([4]), [0])

    def test_against_reference(self):
        rng = random.Random(41)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(25))]
            original = values.copy()
            expected = [sum(y < x for y in values[i+1:]) for i, x in enumerate(values)]
            self.assertEqual(count_smaller_right(values), expected)
            self.assertEqual(values, original)
