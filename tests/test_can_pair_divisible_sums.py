import random
import unittest

from arrays.can_pair_divisible_sums import can_pair_divisible_sums


class TestCanPairDivisibleSums(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(can_pair_divisible_sums([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
        self.assertFalse(can_pair_divisible_sums([1, 2, 3, 4, 5, 6], 10))

    def test_edges(self):
        self.assertTrue(can_pair_divisible_sums([], 1))
        self.assertTrue(can_pair_divisible_sums([-1, 1], 3))
        self.assertFalse(can_pair_divisible_sums([2], 2))
        with self.assertRaises(ValueError): can_pair_divisible_sums([], 0)

    def test_against_reference(self):
        rng = random.Random(194)
        for _ in range(150):
            a = [rng.randrange(-8, 9) for _ in range(rng.randrange(10))]
            modulus = rng.randrange(1, 8)
            def possible(s):
                if not s: return True
                return any((s[0]+s[j]) % modulus == 0 and possible(s[1:j]+s[j+1:]) for j in range(1, len(s)))
            self.assertEqual(can_pair_divisible_sums(a, modulus), possible(a))
