import random
import unittest

from arrays.closest_subarray_and_difference import closest_subarray_and_difference


class TestClosestSubarrayAndDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(closest_subarray_and_difference([9, 12, 3, 7, 15], 5), 2)

    def test_edges(self):
        self.assertIsNone(closest_subarray_and_difference([], 0))
        self.assertEqual(closest_subarray_and_difference([0], 3), 3)
        with self.assertRaises(ValueError): closest_subarray_and_difference([-1], 0)

    def test_against_reference(self):
        from functools import reduce
        from operator import and_
        rng = random.Random(312)
        for _ in range(170):
            a = [rng.randrange(64) for _ in range(rng.randrange(20))]
            target = rng.randrange(100)
            expected = min((abs(reduce(and_, a[i:j])-target) for i in range(len(a)) for j in range(i+1, len(a)+1)), default=None)
            self.assertEqual(closest_subarray_and_difference(a, target), expected)
