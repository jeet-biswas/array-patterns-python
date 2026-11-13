import random
import unittest

from arrays.max_product_subarray import max_product_subarray


class TestMaxProductSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_product_subarray([2, 3, -2, 4]), 6)
        self.assertEqual(max_product_subarray([-2, 3, -4]), 24)

    def test_edges(self):
        self.assertEqual(max_product_subarray([-7]), -7)
        self.assertEqual(max_product_subarray([-2, 0, -1]), 0)
        with self.assertRaises(ValueError):
            max_product_subarray([])

    def test_against_brute_force(self):
        from math import prod
        rng = random.Random(23)
        for _ in range(100):
            values = [rng.randrange(-3, 4) for _ in range(rng.randrange(1, 12))]
            expected = max(prod(values[i:j]) for i in range(len(values))
                           for j in range(i+1, len(values)+1))
            self.assertEqual(max_product_subarray(values), expected)
