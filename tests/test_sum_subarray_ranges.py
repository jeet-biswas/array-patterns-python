import random
import unittest

from arrays.sum_subarray_ranges import sum_subarray_ranges


class TestSumSubarrayRanges(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_subarray_ranges([1, 2, 3]), 4)
        self.assertEqual(sum_subarray_ranges([4, -2, -3, 4, 1]), 59)

    def test_edges(self):
        self.assertEqual(sum_subarray_ranges([]), 0)
        self.assertEqual(sum_subarray_ranges([-5]), 0)
        self.assertEqual(sum_subarray_ranges([2, 2, 2]), 0)
        self.assertEqual(sum_subarray_ranges([1, 3, 3]), 4)

    def test_against_reference(self):
        rng = random.Random(96)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(18))]
            expected = sum(max(values[i:j])-min(values[i:j]) for i in range(len(values)) for j in range(i+1, len(values)+1))
            self.assertEqual(sum_subarray_ranges(values), expected)
