import random
import unittest

from arrays.three_sum import three_sum


class TestThreeSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1)])
        self.assertEqual(three_sum([0, 0, 0, 0]), [(0, 0, 0)])

    def test_edges(self):
        for values in ([], [0], [0, 0], [1, 2, 3]):
            self.assertEqual(three_sum(values), [])

    def test_against_combinations(self):
        from itertools import combinations
        rng = random.Random(22)
        for _ in range(100):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(12))]
            original = values.copy()
            expected = sorted({tuple(sorted(t)) for t in combinations(values, 3) if sum(t) == 0})
            self.assertEqual(three_sum(values), expected)
            self.assertEqual(values, original)
