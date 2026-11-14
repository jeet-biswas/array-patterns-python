import random
import unittest

from arrays.largest_histogram_rectangle import largest_histogram_rectangle


class TestLargestHistogramRectangle(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(largest_histogram_rectangle([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(largest_histogram_rectangle([2, 2, 2]), 6)

    def test_edges(self):
        self.assertEqual(largest_histogram_rectangle([]), 0)
        self.assertEqual(largest_histogram_rectangle([0, 0]), 0)
        self.assertEqual(largest_histogram_rectangle([7]), 7)
        with self.assertRaises(ValueError):
            largest_histogram_rectangle([2, -1])

    def test_against_reference(self):
        rng = random.Random(44)
        for _ in range(120):
            values = [rng.randrange(9) for _ in range(rng.randrange(16))]
            original = values.copy()
            expected = max((min(values[i:j]) * (j-i) for i in range(len(values))
                            for j in range(i+1, len(values)+1)), default=0)
            self.assertEqual(largest_histogram_rectangle(values), expected)
            self.assertEqual(values, original)
