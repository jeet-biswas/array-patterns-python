import random
import unittest

from arrays.equal_range import equal_range


class TestEqualRange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(equal_range([1, 2, 2, 2, 4], 2), (1, 4))
        self.assertEqual(equal_range([1, 3, 5], 4), (2, 2))

    def test_edges(self):
        self.assertEqual(equal_range([], 1), (0, 0))
        self.assertEqual(equal_range([2, 2], 1), (0, 0))
        self.assertEqual(equal_range([2, 2], 3), (2, 2))

    def test_against_reference(self):
        from bisect import bisect_left, bisect_right
        rng = random.Random(57)
        for _ in range(150):
            values = sorted(rng.randrange(-6, 7) for _ in range(rng.randrange(30)))
            target = rng.randrange(-8, 9)
            self.assertEqual(equal_range(values, target), (bisect_left(values, target), bisect_right(values, target)))
