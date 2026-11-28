import random
import unittest

from arrays.offline_range_greater_counts import offline_range_greater_counts


class TestOfflineRangeGreaterCounts(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(offline_range_greater_counts([5, 1, 2, 5], [(0, 4, 2), (1, 4, 5)]), [2, 0])

    def test_edges(self):
        self.assertEqual(offline_range_greater_counts([], [(0, 0, -1)]), [0])
        with self.assertRaises(IndexError): offline_range_greater_counts([1], [(1, 0, 0)])

    def test_against_reference(self):
        rng = random.Random(304)
        for _ in range(130):
            a = [rng.randrange(-15, 16) for _ in range(rng.randrange(80))]
            queries = []
            for _ in range(25):
                left, right = sorted((rng.randrange(len(a)+1), rng.randrange(len(a)+1)))
                queries.append((left, right, rng.randrange(-18, 19)))
            expected = [sum(x > t for x in a[l:r]) for l, r, t in queries]
            self.assertEqual(offline_range_greater_counts(a, queries), expected)
