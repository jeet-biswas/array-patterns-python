import random
import unittest

from arrays.max_circular_subarray import max_circular_subarray


class TestMaxCircularSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_circular_subarray([5, -3, 5]), 10)
        self.assertEqual(max_circular_subarray([1, -2, 3, -2]), 3)

    def test_edges(self):
        self.assertEqual(max_circular_subarray([-3, -2, -5]), -2)
        self.assertEqual(max_circular_subarray([7]), 7)
        self.assertEqual(max_circular_subarray([0, 0]), 0)
        with self.assertRaises(ValueError):
            max_circular_subarray([])

    def test_against_brute_force(self):
        rng = random.Random(31)
        for _ in range(120):
            values = [rng.randrange(-6, 7) for _ in range(rng.randrange(1, 12))]
            expected = max(sum(values[(start+j) % len(values)] for j in range(length))
                           for start in range(len(values)) for length in range(1, len(values)+1))
            self.assertEqual(max_circular_subarray(values), expected)
