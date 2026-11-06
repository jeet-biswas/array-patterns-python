import random
import unittest

from arrays.next_permutation import next_permutation


class TestNextPermutation(unittest.TestCase):
    def test_examples(self):
        values = [1, 2, 3]
        self.assertTrue(next_permutation(values))
        self.assertEqual(values, [1, 3, 2])
        values = [1, 1, 5]
        self.assertTrue(next_permutation(values))
        self.assertEqual(values, [1, 5, 1])

    def test_edges(self):
        for values, expected in [([], []), ([1], [1]), ([3, 2, 1], [1, 2, 3]), ([2, 2], [2, 2])]:
            self.assertFalse(next_permutation(values))
            self.assertEqual(values, expected)

    def test_all_small_permutations(self):
        from itertools import permutations
        for seed in ([1, 2, 3, 4], [1, 1, 2, 3], [0, 0, 0]):
            ordered = sorted(set(permutations(seed)))
            for i, arrangement in enumerate(ordered):
                values = list(arrangement)
                advanced = next_permutation(values)
                self.assertEqual(values, list(ordered[(i+1) % len(ordered)]))
                self.assertEqual(advanced, i < len(ordered)-1)
