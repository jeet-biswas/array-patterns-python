import random
import unittest

from arrays.count_equal_pairs import count_equal_pairs


class TestCountEqualPairs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_equal_pairs([1, 2, 3, 1, 1, 3]), 4)
        self.assertEqual(count_equal_pairs([2, 2, 2, 2]), 6)

    def test_edges(self):
        self.assertEqual(count_equal_pairs([]), 0)
        self.assertEqual(count_equal_pairs([1]), 0)
        self.assertEqual(count_equal_pairs([-2, -2, 0]), 1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(129)
        for _ in range(150):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(30))]
            self.assertEqual(count_equal_pairs(values), sum(a == b for a, b in combinations(values, 2)))
