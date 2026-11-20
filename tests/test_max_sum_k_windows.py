import random
import unittest

from arrays.max_sum_k_windows import max_sum_k_windows


class TestMaxSumKWindows(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_k_windows([1, 2, -5, 4, 5, 0], 2, 2), 12)
        self.assertEqual(max_sum_k_windows([-5, -2, -3], 1, 2), -5)

    def test_edges(self):
        self.assertEqual(max_sum_k_windows([], 1, 0), 0)
        self.assertEqual(max_sum_k_windows([1, 2, 3, 4], 2, 2), 10)
        for width, count in [(0, 1), (1, -1), (2, 2)]:
            with self.assertRaises(ValueError):
                max_sum_k_windows([1, 2, 3], width, count)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(124)
        for _ in range(120):
            values = [rng.randrange(-6, 8) for _ in range(rng.randrange(1, 13))]
            width = rng.randrange(1, len(values)+1)
            count = rng.randrange(len(values)//width+1)
            expected = max(sum(sum(values[i:i+width]) for i in starts)
                           for starts in combinations(range(len(values)-width+1), count)
                           if all(a+width <= b for a, b in zip(starts, starts[1:])))
            self.assertEqual(max_sum_k_windows(values, width, count), expected)
