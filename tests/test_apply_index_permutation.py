import random
import unittest

from arrays.apply_index_permutation import apply_index_permutation


class TestApplyIndexPermutation(unittest.TestCase):
    def test_examples(self):
        a = [10, 20, 30]
        self.assertIsNone(apply_index_permutation(a, [2, 0, 1]))
        self.assertEqual(a, [20, 30, 10])

    def test_edges(self):
        a = []
        apply_index_permutation(a, [])
        self.assertEqual(a, [])
        a = [7, 8]
        with self.assertRaises(ValueError): apply_index_permutation(a, [0, 0])
        self.assertEqual(a, [7, 8])
        with self.assertRaises(ValueError): apply_index_permutation(a, a)

    def test_against_reference(self):
        rng = random.Random(292)
        for _ in range(150):
            n = rng.randrange(60)
            a = [rng.randrange(-20, 21) for _ in range(n)]
            p = rng.sample(range(n), n)
            before = p.copy()
            expected = [0]*n
            for i in range(n): expected[p[i]] = a[i]
            apply_index_permutation(a, p)
            self.assertEqual(a, expected)
            self.assertEqual(p, before)
