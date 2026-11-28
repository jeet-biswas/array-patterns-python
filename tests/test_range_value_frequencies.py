import random
import unittest

from arrays.range_value_frequencies import range_value_frequencies


class TestRangeValueFrequencies(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(range_value_frequencies([1, 2, 1, 3, 1], [(1, 5, 1), (0, 2, 3)]), [2, 0])

    def test_edges(self):
        self.assertEqual(range_value_frequencies([], [(0, 0, 7)]), [0])
        with self.assertRaises(IndexError): range_value_frequencies([1], [(0, 2, 1)])

    def test_against_reference(self):
        rng = random.Random(303)
        for _ in range(130):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(80))]
            queries = []
            for _ in range(20):
                left, right = sorted((rng.randrange(len(a)+1), rng.randrange(len(a)+1)))
                queries.append((left, right, rng.randrange(-7, 8)))
            self.assertEqual(range_value_frequencies(a, queries), [a[l:r].count(v) for l, r, v in queries])
