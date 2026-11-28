import random
import unittest

from arrays.sum_subset_xors import sum_subset_xors


class TestSumSubsetXors(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_subset_xors([1, 3]), 6)

    def test_edges(self):
        self.assertEqual(sum_subset_xors([]), 0)
        self.assertEqual(sum_subset_xors([0, 0]), 0)
        with self.assertRaises(ValueError): sum_subset_xors([-1])

    def test_against_reference(self):
        from functools import reduce
        from operator import xor
        rng = random.Random(308)
        for _ in range(130):
            a = [rng.randrange(32) for _ in range(rng.randrange(12))]
            expected = sum(reduce(xor, (x for i, x in enumerate(a) if mask >> i & 1), 0) for mask in range(1 << len(a)))
            self.assertEqual(sum_subset_xors(a), expected)
