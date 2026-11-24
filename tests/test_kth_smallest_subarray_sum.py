import random
import unittest

from arrays.kth_smallest_subarray_sum import kth_smallest_subarray_sum


class TestKthSmallestSubarraySum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_smallest_subarray_sum([2, 1, 3], 4), 3)

    def test_edges(self):
        self.assertEqual(kth_smallest_subarray_sum([0, 0], 3), 0)
        with self.assertRaises(ValueError): kth_smallest_subarray_sum([], 1)
        with self.assertRaises(ValueError): kth_smallest_subarray_sum([-1], 1)
        with self.assertRaises(ValueError): kth_smallest_subarray_sum([1], 2)

    def test_against_reference(self):
        rng = random.Random(189)
        for _ in range(130):
            a = [rng.randrange(8) for _ in range(rng.randrange(1, 12))]
            sums = sorted(sum(a[i:j]) for i in range(len(a)) for j in range(i+1, len(a)+1))
            for k in {1, len(sums), rng.randrange(1, len(sums)+1)}:
                self.assertEqual(kth_smallest_subarray_sum(a, k), sums[k-1])
