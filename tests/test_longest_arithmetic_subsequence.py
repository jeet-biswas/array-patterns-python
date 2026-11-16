import random
import unittest

from arrays.longest_arithmetic_subsequence import longest_arithmetic_subsequence


class TestLongestArithmeticSubsequence(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_arithmetic_subsequence([3, 6, 9, 12]), 4)
        self.assertEqual(longest_arithmetic_subsequence([9, 4, 7, 2, 10]), 3)

    def test_edges(self):
        self.assertEqual(longest_arithmetic_subsequence([]), 0)
        self.assertEqual(longest_arithmetic_subsequence([5]), 1)
        self.assertEqual(longest_arithmetic_subsequence([2, 2, 2, 2]), 4)
        self.assertEqual(longest_arithmetic_subsequence([5, 3, 1]), 3)

    def test_against_reference(self):
        rng = random.Random(73)
        for _ in range(100):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(10))]
            expected = 0
            for mask in range(1 << len(values)):
                sequence = [x for i, x in enumerate(values) if mask & (1 << i)]
                differences = [b-a for a, b in zip(sequence, sequence[1:])]
                if len(set(differences)) <= 1:
                    expected = max(expected, len(sequence))
            self.assertEqual(longest_arithmetic_subsequence(values), expected)
