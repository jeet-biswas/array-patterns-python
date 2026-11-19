import random
import unittest

from arrays.kth_pair_distance import kth_pair_distance


class TestKthPairDistance(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_pair_distance([1, 3, 1], 1), 0)
        self.assertEqual(kth_pair_distance([1, 6, 1], 3), 5)

    def test_edges(self):
        self.assertEqual(kth_pair_distance([-4, 3], 1), 7)
        self.assertEqual(kth_pair_distance([2, 2, 2], 3), 0)
        for values, k in [([], 1), ([1], 1), ([1, 2], 0), ([1, 2], 2)]:
            with self.assertRaises(ValueError):
                kth_pair_distance(values, k)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(117)
        for _ in range(150):
            values = [rng.randrange(-15, 16) for _ in range(rng.randrange(2, 20))]
            distances = sorted(abs(a-b) for a, b in combinations(values, 2))
            k = rng.randrange(1, len(distances)+1)
            original = values.copy()
            self.assertEqual(kth_pair_distance(values, k), distances[k-1])
            self.assertEqual(values, original)
