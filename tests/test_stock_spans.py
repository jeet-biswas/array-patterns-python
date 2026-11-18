import random
import unittest

from arrays.stock_spans import stock_spans


class TestStockSpans(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(stock_spans([100, 80, 60, 70, 60, 75, 85]), [1, 1, 1, 2, 1, 4, 6])
        self.assertEqual(stock_spans([1, 2, 3]), [1, 2, 3])

    def test_edges(self):
        self.assertEqual(stock_spans([]), [])
        self.assertEqual(stock_spans([4, 4, 4]), [1, 2, 3])
        self.assertEqual(stock_spans([3, 2, 1]), [1, 1, 1])

    def test_against_reference(self):
        rng = random.Random(95)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(25))]
            expected = []
            for i, value in enumerate(values):
                start = i
                while start > 0 and values[start-1] <= value:
                    start -= 1
                expected.append(i-start+1)
            self.assertEqual(stock_spans(values), expected)
