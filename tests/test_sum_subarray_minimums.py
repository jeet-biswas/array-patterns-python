import random
import unittest

from arrays.sum_subarray_minimums import sum_subarray_minimums


class TestSumSubarrayMinimums(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_subarray_minimums([3, 1, 2, 4]), 17)
        self.assertEqual(sum_subarray_minimums([2, 2, 2]), 12)

    def test_edges(self):
        self.assertEqual(sum_subarray_minimums([]), 0)
        self.assertEqual(sum_subarray_minimums([-3]), -3)
        self.assertEqual(sum_subarray_minimums([-1, -2]), -5)

    def test_against_brute_force(self):
        rng = random.Random(32)
        for _ in range(150):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(15))]
            expected = sum(min(values[i:j]) for i in range(len(values))
                           for j in range(i+1, len(values)+1))
            self.assertEqual(sum_subarray_minimums(values), expected)
