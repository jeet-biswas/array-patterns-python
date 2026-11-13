import random
import unittest

from arrays.min_swaps_group_ones import min_swaps_group_ones


class TestMinSwapsGroupOnes(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_swaps_group_ones([1, 0, 1, 0, 1]), 1)
        self.assertEqual(min_swaps_group_ones([1, 0, 0, 1]), 1)

    def test_edges(self):
        for values in ([], [0, 0], [1], [1, 1, 1], [0, 1, 1, 0]):
            self.assertEqual(min_swaps_group_ones(values), 0)
        with self.assertRaises(ValueError):
            min_swaps_group_ones([1, 2, 0])

    def test_against_exhaustive_target_states(self):
        from itertools import product
        for n in range(8):
            for state in product((0, 1), repeat=n):
                values = list(state)
                width = sum(values)
                expected = min((sum(x != int(start <= i < start+width)
                                    for i, x in enumerate(values)) // 2
                                for start in range(n-width+1)), default=0)
                self.assertEqual(min_swaps_group_ones(values), expected)
