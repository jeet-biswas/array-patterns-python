import random
import unittest

from arrays.count_product_below import count_product_below


class TestCountProductBelow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_product_below([10, 5, 2, 6], 100), 8)
        self.assertEqual(count_product_below([1, 1, 1], 2), 6)

    def test_edges(self):
        self.assertEqual(count_product_below([], 5), 0)
        self.assertEqual(count_product_below([1, 2], 1), 0)
        self.assertEqual(count_product_below([5], 5), 0)
        for values in ([0, 2], [-1]):
            with self.assertRaises(ValueError):
                count_product_below(values, 0)

    def test_against_reference(self):
        from math import prod
        rng = random.Random(84)
        for _ in range(150):
            values = [rng.randrange(1, 8) for _ in range(rng.randrange(15))]
            threshold = rng.randrange(-3, 100)
            expected = sum(prod(values[i:j]) < threshold for i in range(len(values)) for j in range(i+1, len(values)+1))
            self.assertEqual(count_product_below(values, threshold), expected)
