import random
import unittest

from arrays.array_leaders import array_leaders


class TestArrayLeaders(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(array_leaders([16, 17, 4, 3, 5, 2]), [17, 5, 2])
        self.assertEqual(array_leaders([3, 3]), [3])

    def test_edges(self):
        self.assertEqual(array_leaders([]), [])
        self.assertEqual(array_leaders([-3, -2, -1]), [-1])
        self.assertEqual(array_leaders([3, 2, 1]), [3, 2, 1])

    def test_against_brute_force(self):
        rng = random.Random(11)
        for _ in range(100):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(20))]
            expected = [x for i, x in enumerate(values) if all(x > y for y in values[i+1:])]
            self.assertEqual(array_leaders(values), expected)
