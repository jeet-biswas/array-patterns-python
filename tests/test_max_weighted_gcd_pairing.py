import random
import unittest

from arrays.max_weighted_gcd_pairing import max_weighted_gcd_pairing


class TestMaxWeightedGcdPairing(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_weighted_gcd_pairing([3, 4, 6, 8]), 11)

    def test_edges(self):
        self.assertEqual(max_weighted_gcd_pairing([]), 0)
        self.assertEqual(max_weighted_gcd_pairing([2, 4]), 2)
        with self.assertRaises(ValueError): max_weighted_gcd_pairing([1])
        with self.assertRaises(ValueError): max_weighted_gcd_pairing([0, 2])

    def test_against_reference(self):
        from itertools import permutations
        from math import gcd
        rng = random.Random(262)
        for _ in range(70):
            a = [rng.randrange(1, 13) for _ in range(2*rng.randrange(4))]
            expected = max((sum((i//2+1)*gcd(order[i], order[i+1]) for i in range(0, len(order), 2)) for order in permutations(a)), default=0)
            self.assertEqual(max_weighted_gcd_pairing(a), expected)
