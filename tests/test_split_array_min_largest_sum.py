import random
import unittest

from arrays.split_array_min_largest_sum import split_array_min_largest_sum


class TestSplitArrayMinLargestSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(split_array_min_largest_sum([7, 2, 5, 10, 8], 2), 18)
        self.assertEqual(split_array_min_largest_sum([1, 2, 3, 4, 5], 2), 9)

    def test_edges(self):
        self.assertEqual(split_array_min_largest_sum([0, 0, 0], 2), 0)
        self.assertEqual(split_array_min_largest_sum([3, 1], 1), 4)
        self.assertEqual(split_array_min_largest_sum([3, 1], 2), 3)
        for values, k in [([], 1), ([1], 0), ([1], 2), ([-1, 2], 1)]:
            with self.assertRaises(ValueError):
                split_array_min_largest_sum(values, k)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(76)
        for _ in range(120):
            values = [rng.randrange(8) for _ in range(rng.randrange(1, 10))]
            k = rng.randrange(1, len(values)+1)
            expected = min(max(sum(values[a:b]) for a, b in zip((0,)+cuts, cuts+(len(values),)))
                           for cuts in combinations(range(1, len(values)), k-1))
            self.assertEqual(split_array_min_largest_sum(values, k), expected)
