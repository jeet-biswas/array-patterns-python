import random
import unittest

from arrays.minimum_equal_group_removals import minimum_equal_group_removals


class TestMinimumEqualGroupRemovals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_equal_group_removals([2, 3, 3, 2, 2, 4, 2, 3, 4]), 4)

    def test_edges(self):
        self.assertEqual(minimum_equal_group_removals([]), 0)
        self.assertIsNone(minimum_equal_group_removals([1, 2, 2]))
        self.assertEqual(minimum_equal_group_removals([5]*4), 2)

    def test_against_reference(self):
        from collections import Counter
        from functools import lru_cache
        @lru_cache(None)
        def remove(count):
            if count == 0: return 0
            options = [remove(count-size) for size in (2, 3) if count >= size]
            return 1+min(options, default=float('inf'))
        rng = random.Random(275)
        for _ in range(180):
            a = [rng.randrange(5) for _ in range(rng.randrange(30))]
            expected = sum(remove(count) for count in Counter(a).values())
            self.assertEqual(minimum_equal_group_removals(a), None if expected == float('inf') else expected)
