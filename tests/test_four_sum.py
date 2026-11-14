import random
import unittest

from arrays.four_sum import four_sum


class TestFourSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(four_sum([1, 0, -1, 0, -2, 2], 0), [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)])
        self.assertEqual(four_sum([2, 2, 2, 2, 2], 8), [(2, 2, 2, 2)])

    def test_edges(self):
        self.assertEqual(four_sum([], 0), [])
        self.assertEqual(four_sum([0, 0, 0], 0), [])
        self.assertEqual(four_sum([1, 2, 3, 4], -1), [])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(37)
        for _ in range(100):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(12))]
            original = values.copy()
            target = rng.randrange(-10, 11)
            expected = sorted({tuple(sorted(t)) for t in combinations(values, 4) if sum(t) == target})
            self.assertEqual(four_sum(values, target), expected)
            self.assertEqual(values, original)
