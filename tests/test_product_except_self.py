import random
import unittest

from arrays.product_except_self import product_except_self


class TestProductExceptSelf(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self([-1, 2, -3]), [-6, 3, -2])

    def test_edges(self):
        self.assertEqual(product_except_self([]), [])
        self.assertEqual(product_except_self([5]), [1])
        self.assertEqual(product_except_self([0, 2, 3]), [6, 0, 0])
        self.assertEqual(product_except_self([0, 2, 0]), [0, 0, 0])

    def test_against_brute_force(self):
        import math
        rng = random.Random(7)
        for _ in range(100):
            values = [rng.randrange(-3, 4) for _ in range(rng.randrange(10))]
            expected = [math.prod(values[:i] + values[i + 1:]) for i in range(len(values))]
            self.assertEqual(product_except_self(values), expected)
