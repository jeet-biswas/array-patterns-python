import random
import unittest

from arrays.triangle_count import triangle_count


class TestTriangleCount(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(triangle_count([2, 2, 3, 4]), 3)
        self.assertEqual(triangle_count([4, 2, 3, 4]), 4)

    def test_edges(self):
        self.assertEqual(triangle_count([]), 0)
        self.assertEqual(triangle_count([0, 1, 1]), 0)
        self.assertEqual(triangle_count([1, 2, 3]), 0)
        with self.assertRaises(ValueError):
            triangle_count([2, -1, 3])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(83)
        for _ in range(150):
            values = [rng.randrange(10) for _ in range(rng.randrange(15))]
            original = values.copy()
            expected = sum(a+b > c and a+c > b and b+c > a for a, b, c in combinations(values, 3))
            self.assertEqual(triangle_count(values), expected)
            self.assertEqual(values, original)
