import random
import unittest

from arrays.largest_divisible_subset import largest_divisible_subset


class TestLargestDivisibleSubset(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(largest_divisible_subset([1, 2, 4, 8]), [1, 2, 4, 8])
        self.assertEqual(largest_divisible_subset([1, 2, 3]), [1, 2])

    def test_edges(self):
        self.assertEqual(largest_divisible_subset([]), [])
        self.assertEqual(largest_divisible_subset([2, 2, 4]), [2, 2, 4])
        with self.assertRaises(ValueError): largest_divisible_subset([0])

    def test_against_reference(self):
        from collections import Counter
        from itertools import combinations
        rng = random.Random(193)
        for _ in range(110):
            a = [rng.randrange(1, 19) for _ in range(rng.randrange(10))]
            expected = max(k for k in range(len(a)+1) if any(all(x % y == 0 or y % x == 0 for x, y in combinations(s, 2)) for s in combinations(a, k)))
            before = a.copy()
            result = largest_divisible_subset(a)
            self.assertEqual(len(result), expected)
            self.assertEqual(result, sorted(result))
            self.assertFalse(Counter(result)-Counter(a))
            self.assertTrue(all(x % y == 0 or y % x == 0 for x, y in combinations(result, 2)))
            self.assertEqual(a, before)
