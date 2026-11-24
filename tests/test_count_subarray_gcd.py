import random
import unittest

from arrays.count_subarray_gcd import count_subarray_gcd


class TestCountSubarrayGcd(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarray_gcd([9, 3, 1, 2, 6, 3], 3), 4)

    def test_edges(self):
        self.assertEqual(count_subarray_gcd([], 1), 0)
        self.assertEqual(count_subarray_gcd([4, 4, 4], 4), 6)
        with self.assertRaises(ValueError): count_subarray_gcd([0], 1)
        with self.assertRaises(ValueError): count_subarray_gcd([], 0)

    def test_against_reference(self):
        from math import gcd
        rng = random.Random(191)
        for _ in range(130):
            a = [rng.randrange(1, 25) for _ in range(rng.randrange(12))]
            target = rng.randrange(1, 10)
            expected = sum(gcd(*a[i:j]) == target for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_subarray_gcd(a, target), expected)
