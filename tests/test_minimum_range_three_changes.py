import random
import unittest

from arrays.minimum_range_three_changes import minimum_range_three_changes


class TestMinimumRangeThreeChanges(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_range_three_changes([1, 5, 0, 10, 14]), 1)
        self.assertEqual(minimum_range_three_changes([6, 6, 0, 1, 1, 4, 6]), 2)

    def test_edges(self):
        self.assertEqual(minimum_range_three_changes([]), 0)
        self.assertEqual(minimum_range_three_changes([5, 3, 2, 4]), 0)
        self.assertEqual(minimum_range_three_changes([2, 2, 2, 2, 2]), 0)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(141)
        for _ in range(150):
            values = [rng.randrange(-15, 16) for _ in range(rng.randrange(12))]
            candidates = []
            for count in range(min(3, len(values))+1):
                for changed in combinations(range(len(values)), count):
                    unchanged = [x for i, x in enumerate(values) if i not in changed]
                    candidates.append(max(unchanged)-min(unchanged) if unchanged else 0)
            original = values.copy()
            self.assertEqual(minimum_range_three_changes(values), min(candidates))
            self.assertEqual(values, original)
