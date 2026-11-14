import random
import unittest

from arrays.shortest_subarray_signed import shortest_subarray_signed


class TestShortestSubarraySigned(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_subarray_signed([2, -1, 2], 3), 3)
        self.assertEqual(shortest_subarray_signed([84, -37, 32, 40, 95], 167), 3)

    def test_edges(self):
        self.assertEqual(shortest_subarray_signed([], 0), 0)
        self.assertEqual(shortest_subarray_signed([-5], -3), 0)
        self.assertEqual(shortest_subarray_signed([-2], -3), 1)
        self.assertEqual(shortest_subarray_signed([0], 0), 1)

    def test_against_reference(self):
        rng = random.Random(51)
        for _ in range(200):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(18))]
            target = rng.randrange(-8, 25)
            expected = min((j-i for i in range(len(values)) for j in range(i+1, len(values)+1)
                            if sum(values[i:j]) >= target), default=0)
            self.assertEqual(shortest_subarray_signed(values, target), expected)
