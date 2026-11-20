import random
import unittest

from arrays.max_subsequence_score import max_subsequence_score


class TestMaxSubsequenceScore(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_subsequence_score([1, 3, 3, 2], [2, 1, 3, 4], 3), 12)
        self.assertEqual(max_subsequence_score([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1), 30)

    def test_edges(self):
        self.assertEqual(max_subsequence_score([0, 0], [1, 2], 2), 0)
        for first, second, k in [([], [], 1), ([1], [], 1), ([-1], [2], 1), ([1], [2], 0)]:
            with self.assertRaises(ValueError):
                max_subsequence_score(first, second, k)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(136)
        for _ in range(120):
            n = rng.randrange(1, 11)
            first, second = [rng.randrange(10) for _ in range(n)], [rng.randrange(10) for _ in range(n)]
            k = rng.randrange(1, n+1)
            expected = max(sum(first[i] for i in chosen)*min(second[i] for i in chosen)
                           for chosen in combinations(range(n), k))
            original = first.copy(), second.copy()
            self.assertEqual(max_subsequence_score(first, second, k), expected)
            self.assertEqual((first, second), original)
