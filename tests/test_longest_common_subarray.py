import random
import unittest

from arrays.longest_common_subarray import longest_common_subarray


class TestLongestCommonSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_common_subarray([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]), 3)

    def test_edges(self):
        self.assertEqual(longest_common_subarray([], []), 0)
        self.assertEqual(longest_common_subarray([0, 0], [0, 0, 0]), 2)

    def test_against_reference(self):
        rng = random.Random(163)
        for _ in range(120):
            a = [rng.randrange(4) for _ in range(rng.randrange(10))]
            b = [rng.randrange(4) for _ in range(rng.randrange(10))]
            blocks = {tuple(a[i:j]) for i in range(len(a)) for j in range(i+1, len(a)+1)}
            expected = max((j-i for i in range(len(b)) for j in range(i+1, len(b)+1) if tuple(b[i:j]) in blocks), default=0)
            self.assertEqual(longest_common_subarray(a, b), expected)
