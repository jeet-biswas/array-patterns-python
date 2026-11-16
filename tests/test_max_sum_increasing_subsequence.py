import random
import unittest

from arrays.max_sum_increasing_subsequence import max_sum_increasing_subsequence


class TestMaxSumIncreasingSubsequence(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 101, 2, 3, 100, 4, 5]), 106)
        self.assertEqual(max_sum_increasing_subsequence([4, 1, 2, 3]), 6)

    def test_edges(self):
        self.assertEqual(max_sum_increasing_subsequence([-5, -2, -3]), -2)
        self.assertEqual(max_sum_increasing_subsequence([2, 2, 2]), 2)
        with self.assertRaises(ValueError):
            max_sum_increasing_subsequence([])

    def test_against_reference(self):
        rng = random.Random(71)
        for _ in range(100):
            values = [rng.randrange(-5, 10) for _ in range(rng.randrange(1, 11))]
            sums = []
            for mask in range(1, 1 << len(values)):
                subsequence = [x for i, x in enumerate(values) if mask & (1 << i)]
                if all(a < b for a, b in zip(subsequence, subsequence[1:])):
                    sums.append(sum(subsequence))
            self.assertEqual(max_sum_increasing_subsequence(values), max(sums))
