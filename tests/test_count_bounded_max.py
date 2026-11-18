import random
import unittest

from arrays.count_bounded_max import count_bounded_max


class TestCountBoundedMax(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_bounded_max([2, 1, 4, 3], 2, 3), 3)
        self.assertEqual(count_bounded_max([2, 9, 2, 5, 6], 2, 8), 7)

    def test_edges(self):
        self.assertEqual(count_bounded_max([], 0, 0), 0)
        self.assertEqual(count_bounded_max([2, 2], 2, 2), 3)
        self.assertEqual(count_bounded_max([-3, -2], -2, -1), 2)
        with self.assertRaises(ValueError):
            count_bounded_max([1], 2, 1)

    def test_against_reference(self):
        rng = random.Random(85)
        for _ in range(150):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(15))]
            lower, upper = sorted((rng.randrange(-6, 7), rng.randrange(-6, 7)))
            expected = sum(lower <= max(values[i:j]) <= upper for i in range(len(values)) for j in range(i+1, len(values)+1))
            self.assertEqual(count_bounded_max(values, lower, upper), expected)
