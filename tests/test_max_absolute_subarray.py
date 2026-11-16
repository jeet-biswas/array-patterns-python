import random
import unittest

from arrays.max_absolute_subarray import max_absolute_subarray


class TestMaxAbsoluteSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_absolute_subarray([1, -3, 2, 3, -4]), 5)
        self.assertEqual(max_absolute_subarray([2, -5, 1, -4, 3, -2]), 8)

    def test_edges(self):
        self.assertEqual(max_absolute_subarray([]), 0)
        self.assertEqual(max_absolute_subarray([-7]), 7)
        self.assertEqual(max_absolute_subarray([0, 0]), 0)

    def test_against_reference(self):
        rng = random.Random(70)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(20))]
            expected = max((abs(sum(values[i:j])) for i in range(len(values)) for j in range(i+1, len(values)+1)), default=0)
            self.assertEqual(max_absolute_subarray(values), expected)
