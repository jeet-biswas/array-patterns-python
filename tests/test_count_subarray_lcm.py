import random
import unittest

from arrays.count_subarray_lcm import count_subarray_lcm


class TestCountSubarrayLcm(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarray_lcm([3, 6, 2, 7, 1], 6), 4)

    def test_edges(self):
        self.assertEqual(count_subarray_lcm([], 1), 0)
        self.assertEqual(count_subarray_lcm([1, 1], 1), 3)
        with self.assertRaises(ValueError): count_subarray_lcm([-1], 1)
        with self.assertRaises(ValueError): count_subarray_lcm([], 0)

    def test_against_reference(self):
        from math import lcm
        rng = random.Random(192)
        for _ in range(150):
            a = [rng.randrange(1, 13) for _ in range(rng.randrange(12))]
            target = rng.randrange(1, 37)
            expected = sum(lcm(*a[i:j]) == target for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_subarray_lcm(a, target), expected)
