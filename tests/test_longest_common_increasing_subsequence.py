import random
import unittest

from arrays.longest_common_increasing_subsequence import longest_common_increasing_subsequence


class TestLongestCommonIncreasingSubsequence(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_common_increasing_subsequence([3, 4, 9, 1], [5, 3, 8, 9, 10, 2, 1]), 2)

    def test_edges(self):
        self.assertEqual(longest_common_increasing_subsequence([], [1]), 0)
        self.assertEqual(longest_common_increasing_subsequence([2, 2], [2, 2, 2]), 1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(259)
        for _ in range(110):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(9))]
            b = [rng.randrange(-4, 5) for _ in range(rng.randrange(9))]
            best = 0
            for k in range(1, min(len(a), len(b))+1):
                common = set(combinations(a, k)) & set(combinations(b, k))
                if any(all(x < y for x, y in zip(s, s[1:])) for s in common): best = k
            self.assertEqual(longest_common_increasing_subsequence(a, b), best)
