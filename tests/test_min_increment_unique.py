import random
import unittest

from arrays.min_increment_unique import min_increment_unique


class TestMinIncrementUnique(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_increment_unique([3, 2, 1, 2, 1, 7]), 6)
        self.assertEqual(min_increment_unique([-2, -2, -2]), 3)

    def test_edges(self):
        self.assertEqual(min_increment_unique([]), 0)
        self.assertEqual(min_increment_unique([1, 2, 9]), 0)
        self.assertEqual(min_increment_unique([0, 0]), 1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(68)
        for _ in range(70):
            values = [rng.randrange(-2, 4) for _ in range(rng.randrange(1, 6))]
            ordered = sorted(values)
            expected = min(sum(target)-sum(values)
                           for target in combinations(range(min(values), max(values)+len(values)+1), len(values))
                           if all(a <= b for a, b in zip(ordered, target)))
            original = values.copy()
            self.assertEqual(min_increment_unique(values), expected)
            self.assertEqual(values, original)
