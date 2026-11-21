import random
import unittest

from arrays.min_insertions_target_subsequence import min_insertions_target_subsequence


class TestMinInsertionsTargetSubsequence(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_insertions_target_subsequence([5, 1, 3], [9, 4, 2, 3, 4]), 2)

    def test_edges(self):
        self.assertEqual(min_insertions_target_subsequence([], [1]), 0)
        self.assertEqual(min_insertions_target_subsequence([1, 2], []), 2)
        with self.assertRaises(ValueError): min_insertions_target_subsequence([1, 1], [])

    def test_against_reference(self):
        rng = random.Random(164)
        for _ in range(130):
            target = rng.sample(range(8), rng.randrange(8))
            source = [rng.randrange(10) for _ in range(rng.randrange(12))]
            dp = [[0]*(len(source)+1) for _ in range(len(target)+1)]
            for i, x in enumerate(target, 1):
                for j, y in enumerate(source, 1):
                    dp[i][j] = dp[i-1][j-1]+1 if x == y else max(dp[i-1][j], dp[i][j-1])
            self.assertEqual(min_insertions_target_subsequence(target, source), len(target)-dp[-1][-1])
