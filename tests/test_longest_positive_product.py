import random
import unittest

from arrays.longest_positive_product import longest_positive_product


class TestLongestPositiveProduct(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_positive_product([1, -2, -3, 4]), 4)
        self.assertEqual(longest_positive_product([0, 1, -2, -3, -4]), 3)

    def test_edges(self):
        self.assertEqual(longest_positive_product([]), 0)
        self.assertEqual(longest_positive_product([-1]), 0)

    def test_against_reference(self):
        from math import prod
        rng = random.Random(143)
        for _ in range(150):
            a = [rng.randrange(-2, 3) for _ in range(rng.randrange(12))]
            expected = max((j-i for i in range(len(a)) for j in range(i+1, len(a)+1) if prod(a[i:j]) > 0), default=0)
            self.assertEqual(longest_positive_product(a), expected)
