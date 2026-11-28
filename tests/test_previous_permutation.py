import random
import unittest

from arrays.previous_permutation import previous_permutation


class TestPreviousPermutation(unittest.TestCase):
    def test_examples(self):
        a = [3, 1, 2]
        self.assertTrue(previous_permutation(a))
        self.assertEqual(a, [2, 3, 1])

    def test_edges(self):
        a = [1, 2, 2]
        self.assertFalse(previous_permutation(a))
        self.assertEqual(a, [2, 2, 1])
        self.assertFalse(previous_permutation([]))

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(295)
        for _ in range(100):
            a = [rng.randrange(-2, 3) for _ in range(rng.randrange(8))]
            ordered = sorted(set(permutations(a)))
            index = ordered.index(tuple(a))
            self.assertEqual(previous_permutation(a), index > 0)
            self.assertEqual(tuple(a), ordered[index-1])
