import random
import unittest

from arrays.maximum_subarray_xor import maximum_subarray_xor


class TestMaximumSubarrayXor(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximum_subarray_xor([1, 2, 3, 4]), 7)

    def test_edges(self):
        self.assertEqual(maximum_subarray_xor([]), 0)
        self.assertEqual(maximum_subarray_xor([0, 0]), 0)
        with self.assertRaises(ValueError): maximum_subarray_xor([-1])

    def test_against_reference(self):
        from functools import reduce
        from operator import xor
        rng = random.Random(315)
        for _ in range(170):
            a = [rng.randrange(256) for _ in range(rng.randrange(25))]
            expected = max((reduce(xor, a[i:j]) for i in range(len(a)) for j in range(i+1, len(a)+1)), default=0)
            self.assertEqual(maximum_subarray_xor(a), expected)
