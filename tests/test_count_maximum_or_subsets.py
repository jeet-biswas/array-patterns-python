import random
import unittest

from arrays.count_maximum_or_subsets import count_maximum_or_subsets


class TestCountMaximumOrSubsets(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_maximum_or_subsets([3, 1]), 2)
        self.assertEqual(count_maximum_or_subsets([2, 2, 2]), 7)

    def test_edges(self):
        self.assertEqual(count_maximum_or_subsets([]), 0)
        self.assertEqual(count_maximum_or_subsets([0, 0]), 3)
        with self.assertRaises(ValueError): count_maximum_or_subsets([-1])

    def test_against_reference(self):
        from functools import reduce
        from operator import or_
        rng = random.Random(307)
        for _ in range(130):
            a = [rng.randrange(32) for _ in range(rng.randrange(12))]
            target = reduce(or_, a, 0)
            expected = sum(reduce(or_, (x for i, x in enumerate(a) if mask >> i & 1), 0) == target for mask in range(1, 1 << len(a)))
            self.assertEqual(count_maximum_or_subsets(a), expected)
