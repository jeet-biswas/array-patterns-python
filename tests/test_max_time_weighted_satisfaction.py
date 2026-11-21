import random
import unittest

from arrays.max_time_weighted_satisfaction import max_time_weighted_satisfaction


class TestMaxTimeWeightedSatisfaction(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_time_weighted_satisfaction([-1, -8, 0, 5, -9]), 14)

    def test_edges(self):
        self.assertEqual(max_time_weighted_satisfaction([]), 0)
        self.assertEqual(max_time_weighted_satisfaction([-3, -2, -1]), 0)

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(180)
        for _ in range(60):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(7))]
            expected = max(sum((i+1)*x for i, x in enumerate(order)) for k in range(len(a)+1) for order in permutations(a, k))
            self.assertEqual(max_time_weighted_satisfaction(a), expected)
