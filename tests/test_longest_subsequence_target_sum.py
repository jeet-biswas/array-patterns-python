import random
import unittest

from arrays.longest_subsequence_target_sum import longest_subsequence_target_sum


class TestLongestSubsequenceTargetSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_subsequence_target_sum([1, 2, 3, 4, 5], 9), 3)

    def test_edges(self):
        self.assertEqual(longest_subsequence_target_sum([], 0), 0)
        self.assertIsNone(longest_subsequence_target_sum([], 1))
        self.assertEqual(longest_subsequence_target_sum([0, -2, 2, 0], 0), 4)

    def test_against_reference(self):
        rng = random.Random(196)
        for _ in range(140):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(11))]
            target = rng.randrange(-12, 13)
            expected = max((mask.bit_count() for mask in range(1 << len(a)) if sum(x for i, x in enumerate(a) if mask >> i & 1) == target), default=None)
            self.assertEqual(longest_subsequence_target_sum(a, target), expected)
