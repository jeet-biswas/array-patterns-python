import random
import unittest

from arrays.multiset_permutation_rank import multiset_permutation_rank


class TestMultisetPermutationRank(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(multiset_permutation_rank([2, 1, 1]), 3)
        self.assertEqual(multiset_permutation_rank([1, 2, 1]), 2)

    def test_edges(self):
        self.assertEqual(multiset_permutation_rank([]), 1)
        self.assertEqual(multiset_permutation_rank([7, 7, 7]), 1)
        self.assertEqual(multiset_permutation_rank([-2, -1]), 1)

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(265)
        for _ in range(130):
            a = [rng.randrange(-2, 3) for _ in range(rng.randrange(8))]
            ordered = sorted(set(permutations(a)))
            self.assertEqual(multiset_permutation_rank(a), ordered.index(tuple(a))+1)
