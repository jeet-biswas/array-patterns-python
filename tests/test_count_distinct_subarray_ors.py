import random
import unittest

from arrays.count_distinct_subarray_ors import count_distinct_subarray_ors


class TestCountDistinctSubarrayOrs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_distinct_subarray_ors([1, 2, 4]), 6)
        self.assertEqual(count_distinct_subarray_ors([1, 1, 2]), 3)

    def test_edges(self):
        self.assertEqual(count_distinct_subarray_ors([]), 0)
        self.assertEqual(count_distinct_subarray_ors([0, 0]), 1)
        self.assertEqual(count_distinct_subarray_ors([1 << 70]), 1)
        with self.assertRaises(ValueError):
            count_distinct_subarray_ors([-1])

    def test_against_reference(self):
        from functools import reduce
        from operator import or_
        rng = random.Random(109)
        for _ in range(150):
            values = [rng.randrange(64) for _ in range(rng.randrange(18))]
            expected = {reduce(or_, values[i:j], 0) for i in range(len(values)) for j in range(i+1, len(values)+1)}
            self.assertEqual(count_distinct_subarray_ors(values), len(expected))
