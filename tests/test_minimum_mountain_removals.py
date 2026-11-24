import random
import unittest

from arrays.minimum_mountain_removals import minimum_mountain_removals


class TestMinimumMountainRemovals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_mountain_removals([2, 1, 1, 5, 6, 2, 3, 1]), 3)

    def test_edges(self):
        self.assertIsNone(minimum_mountain_removals([]))
        self.assertIsNone(minimum_mountain_removals([1, 2, 3]))
        self.assertEqual(minimum_mountain_removals([1, 3, 1]), 0)

    def test_against_reference(self):
        rng = random.Random(195)
        for _ in range(110):
            a = [rng.randrange(-3, 5) for _ in range(rng.randrange(10))]
            longest = 0
            for mask in range(1 << len(a)):
                s = [x for i, x in enumerate(a) if mask >> i & 1]
                if any(all(s[i] < s[i+1] for i in range(p)) and all(s[i] > s[i+1] for i in range(p, len(s)-1)) for p in range(1, len(s)-1)):
                    longest = max(longest, len(s))
            self.assertEqual(minimum_mountain_removals(a), len(a)-longest if longest else None)
