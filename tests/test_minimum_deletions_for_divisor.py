import random
import unittest

from arrays.minimum_deletions_for_divisor import minimum_deletions_for_divisor


class TestMinimumDeletionsForDivisor(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_deletions_for_divisor([2, 3, 2, 4, 3], [9, 6, 9, 3, 15]), 2)

    def test_edges(self):
        self.assertIsNone(minimum_deletions_for_divisor([], [1]))
        self.assertIsNone(minimum_deletions_for_divisor([2], [3]))
        with self.assertRaises(ValueError): minimum_deletions_for_divisor([1], [])
        with self.assertRaises(ValueError): minimum_deletions_for_divisor([0], [2])

    def test_against_reference(self):
        rng = random.Random(260)
        for _ in range(140):
            a = [rng.randrange(1, 13) for _ in range(rng.randrange(10))]
            targets = [rng.randrange(1, 25) for _ in range(rng.randrange(1, 7))]
            costs = []
            for mask in range(1, 1 << len(a)):
                kept = [x for i, x in enumerate(a) if mask >> i & 1]
                if all(x % min(kept) == 0 for x in targets): costs.append(len(a)-len(kept))
            self.assertEqual(minimum_deletions_for_divisor(a, targets), min(costs, default=None))
