import random
import unittest

from arrays.max_profit_cooldown import max_profit_cooldown


class TestMaxProfitCooldown(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_profit_cooldown([1, 2, 3, 0, 2]), 3)
        self.assertEqual(max_profit_cooldown([1, 4, 2]), 3)

    def test_edges(self):
        self.assertEqual(max_profit_cooldown([]), 0)
        self.assertEqual(max_profit_cooldown([5]), 0)
        self.assertEqual(max_profit_cooldown([5, 3, 1]), 0)
        self.assertEqual(max_profit_cooldown([0, 0, 0]), 0)
        with self.assertRaises(ValueError):
            max_profit_cooldown([1, -1])

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(81)
        for _ in range(120):
            prices = [rng.randrange(9) for _ in range(rng.randrange(11))]
            @lru_cache(None)
            def schedule(start):
                return max([0] + [prices[sell]-prices[buy]+schedule(sell+2)
                                  for buy in range(start, len(prices))
                                  for sell in range(buy+1, len(prices))])
            self.assertEqual(max_profit_cooldown(prices), schedule(0))
