import random
import unittest

from arrays.max_xor_pair import max_xor_pair


class TestMaxXorPair(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_xor_pair([3, 10, 5, 25, 2, 8]), 28)
        self.assertEqual(max_xor_pair([0, 7]), 7)

    def test_edges(self):
        self.assertEqual(max_xor_pair([0, 0]), 0)
        self.assertEqual(max_xor_pair([5, 5]), 0)
        self.assertEqual(max_xor_pair([1 << 80, 1]), (1 << 80) + 1)
        for values in ([], [1], [-1, 2]):
            with self.assertRaises(ValueError):
                max_xor_pair(values)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(106)
        for _ in range(150):
            values = [rng.randrange(1024) for _ in range(rng.randrange(2, 25))]
            self.assertEqual(max_xor_pair(values), max(a ^ b for a, b in combinations(values, 2)))
