import random
import unittest

from arrays.max_frequency_increments import max_frequency_increments


class TestMaxFrequencyIncrements(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_frequency_increments([1, 2, 4], 5), 3)
        self.assertEqual(max_frequency_increments([1, 4, 8, 13], 5), 2)

    def test_edges(self):
        self.assertEqual(max_frequency_increments([], 0), 0)
        self.assertEqual(max_frequency_increments([-3, -2, -2], 0), 2)
        self.assertEqual(max_frequency_increments([-3, -2, -2], 1), 3)
        with self.assertRaises(ValueError):
            max_frequency_increments([1], -1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(87)
        for _ in range(100):
            values = [rng.randrange(-4, 7) for _ in range(rng.randrange(10))]
            original = values.copy()
            budget = rng.randrange(15)
            expected = max((size for size in range(1, len(values)+1)
                            for chosen in combinations(values, size)
                            if size*max(chosen)-sum(chosen) <= budget), default=0)
            self.assertEqual(max_frequency_increments(values, budget), expected)
            self.assertEqual(values, original)
