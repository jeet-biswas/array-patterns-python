import random
import unittest

from arrays.wiggle_subsequence_length import wiggle_subsequence_length


class TestWiggleSubsequenceLength(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(wiggle_subsequence_length([1, 7, 4, 9, 2, 5]), 6)
        self.assertEqual(wiggle_subsequence_length([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7)

    def test_edges(self):
        self.assertEqual(wiggle_subsequence_length([]), 0)
        self.assertEqual(wiggle_subsequence_length([3]), 1)
        self.assertEqual(wiggle_subsequence_length([2, 2, 2]), 1)
        self.assertEqual(wiggle_subsequence_length([1, 2, 3, 4]), 2)

    def test_against_reference(self):
        rng = random.Random(101)
        for _ in range(100):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(11))]
            expected = 0
            for mask in range(1 << len(values)):
                sequence = [x for i, x in enumerate(values) if mask & (1 << i)]
                differences = [b-a for a, b in zip(sequence, sequence[1:])]
                if all(d != 0 for d in differences) and all(a*b < 0 for a, b in zip(differences, differences[1:])):
                    expected = max(expected, len(sequence))
            self.assertEqual(wiggle_subsequence_length(values), expected)
