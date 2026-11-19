import random
import unittest

from arrays.shortest_subarray_or import shortest_subarray_or


class TestShortestSubarrayOr(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_subarray_or([1, 2, 4], 7), 3)
        self.assertEqual(shortest_subarray_or([2, 1, 8], 6), 1)

    def test_edges(self):
        self.assertEqual(shortest_subarray_or([], 1), 0)
        self.assertEqual(shortest_subarray_or([0, 0], 1), 0)
        self.assertEqual(shortest_subarray_or([1, 1], 2), 0)
        for values, target in [([-1], 1), ([1], 0)]:
            with self.assertRaises(ValueError):
                shortest_subarray_or(values, target)

    def test_against_reference(self):
        from functools import reduce
        from operator import or_
        rng = random.Random(108)
        for _ in range(150):
            values = [rng.randrange(32) for _ in range(rng.randrange(15))]
            target = rng.randrange(1, 65)
            expected = min((j-i for i in range(len(values)) for j in range(i+1, len(values)+1)
                            if reduce(or_, values[i:j], 0) >= target), default=0)
            self.assertEqual(shortest_subarray_or(values, target), expected)
