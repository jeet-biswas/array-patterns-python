import random
import unittest

from arrays.longest_subarray_limit import longest_subarray_limit


class TestLongestSubarrayLimit(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_subarray_limit([8, 2, 4, 7], 4), 2)
        self.assertEqual(longest_subarray_limit([10, 1, 2, 4, 7, 2], 5), 4)

    def test_edges(self):
        self.assertEqual(longest_subarray_limit([], 0), 0)
        self.assertEqual(longest_subarray_limit([2, 2, 2], 0), 3)
        self.assertEqual(longest_subarray_limit([-4], 0), 1)
        with self.assertRaises(ValueError):
            longest_subarray_limit([1], -1)

    def test_against_reference(self):
        rng = random.Random(102)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(20))]
            limit = rng.randrange(12)
            expected = max((j-i for i in range(len(values)) for j in range(i+1, len(values)+1)
                            if max(values[i:j])-min(values[i:j]) <= limit), default=0)
            self.assertEqual(longest_subarray_limit(values, limit), expected)
