import random
import unittest

from arrays.lis_length import lis_length


class TestLisLength(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(lis_length([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(lis_length([0, 1, 0, 3, 2, 3]), 4)

    def test_edges(self):
        self.assertEqual(lis_length([]), 0)
        self.assertEqual(lis_length([7, 7, 7]), 1)
        self.assertEqual(lis_length([3, 2, 1]), 1)

    def test_against_reference(self):
        rng = random.Random(40)
        for _ in range(150):
            values = [rng.randrange(-6, 7) for _ in range(rng.randrange(25))]
            dp = [1] * len(values)
            for i in range(len(values)):
                for j in range(i):
                    if values[j] < values[i]:
                        dp[i] = max(dp[i], dp[j]+1)
            self.assertEqual(lis_length(values), max(dp, default=0))
