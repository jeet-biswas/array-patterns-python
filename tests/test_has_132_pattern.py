import random
import unittest

from arrays.has_132_pattern import has_132_pattern


class TestHas132Pattern(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(has_132_pattern([3, 1, 4, 2]))
        self.assertFalse(has_132_pattern([1, 2, 3, 4]))

    def test_edges(self):
        self.assertFalse(has_132_pattern([]))
        self.assertFalse(has_132_pattern([1, 2, 2]))

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(169)
        for _ in range(180):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(13))]
            self.assertEqual(has_132_pattern(a), any(x < z < y for x, y, z in combinations(a, 3)))
