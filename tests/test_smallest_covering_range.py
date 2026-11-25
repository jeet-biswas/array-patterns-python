import random
import unittest

from arrays.smallest_covering_range import smallest_covering_range


class TestSmallestCoveringRange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_covering_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]), (20, 24))

    def test_edges(self):
        self.assertEqual(smallest_covering_range([[1, 2, 3]]), (1, 1))
        with self.assertRaises(ValueError): smallest_covering_range([])
        with self.assertRaises(ValueError): smallest_covering_range([[1], []])
        with self.assertRaises(ValueError): smallest_covering_range([[2, 1]])

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(229)
        for _ in range(130):
            arrays = [sorted(rng.randrange(-10, 11) for _ in range(rng.randrange(1, 6))) for _ in range(rng.randrange(1, 5))]
            intervals = [(min(s), max(s)) for s in product(*arrays)]
            expected = min(intervals, key=lambda p: (p[1]-p[0], p[0]))
            self.assertEqual(smallest_covering_range(arrays), expected)
