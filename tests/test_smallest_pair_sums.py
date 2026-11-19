import random
import unittest

from arrays.smallest_pair_sums import smallest_pair_sums


class TestSmallestPairSums(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_pair_sums([1, 7, 11], [2, 4, 6], 3), [(1, 2), (1, 4), (1, 6)])
        self.assertEqual(smallest_pair_sums([1, 1, 2], [1, 2], 3), [(1, 1), (1, 1), (1, 2)])

    def test_edges(self):
        self.assertEqual(smallest_pair_sums([], [1], 3), [])
        self.assertEqual(smallest_pair_sums([1], [2], 0), [])
        self.assertEqual(smallest_pair_sums([1], [2], 5), [(1, 2)])
        with self.assertRaises(ValueError):
            smallest_pair_sums([], [], -1)

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(118)
        for _ in range(150):
            left = sorted(rng.randrange(-5, 6) for _ in range(rng.randrange(12)))
            right = sorted(rng.randrange(-5, 6) for _ in range(rng.randrange(12)))
            k = rng.randrange(30)
            original = left.copy(), right.copy()
            expected = sorted(product(left, right), key=lambda pair: (sum(pair), pair[0], pair[1]))[:k]
            self.assertEqual(smallest_pair_sums(left, right, k), expected)
            self.assertEqual((left, right), original)
