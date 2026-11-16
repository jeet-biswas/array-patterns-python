import random
import unittest

from arrays.max_min_distance import max_min_distance


class TestMaxMinDistance(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_min_distance([1, 2, 3, 4, 7], 3), 3)
        self.assertEqual(max_min_distance([-5, 0, 10], 2), 15)

    def test_edges(self):
        self.assertEqual(max_min_distance([2, 2, 2], 2), 0)
        self.assertEqual(max_min_distance([1, 3, 9], 3), 2)
        for positions, count in [([], 2), ([1], 1), ([1, 2], 3)]:
            with self.assertRaises(ValueError):
                max_min_distance(positions, count)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(77)
        for _ in range(120):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(2, 10))]
            count = rng.randrange(2, len(values)+1)
            expected = max(min(abs(a-b) for a, b in combinations(selection, 2))
                           for selection in combinations(values, count))
            original = values.copy()
            self.assertEqual(max_min_distance(values, count), expected)
            self.assertEqual(values, original)
