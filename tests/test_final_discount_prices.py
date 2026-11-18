import random
import unittest

from arrays.final_discount_prices import final_discount_prices


class TestFinalDiscountPrices(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(final_discount_prices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])
        self.assertEqual(final_discount_prices([10, 1, 1, 6]), [9, 0, 1, 6])

    def test_edges(self):
        self.assertEqual(final_discount_prices([]), [])
        self.assertEqual(final_discount_prices([2, 2]), [0, 2])
        self.assertEqual(final_discount_prices([0, 0]), [0, 0])
        with self.assertRaises(ValueError):
            final_discount_prices([1, -2])

    def test_against_reference(self):
        rng = random.Random(94)
        for _ in range(150):
            values = [rng.randrange(12) for _ in range(rng.randrange(25))]
            original = values.copy()
            expected = [x-next((y for y in values[i+1:] if y <= x), 0) for i, x in enumerate(values)]
            self.assertEqual(final_discount_prices(values), expected)
            self.assertEqual(values, original)
