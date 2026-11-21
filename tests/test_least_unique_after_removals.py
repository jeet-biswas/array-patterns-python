import random
import unittest

from arrays.least_unique_after_removals import least_unique_after_removals


class TestLeastUniqueAfterRemovals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(least_unique_after_removals([4, 3, 1, 1, 3, 3, 2], 3), 2)

    def test_edges(self):
        self.assertEqual(least_unique_after_removals([], 0), 0)
        self.assertEqual(least_unique_after_removals([1, 2], 2), 0)
        with self.assertRaises(ValueError): least_unique_after_removals([1], 2)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(179)
        for _ in range(150):
            a = [rng.randrange(5) for _ in range(rng.randrange(10))]
            k = rng.randrange(len(a)+1)
            expected = min(len(set(kept)) for kept in combinations(a, len(a)-k))
            self.assertEqual(least_unique_after_removals(a, k), expected)
