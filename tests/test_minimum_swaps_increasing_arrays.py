import random
import unittest

from arrays.minimum_swaps_increasing_arrays import minimum_swaps_increasing_arrays


class TestMinimumSwapsIncreasingArrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_swaps_increasing_arrays([1, 3, 5, 4], [1, 2, 3, 7]), 1)

    def test_edges(self):
        self.assertEqual(minimum_swaps_increasing_arrays([], []), 0)
        self.assertIsNone(minimum_swaps_increasing_arrays([2, 1], [2, 1]))
        with self.assertRaises(ValueError): minimum_swaps_increasing_arrays([1], [])

    def test_against_reference(self):
        rng = random.Random(268)
        for _ in range(140):
            n = rng.randrange(9)
            a = [rng.randrange(-3, 9) for _ in range(n)]
            b = [rng.randrange(-3, 9) for _ in range(n)]
            costs = []
            for mask in range(1 << n):
                x = [b[i] if mask >> i & 1 else a[i] for i in range(n)]
                y = [a[i] if mask >> i & 1 else b[i] for i in range(n)]
                if all(x[i] < x[i+1] and y[i] < y[i+1] for i in range(n-1)): costs.append(mask.bit_count())
            self.assertEqual(minimum_swaps_increasing_arrays(a, b), min(costs, default=None))
