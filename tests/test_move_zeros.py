import random
import unittest

from arrays.move_zeros import move_zeros


class TestMoveZeros(unittest.TestCase):
    def test_examples(self):
        values = [0, 1, 0, 3, 12]
        self.assertIsNone(move_zeros(values))
        self.assertEqual(values, [1, 3, 12, 0, 0])

    def test_edges(self):
        for values in ([], [0, 0], [-2, 3]):
            original = values.copy()
            move_zeros(values)
            self.assertEqual(values, original)

    def test_against_filter(self):
        rng = random.Random(4)
        for _ in range(100):
            values = [rng.randrange(-2, 3) for _ in range(rng.randrange(20))]
            expected = [x for x in values if x] + [0] * values.count(0)
            move_zeros(values)
            self.assertEqual(values, expected)
