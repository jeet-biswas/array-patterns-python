import random
import unittest

from arrays.compact_sorted import compact_sorted


class TestCompactSorted(unittest.TestCase):
    def test_examples(self):
        values = [1, 1, 2, 2, 3]
        count = compact_sorted(values)
        self.assertEqual(count, 3)
        self.assertEqual(values[:count], [1, 2, 3])

    def test_edges(self):
        self.assertEqual(compact_sorted([]), 0)
        values = [4, 4, 4]
        self.assertEqual(compact_sorted(values), 1)
        self.assertEqual(values[0], 4)

    def test_against_unique(self):
        rng = random.Random(5)
        for _ in range(100):
            values = sorted(rng.randrange(-4, 5) for _ in range(rng.randrange(20)))
            expected = sorted(set(values))
            count = compact_sorted(values)
            self.assertEqual(values[:count], expected)
