import random
import unittest

from arrays.min_moves_equal import min_moves_equal


class TestMinMovesEqual(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_moves_equal([1, 10, 2, 9]), 16)
        self.assertEqual(min_moves_equal([-3, -1, 4]), 7)

    def test_edges(self):
        self.assertEqual(min_moves_equal([]), 0)
        self.assertEqual(min_moves_equal([9]), 0)
        self.assertEqual(min_moves_equal([4, 4, 4]), 0)

    def test_against_reference(self):
        rng = random.Random(69)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 20))]
            original = values.copy()
            expected = min(sum(abs(x-target) for x in values) for target in range(min(values), max(values)+1))
            self.assertEqual(min_moves_equal(values), expected)
            self.assertEqual(values, original)
