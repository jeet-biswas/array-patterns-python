import random
import unittest

from arrays.max_subarray import max_subarray


class TestMaxSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_subarray([-4, -2, -7]), -2)

    def test_edges(self):
        self.assertEqual(max_subarray([0]), 0)
        self.assertEqual(max_subarray([9]), 9)
        with self.assertRaises(ValueError):
            max_subarray([])

    def test_against_brute_force(self):
        rng = random.Random(2)
        for _ in range(100):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 12))]
            expected = max(sum(values[i:j]) for i in range(len(values))
                           for j in range(i + 1, len(values) + 1))
            self.assertEqual(max_subarray(values), expected)
