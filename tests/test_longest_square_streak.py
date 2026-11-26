import random
import unittest

from arrays.longest_square_streak import longest_square_streak


class TestLongestSquareStreak(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_square_streak([4, 3, 6, 16, 8, 2]), 3)

    def test_edges(self):
        self.assertEqual(longest_square_streak([]), -1)
        self.assertEqual(longest_square_streak([2, 2]), -1)
        with self.assertRaises(ValueError): longest_square_streak([1])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(256)
        for _ in range(110):
            a = [rng.choice([2, 3, 4, 9, 16, 81, 256, 5, 25]) for _ in range(rng.randrange(11))]
            best = -1
            for k in range(2, len(a)+1):
                for subset in combinations(a, k):
                    s = sorted(subset)
                    if all(x*x == y for x, y in zip(s, s[1:])): best = max(best, k)
            self.assertEqual(longest_square_streak(a), best)
