import random
import unittest

from arrays.min_cost_equal_weighted import min_cost_equal_weighted


class TestMinCostEqualWeighted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_cost_equal_weighted([1, 3, 5, 2], [2, 3, 1, 14]), 8)
        self.assertEqual(min_cost_equal_weighted([-3, 4], [1, 2]), 7)

    def test_edges(self):
        self.assertEqual(min_cost_equal_weighted([], []), 0)
        self.assertEqual(min_cost_equal_weighted([1, 9], [0, 0]), 0)
        self.assertEqual(min_cost_equal_weighted([7], [3]), 0)
        for values, weights in [([1], []), ([1], [-1])]:
            with self.assertRaises(ValueError):
                min_cost_equal_weighted(values, weights)

    def test_against_reference(self):
        rng = random.Random(119)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 15))]
            weights = [rng.randrange(6) for _ in values]
            original = values.copy(), weights.copy()
            expected = min(sum(w*abs(x-target) for x, w in zip(values, weights))
                           for target in range(min(values), max(values)+1))
            self.assertEqual(min_cost_equal_weighted(values, weights), expected)
            self.assertEqual((values, weights), original)
