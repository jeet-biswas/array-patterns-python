import random
import unittest

from arrays.max_alternating_subsequence_sum import max_alternating_subsequence_sum


class TestMaxAlternatingSubsequenceSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_alternating_subsequence_sum([4, 2, 5, 3]), 7)
        self.assertEqual(max_alternating_subsequence_sum([-2, -5]), 3)

    def test_edges(self):
        self.assertEqual(max_alternating_subsequence_sum([]), 0)
        self.assertEqual(max_alternating_subsequence_sum([-7]), 0)

    def test_against_reference(self):
        rng = random.Random(144)
        for _ in range(120):
            a = [rng.randrange(-6, 7) for _ in range(rng.randrange(9))]
            scores = []
            for mask in range(1 << len(a)):
                selected = [x for i, x in enumerate(a) if mask >> i & 1]
                scores.append(sum(x if i % 2 == 0 else -x for i, x in enumerate(selected)))
            self.assertEqual(max_alternating_subsequence_sum(a), max(scores))
