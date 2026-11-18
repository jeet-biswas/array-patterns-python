import random
import unittest

from arrays.count_fixed_bounds import count_fixed_bounds


class TestCountFixedBounds(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_fixed_bounds([1, 3, 5, 2, 7, 5], 1, 5), 2)
        self.assertEqual(count_fixed_bounds([1, 1, 1, 1], 1, 1), 10)

    def test_edges(self):
        self.assertEqual(count_fixed_bounds([], 1, 2), 0)
        self.assertEqual(count_fixed_bounds([1, 2, 3], 0, 3), 0)
        self.assertEqual(count_fixed_bounds([-2, -1], -2, -1), 1)
        with self.assertRaises(ValueError):
            count_fixed_bounds([1], 2, 1)

    def test_against_reference(self):
        rng = random.Random(86)
        for _ in range(150):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(15))]
            lower, upper = sorted((rng.randrange(-5, 6), rng.randrange(-5, 6)))
            expected = sum(min(values[i:j]) == lower and max(values[i:j]) == upper
                           for i in range(len(values)) for j in range(i+1, len(values)+1))
            self.assertEqual(count_fixed_bounds(values, lower, upper), expected)
