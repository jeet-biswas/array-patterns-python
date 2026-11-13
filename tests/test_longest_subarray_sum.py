import random
import unittest

from arrays.longest_subarray_sum import longest_subarray_sum


class TestLongestSubarraySum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_subarray_sum([1, -1, 5, -2, 3], 3), 4)
        self.assertEqual(longest_subarray_sum([-2, -1, 2, 1], 1), 2)

    def test_edges(self):
        self.assertEqual(longest_subarray_sum([], 0), 0)
        self.assertEqual(longest_subarray_sum([0, 0, 0], 0), 3)
        self.assertEqual(longest_subarray_sum([1, 2], 8), 0)

    def test_against_brute_force(self):
        rng = random.Random(25)
        for _ in range(100):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(15))]
            target = rng.randrange(-8, 9)
            expected = max((j-i for i in range(len(values)) for j in range(i+1, len(values)+1)
                            if sum(values[i:j]) == target), default=0)
            self.assertEqual(longest_subarray_sum(values, target), expected)
