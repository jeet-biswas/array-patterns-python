import random
import unittest

from arrays.sliding_window_max import sliding_window_max


class TestSlidingWindowMax(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(sliding_window_max([2, 2, 2], 2), [2, 2])

    def test_edges(self):
        self.assertEqual(sliding_window_max([-3, -1], 1), [-3, -1])
        self.assertEqual(sliding_window_max([-3, -1], 2), [-1])
        for values, size in [([], 1), ([1], 0), ([1], 2), ([1], -1)]:
            with self.assertRaises(ValueError):
                sliding_window_max(values, size)

    def test_against_brute_force(self):
        rng = random.Random(16)
        for _ in range(100):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 20))]
            size = rng.randrange(1, len(values)+1)
            expected = [max(values[i:i+size]) for i in range(len(values)-size+1)]
            self.assertEqual(sliding_window_max(values, size), expected)
