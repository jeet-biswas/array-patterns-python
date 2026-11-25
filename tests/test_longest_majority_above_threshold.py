import random
import unittest

from arrays.longest_majority_above_threshold import longest_majority_above_threshold


class TestLongestMajorityAboveThreshold(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_majority_above_threshold([9, 9, 6, 0, 6, 6, 9], 8), 3)

    def test_edges(self):
        self.assertEqual(longest_majority_above_threshold([], 0), 0)
        self.assertEqual(longest_majority_above_threshold([3, 3], 3), 0)

    def test_against_reference(self):
        rng = random.Random(219)
        for _ in range(160):
            a = [rng.randrange(-6, 7) for _ in range(rng.randrange(15))]
            threshold = rng.randrange(-4, 5)
            expected = max((j-i for i in range(len(a)) for j in range(i+1, len(a)+1) if 2*sum(x > threshold for x in a[i:j]) > j-i), default=0)
            self.assertEqual(longest_majority_above_threshold(a, threshold), expected)
