import random
import unittest

from arrays.kth_lexicographic_permutation import kth_lexicographic_permutation


class TestKthLexicographicPermutation(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_lexicographic_permutation([3, 1, 2], 4), [2, 3, 1])

    def test_edges(self):
        self.assertEqual(kth_lexicographic_permutation([], 1), [])
        with self.assertRaises(ValueError): kth_lexicographic_permutation([1, 1], 1)
        with self.assertRaises(ValueError): kth_lexicographic_permutation([1], 2)
        with self.assertRaises(ValueError): kth_lexicographic_permutation([], 0)

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(264)
        for _ in range(80):
            a = rng.sample(range(-8, 9), rng.randrange(8))
            ordered = sorted(permutations(a))
            for k in {1, len(ordered), rng.randrange(1, len(ordered)+1)}:
                self.assertEqual(kth_lexicographic_permutation(a, k), list(ordered[k-1]))
