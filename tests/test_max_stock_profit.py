import random
import unittest

from arrays.max_stock_profit import max_stock_profit


class TestMaxStockProfit(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_stock_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_stock_profit([7, 6, 4, 3, 1]), 0)

    def test_edges(self):
        self.assertEqual(max_stock_profit([]), 0)
        self.assertEqual(max_stock_profit([4]), 0)
        with self.assertRaises(ValueError):
            max_stock_profit([1, -2])

    def test_against_brute_force(self):
        rng = random.Random(12)
        for _ in range(100):
            values = [rng.randrange(20) for _ in range(rng.randrange(15))]
            expected = max([0] + [values[j]-values[i] for i in range(len(values))
                                  for j in range(i+1, len(values))])
            self.assertEqual(max_stock_profit(values), expected)
