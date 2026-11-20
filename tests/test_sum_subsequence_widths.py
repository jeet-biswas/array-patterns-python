import random
import unittest

from arrays.sum_subsequence_widths import sum_subsequence_widths


class TestSumSubsequenceWidths(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_subsequence_widths([2, 1, 3]), 6)
        self.assertEqual(sum_subsequence_widths([-2, 3]), 5)

    def test_edges(self):
        self.assertEqual(sum_subsequence_widths([]), 0)
        self.assertEqual(sum_subsequence_widths([7]), 0)
        self.assertEqual(sum_subsequence_widths([2, 2, 2]), 0)

    def test_against_reference(self):
        rng = random.Random(135)
        for _ in range(100):
            values = [rng.randrange(-6, 7) for _ in range(rng.randrange(11))]
            expected = 0
            for mask in range(1, 1 << len(values)):
                sequence = [x for i, x in enumerate(values) if mask & (1 << i)]
                expected += max(sequence)-min(sequence)
            original = values.copy()
            self.assertEqual(sum_subsequence_widths(values), expected)
            self.assertEqual(values, original)
