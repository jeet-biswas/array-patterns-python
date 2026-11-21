import random
import unittest

from arrays.count_bounded_spread_subarrays import count_bounded_spread_subarrays


class TestCountBoundedSpreadSubarrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_bounded_spread_subarrays([5, 4, 2, 4], 2), 8)

    def test_edges(self):
        self.assertEqual(count_bounded_spread_subarrays([], 2), 0)
        self.assertEqual(count_bounded_spread_subarrays([1, 1], 0), 3)
        self.assertEqual(count_bounded_spread_subarrays([1], -1), 0)

    def test_against_reference(self):
        rng = random.Random(156)
        for _ in range(150):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(12))]
            limit = rng.randrange(-1, 8)
            expected = sum(max(a[i:j])-min(a[i:j]) <= limit for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_bounded_spread_subarrays(a, limit), expected)
