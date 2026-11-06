import random
import unittest

from arrays.rotate_right import rotate_right


class TestRotateRight(unittest.TestCase):
    def test_examples(self):
        values = [1, 2, 3, 4, 5]
        self.assertIsNone(rotate_right(values, 2))
        self.assertEqual(values, [4, 5, 1, 2, 3])

    def test_edges(self):
        for values, steps, expected in [([], 4, []), ([1], -9, [1]),
                                       ([1, 2, 3], -1, [2, 3, 1]),
                                       ([1, 2], 0, [1, 2])]:
            rotate_right(values, steps)
            self.assertEqual(values, expected)

    def test_against_slicing(self):
        rng = random.Random(3)
        for _ in range(100):
            values = list(range(rng.randrange(1, 20)))
            steps = rng.randrange(-100, 101)
            k = steps % len(values)
            expected = values[-k:] + values[:-k] if k else values.copy()
            rotate_right(values, steps)
            self.assertEqual(values, expected)
