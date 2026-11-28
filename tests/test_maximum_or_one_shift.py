import random
import unittest

from arrays.maximum_or_one_shift import maximum_or_one_shift


class TestMaximumOrOneShift(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximum_or_one_shift([12, 9], 1), 30)

    def test_edges(self):
        self.assertEqual(maximum_or_one_shift([], 2), 0)
        self.assertEqual(maximum_or_one_shift([1, 2, 4], 0), 7)
        with self.assertRaises(ValueError): maximum_or_one_shift([1], -1)

    def test_against_reference(self):
        from functools import reduce
        from operator import or_
        rng = random.Random(316)
        for _ in range(160):
            a = [rng.randrange(128) for _ in range(rng.randrange(20))]
            shift = rng.randrange(12)
            expected = max((reduce(or_, (x << shift if i == j else x for j, x in enumerate(a)), 0) for i in range(len(a))), default=0)
            self.assertEqual(maximum_or_one_shift(a, shift), expected)
