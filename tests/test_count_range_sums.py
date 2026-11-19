import random
import unittest

from arrays.count_range_sums import count_range_sums


class TestCountRangeSums(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_range_sums([-2, 5, -1], -2, 2), 3)
        self.assertEqual(count_range_sums([0, 0, 0], 0, 0), 6)

    def test_edges(self):
        self.assertEqual(count_range_sums([], -1, 1), 0)
        self.assertEqual(count_range_sums([-4], -4, -4), 1)
        with self.assertRaises(ValueError):
            count_range_sums([1], 2, 1)

    def test_against_reference(self):
        rng = random.Random(104)
        for _ in range(150):
            values = [rng.randrange(-9, 10) for _ in range(rng.randrange(25))]
            lower, upper = sorted((rng.randrange(-15, 16), rng.randrange(-15, 16)))
            expected = sum(lower <= sum(values[i:j]) <= upper for i in range(len(values)) for j in range(i+1, len(values)+1))
            self.assertEqual(count_range_sums(values, lower, upper), expected)
