import random
import unittest

from arrays.max_subsequence_dot_product import max_subsequence_dot_product


class TestMaxSubsequenceDotProduct(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_subsequence_dot_product([2, 1, -2, 5], [3, 0, -6]), 18)

    def test_edges(self):
        self.assertEqual(max_subsequence_dot_product([-1, -1], [1, 1]), -1)
        with self.assertRaises(ValueError): max_subsequence_dot_product([], [1])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(161)
        for _ in range(80):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(1, 7))]
            b = [rng.randrange(-4, 5) for _ in range(rng.randrange(1, 7))]
            expected = max(sum(x*y for x, y in zip(s, t)) for k in range(1, min(len(a), len(b))+1) for s in combinations(a, k) for t in combinations(b, k))
            self.assertEqual(max_subsequence_dot_product(a, b), expected)
