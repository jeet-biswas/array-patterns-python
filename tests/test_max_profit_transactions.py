import random
import unittest

from arrays.max_profit_transactions import max_profit_transactions


class TestMaxProfitTransactions(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_profit_transactions([3, 2, 6, 5, 0, 3], 2), 7)
        self.assertEqual(max_profit_transactions([2, 4, 1], 1), 2)

    def test_edges(self):
        self.assertEqual(max_profit_transactions([], 10), 0)
        self.assertEqual(max_profit_transactions([1, 2, 3], 0), 0)
        self.assertEqual(max_profit_transactions([1, 4, 2, 5], 1000), 6)
        for prices, limit in [([1], -1), ([-1], 1)]:
            with self.assertRaises(ValueError):
                max_profit_transactions(prices, limit)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(125)
        for _ in range(100):
            prices = [rng.randrange(10) for _ in range(rng.randrange(11))]
            limit = rng.randrange(5)
            @lru_cache(None)
            def schedule(start, remaining):
                if remaining == 0:
                    return 0
                return max([0] + [prices[sell]-prices[buy]+schedule(sell+1, remaining-1)
                                  for buy in range(start, len(prices)) for sell in range(buy+1, len(prices))])
            self.assertEqual(max_profit_transactions(prices, limit), schedule(0, limit))
