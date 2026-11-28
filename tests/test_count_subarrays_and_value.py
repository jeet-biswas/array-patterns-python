import random
import unittest

from arrays.count_subarrays_and_value import count_subarrays_and_value


class TestCountSubarraysAndValue(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays_and_value([1, 1, 1], 1), 6)
        self.assertEqual(count_subarrays_and_value([3, 2, 1], 0), 2)

    def test_edges(self):
        self.assertEqual(count_subarrays_and_value([], 0), 0)
        with self.assertRaises(ValueError): count_subarrays_and_value([-1], 0)
        with self.assertRaises(ValueError): count_subarrays_and_value([], -1)

    def test_against_reference(self):
        from functools import reduce
        from operator import and_
        rng = random.Random(311)
        for _ in range(170):
            a = [rng.randrange(64) for _ in range(rng.randrange(20))]
            target = rng.randrange(64)
            expected = sum(reduce(and_, a[i:j]) == target for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_subarrays_and_value(a, target), expected)
