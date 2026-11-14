import random
import unittest

from arrays.three_sum_closest import three_sum_closest


class TestThreeSumClosest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(three_sum_closest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(three_sum_closest([-2, 0, 2, 4], 1), 0)

    def test_edges(self):
        self.assertEqual(three_sum_closest([0, 0, 0], 100), 0)
        for values in ([], [1], [1, 2]):
            with self.assertRaises(ValueError):
                three_sum_closest(values, 0)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(38)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(3, 12))]
            original = values.copy()
            target = rng.randrange(-15, 16)
            expected = min((sum(t) for t in combinations(values, 3)), key=lambda s: (abs(s-target), s))
            self.assertEqual(three_sum_closest(values, target), expected)
            self.assertEqual(values, original)
