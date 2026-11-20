import random
import unittest

from arrays.max_profit_fee import max_profit_fee


class TestMaxProfitFee(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_profit_fee([1, 3, 2, 8, 4, 9], 2), 8)
        self.assertEqual(max_profit_fee([1, 3, 7, 5, 10, 3], 3), 6)

    def test_edges(self):
        self.assertEqual(max_profit_fee([], 0), 0)
        self.assertEqual(max_profit_fee([2], 1), 0)
        self.assertEqual(max_profit_fee([1, 2, 3], 5), 0)
        for prices, fee in [([-1], 0), ([1], -1)]:
            with self.assertRaises(ValueError):
                max_profit_fee(prices, fee)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(126)
        for _ in range(100):
            prices = [rng.randrange(10) for _ in range(rng.randrange(11))]
            fee = rng.randrange(6)
            @lru_cache(None)
            def schedule(start):
                return max([0] + [prices[sell]-prices[buy]-fee+schedule(sell+1)
                                  for buy in range(start, len(prices)) for sell in range(buy+1, len(prices))])
            self.assertEqual(max_profit_fee(prices, fee), schedule(0))
