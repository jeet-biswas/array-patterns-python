import random
import unittest

from arrays.sliding_window_medians import sliding_window_medians


class TestSlidingWindowMedians(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sliding_window_medians([1, 3, -1, -3, 5, 3, 6, 7], 3), [1, -1, -1, 3, 5, 6])
        self.assertEqual(sliding_window_medians([1, 2, 3, 4], 2), [1.5, 2.5, 3.5])

    def test_edges(self):
        self.assertEqual(sliding_window_medians([2, 2, 2], 2), [2.0, 2.0])
        self.assertEqual(sliding_window_medians([-3, 5], 1), [-3.0, 5.0])
        for values, size in [([], 1), ([1], 0), ([1], 2)]:
            with self.assertRaises(ValueError):
                sliding_window_medians(values, size)

    def test_against_reference(self):
        from statistics import median
        rng = random.Random(103)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(1, 25))]
            size = rng.randrange(1, len(values)+1)
            original = values.copy()
            self.assertEqual(sliding_window_medians(values, size), [median(values[i:i+size]) for i in range(len(values)-size+1)])
            self.assertEqual(values, original)
