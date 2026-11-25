import random
import unittest

from arrays.count_equal_product_tuples import count_equal_product_tuples


class TestCountEqualProductTuples(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_equal_product_tuples([2, 3, 4, 6]), 8)

    def test_edges(self):
        self.assertEqual(count_equal_product_tuples([]), 0)
        with self.assertRaises(ValueError): count_equal_product_tuples([1, 1])
        with self.assertRaises(ValueError): count_equal_product_tuples([0, 2])

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(218)
        for _ in range(120):
            a = rng.sample(range(1, 18), rng.randrange(9))
            self.assertEqual(count_equal_product_tuples(a), sum(w*x == y*z for w, x, y, z in permutations(a, 4)))
