import random
import unittest

from arrays.inverse_index_permutation import inverse_index_permutation


class TestInverseIndexPermutation(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(inverse_index_permutation([2, 0, 1]), [1, 2, 0])

    def test_edges(self):
        self.assertEqual(inverse_index_permutation([]), [])
        with self.assertRaises(ValueError): inverse_index_permutation([1, 1])
        with self.assertRaises(ValueError): inverse_index_permutation([-1])

    def test_against_reference(self):
        rng = random.Random(293)
        for _ in range(150):
            n = rng.randrange(80)
            p = rng.sample(range(n), n)
            self.assertEqual(inverse_index_permutation(p), [p.index(i) for i in range(n)])
