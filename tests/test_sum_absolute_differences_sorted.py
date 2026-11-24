import random
import unittest

from arrays.sum_absolute_differences_sorted import sum_absolute_differences_sorted


class TestSumAbsoluteDifferencesSorted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_absolute_differences_sorted([2, 3, 5]), [4, 3, 5])

    def test_edges(self):
        self.assertEqual(sum_absolute_differences_sorted([]), [])
        self.assertEqual(sum_absolute_differences_sorted([-2, -2, -2]), [0, 0, 0])
        with self.assertRaises(ValueError): sum_absolute_differences_sorted([2, 1])

    def test_against_reference(self):
        rng = random.Random(203)
        for _ in range(150):
            a = sorted(rng.randrange(-20, 21) for _ in range(rng.randrange(20)))
            self.assertEqual(sum_absolute_differences_sorted(a), [sum(abs(x-y) for y in a) for x in a])
