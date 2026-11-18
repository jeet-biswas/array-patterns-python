import random
import unittest

from arrays.min_adjacent_swaps_ones import min_adjacent_swaps_ones


class TestMinAdjacentSwapsOnes(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_adjacent_swaps_ones([1, 0, 0, 1]), 2)
        self.assertEqual(min_adjacent_swaps_ones([1, 0, 1, 0, 1]), 2)

    def test_edges(self):
        for values in ([], [0, 0], [1], [0, 1, 1, 0]):
            self.assertEqual(min_adjacent_swaps_ones(values), 0)
        with self.assertRaises(ValueError):
            min_adjacent_swaps_ones([1, 2])

    def test_against_reference(self):
        from itertools import product
        for n in range(9):
            for state in product((0, 1), repeat=n):
                positions = [i for i, value in enumerate(state) if value]
                width = len(positions)
                expected = min(sum(abs(position-(start+rank)) for rank, position in enumerate(positions))
                               for start in range(n-width+1))
                self.assertEqual(min_adjacent_swaps_ones(list(state)), expected)
