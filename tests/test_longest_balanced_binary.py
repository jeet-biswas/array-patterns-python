import random
import unittest

from arrays.longest_balanced_binary import longest_balanced_binary


class TestLongestBalancedBinary(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_balanced_binary([0, 1, 0]), 2)
        self.assertEqual(longest_balanced_binary([0, 0, 1, 0, 1, 1]), 6)

    def test_edges(self):
        for values in ([], [1], [0, 0, 0]):
            self.assertEqual(longest_balanced_binary(values), 0)
        with self.assertRaises(ValueError):
            longest_balanced_binary([0, 2, 1])

    def test_against_reference(self):
        from itertools import product
        for n in range(8):
            for state in product((0, 1), repeat=n):
                values = list(state)
                expected = max((j-i for i in range(n) for j in range(i+1, n+1)
                                if sum(values[i:j])*2 == j-i), default=0)
                self.assertEqual(longest_balanced_binary(values), expected)
