import random
import unittest

from arrays.minimum_k_bit_flips import minimum_k_bit_flips


class TestMinimumKBitFlips(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_k_bit_flips([0, 0, 0, 1, 0, 1, 1, 0], 3), 3)

    def test_edges(self):
        self.assertEqual(minimum_k_bit_flips([], 3), 0)
        self.assertEqual(minimum_k_bit_flips([0, 1], 3), -1)
        with self.assertRaises(ValueError): minimum_k_bit_flips([2], 1)
        with self.assertRaises(ValueError): minimum_k_bit_flips([], 0)

    def test_against_reference(self):
        from itertools import product
        for n in range(7):
            for bits in product((0, 1), repeat=n):
                for k in range(1, n+2):
                    best = None
                    for mask in range(1 << max(0, n-k+1)):
                        a = list(bits)
                        for start in range(max(0, n-k+1)):
                            if mask >> start & 1:
                                for i in range(start, start+k): a[i] ^= 1
                        if all(a):
                            count = mask.bit_count()
                            best = count if best is None else min(best, count)
                    self.assertEqual(minimum_k_bit_flips(list(bits), k), -1 if best is None else best)
