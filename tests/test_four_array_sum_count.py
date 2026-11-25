import random
import unittest

from arrays.four_array_sum_count import four_array_sum_count


class TestFourArraySumCount(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(four_array_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)

    def test_edges(self):
        self.assertEqual(four_array_sum_count([], [0], [0], [0]), 0)
        self.assertEqual(four_array_sum_count([1, 1], [1], [1], [1], 4), 2)

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(217)
        for _ in range(140):
            arrays = [[rng.randrange(-4, 5) for _ in range(rng.randrange(6))] for _ in range(4)]
            target = rng.randrange(-8, 9)
            self.assertEqual(four_array_sum_count(*arrays, target), sum(sum(s) == target for s in product(*arrays)))
