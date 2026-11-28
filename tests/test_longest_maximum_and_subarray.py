import random
import unittest

from arrays.longest_maximum_and_subarray import longest_maximum_and_subarray


class TestLongestMaximumAndSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_maximum_and_subarray([1, 2, 3, 3, 2, 2]), 2)

    def test_edges(self):
        self.assertEqual(longest_maximum_and_subarray([]), 0)
        self.assertEqual(longest_maximum_and_subarray([0, 0, 0]), 3)
        with self.assertRaises(ValueError): longest_maximum_and_subarray([-1])

    def test_against_reference(self):
        from functools import reduce
        from operator import and_
        rng = random.Random(310)
        for _ in range(150):
            a = [rng.randrange(16) for _ in range(rng.randrange(15))]
            candidates = [(reduce(and_, a[i:j]), j-i) for i in range(len(a)) for j in range(i+1, len(a)+1)]
            self.assertEqual(longest_maximum_and_subarray(a), max(candidates)[1] if candidates else 0)
