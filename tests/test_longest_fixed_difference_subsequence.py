import random
import unittest

from arrays.longest_fixed_difference_subsequence import longest_fixed_difference_subsequence


class TestLongestFixedDifferenceSubsequence(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_fixed_difference_subsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2), 4)

    def test_edges(self):
        self.assertEqual(longest_fixed_difference_subsequence([], 0), 0)
        self.assertEqual(longest_fixed_difference_subsequence([3, 3, 3], 0), 3)

    def test_against_reference(self):
        rng = random.Random(159)
        for _ in range(120):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(10))]
            difference = rng.randrange(-3, 4)
            best = 0
            for mask in range(1 << len(a)):
                s = [x for i, x in enumerate(a) if mask >> i & 1]
                if all(y-x == difference for x, y in zip(s, s[1:])): best = max(best, len(s))
            self.assertEqual(longest_fixed_difference_subsequence(a, difference), best)
