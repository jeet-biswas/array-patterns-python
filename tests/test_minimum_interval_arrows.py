import random
import unittest

from arrays.minimum_interval_arrows import minimum_interval_arrows


class TestMinimumIntervalArrows(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_interval_arrows([(10, 16), (2, 8), (1, 6), (7, 12)]), 2)

    def test_edges(self):
        self.assertEqual(minimum_interval_arrows([]), 0)
        self.assertEqual(minimum_interval_arrows([(1, 2), (2, 3)]), 1)
        with self.assertRaises(ValueError): minimum_interval_arrows([(3, 1)])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(172)
        for _ in range(100):
            a = [tuple(sorted((rng.randrange(-3, 5), rng.randrange(-3, 5)))) for _ in range(rng.randrange(7))]
            points = sorted({x for interval in a for x in interval})
            expected = next(k for k in range(len(points)+1) if any(all(any(start <= p <= end for p in chosen) for start, end in a) for chosen in combinations(points, k)))
            before = a.copy()
            self.assertEqual(minimum_interval_arrows(a), expected)
            self.assertEqual(a, before)
