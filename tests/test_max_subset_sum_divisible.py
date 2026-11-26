import random
import unittest

from arrays.max_subset_sum_divisible import max_subset_sum_divisible


class TestMaxSubsetSumDivisible(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_subset_sum_divisible([3, 6, 5, 1, 8], 3), 18)
        self.assertEqual(max_subset_sum_divisible([-1, 6], 5), 5)

    def test_edges(self):
        self.assertEqual(max_subset_sum_divisible([], 7), 0)
        self.assertEqual(max_subset_sum_divisible([-3, -2], 1), 0)
        with self.assertRaises(ValueError): max_subset_sum_divisible([], 0)

    def test_against_reference(self):
        rng = random.Random(251)
        for _ in range(140):
            a = [rng.randrange(-8, 10) for _ in range(rng.randrange(11))]
            modulus = rng.randrange(1, 9)
            sums = [sum(x for i, x in enumerate(a) if mask >> i & 1) for mask in range(1 << len(a))]
            self.assertEqual(max_subset_sum_divisible(a, modulus), max(s for s in sums if s % modulus == 0))
