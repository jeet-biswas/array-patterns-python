import random
import unittest

from arrays.count_subarrays_median_value import count_subarrays_median_value


class TestCountSubarraysMedianValue(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays_median_value([3, 2, 1, 4, 5], 4), 3)

    def test_edges(self):
        self.assertEqual(count_subarrays_median_value([], 1), 0)
        self.assertEqual(count_subarrays_median_value([2, 3], 4), 0)
        self.assertEqual(count_subarrays_median_value([1, 2], 1), 2)
        with self.assertRaises(ValueError): count_subarrays_median_value([1, 1], 1)

    def test_against_reference(self):
        rng = random.Random(272)
        for _ in range(160):
            a = rng.sample(range(-10, 11), rng.randrange(14))
            target = rng.choice(a) if a and rng.randrange(2) else rng.randrange(-12, 13)
            expected = sum(sorted(a[i:j])[(j-i-1)//2] == target for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_subarrays_median_value(a, target), expected)
