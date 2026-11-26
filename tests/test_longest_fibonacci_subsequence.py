import random
import unittest

from arrays.longest_fibonacci_subsequence import longest_fibonacci_subsequence


class TestLongestFibonacciSubsequence(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_fibonacci_subsequence([1, 2, 3, 4, 5, 6, 7, 8]), 5)

    def test_edges(self):
        self.assertEqual(longest_fibonacci_subsequence([]), 0)
        self.assertEqual(longest_fibonacci_subsequence([1, 4, 10]), 0)
        with self.assertRaises(ValueError): longest_fibonacci_subsequence([1, 1, 2])
        with self.assertRaises(ValueError): longest_fibonacci_subsequence([0, 1, 2])

    def test_against_reference(self):
        rng = random.Random(255)
        for _ in range(120):
            a = sorted(rng.sample(range(1, 30), rng.randrange(11)))
            best = 0
            for mask in range(1 << len(a)):
                s = [x for i, x in enumerate(a) if mask >> i & 1]
                if len(s) >= 3 and all(s[i]+s[i+1] == s[i+2] for i in range(len(s)-2)):
                    best = max(best, len(s))
            self.assertEqual(longest_fibonacci_subsequence(a), best)
