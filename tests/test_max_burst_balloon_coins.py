import random
import unittest

from arrays.max_burst_balloon_coins import max_burst_balloon_coins


class TestMaxBurstBalloonCoins(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_burst_balloon_coins([3, 1, 5, 8]), 167)

    def test_edges(self):
        self.assertEqual(max_burst_balloon_coins([]), 0)
        self.assertEqual(max_burst_balloon_coins([0, 0]), 0)
        self.assertEqual(max_burst_balloon_coins([7]), 7)
        with self.assertRaises(ValueError): max_burst_balloon_coins([-1])

    def test_against_reference(self):
        from functools import lru_cache
        @lru_cache(None)
        def reference(s):
            return max(((s[i-1] if i else 1)*x*(s[i+1] if i+1 < len(s) else 1)+reference(s[:i]+s[i+1:]) for i, x in enumerate(s)), default=0)
        rng = random.Random(221)
        for _ in range(100):
            a = [rng.randrange(6) for _ in range(rng.randrange(8))]
            self.assertEqual(max_burst_balloon_coins(a), reference(tuple(a)))
