import random
import unittest

from arrays.min_circular_swaps_group_ones import min_circular_swaps_group_ones


class TestMinCircularSwapsGroupOnes(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_circular_swaps_group_ones([0, 1, 0, 1, 1, 0, 0]), 1)

    def test_edges(self):
        self.assertEqual(min_circular_swaps_group_ones([]), 0)
        self.assertEqual(min_circular_swaps_group_ones([1, 0, 0, 1]), 0)
        with self.assertRaises(ValueError): min_circular_swaps_group_ones([2])

    def test_against_reference(self):
        from itertools import product
        for n in range(1, 9):
            for bits in product((0, 1), repeat=n):
                width = sum(bits)
                targets = [{(start+j) % n for j in range(width)} for start in range(n)]
                expected = min(sum(bits[i] == 0 for i in target) for target in targets)
                self.assertEqual(min_circular_swaps_group_ones(list(bits)), expected)
