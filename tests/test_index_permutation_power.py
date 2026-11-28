import random
import unittest

from arrays.index_permutation_power import index_permutation_power


class TestIndexPermutationPower(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(index_permutation_power([2, 0, 1], 2), [1, 2, 0])
        self.assertEqual(index_permutation_power([2, 0, 1], -1), [1, 2, 0])

    def test_edges(self):
        self.assertEqual(index_permutation_power([], 10**50), [])
        self.assertEqual(index_permutation_power([1, 0], 0), [0, 1])
        with self.assertRaises(ValueError): index_permutation_power([2], 1)

    def test_against_reference(self):
        rng = random.Random(294)
        for _ in range(160):
            n = rng.randrange(40)
            p = rng.sample(range(n), n)
            exponent = rng.randrange(-20, 21)
            mapping = p if exponent >= 0 else [p.index(i) for i in range(n)]
            expected = list(range(n))
            for _ in range(abs(exponent)): expected = [mapping[i] for i in expected]
            self.assertEqual(index_permutation_power(p, exponent), expected)
