import random
import unittest

from arrays.can_split_same_average import can_split_same_average


class TestCanSplitSameAverage(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(can_split_same_average([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertFalse(can_split_same_average([3, 1]))

    def test_edges(self):
        self.assertFalse(can_split_same_average([]))
        self.assertFalse(can_split_same_average([0]))
        self.assertTrue(can_split_same_average([-1, 1, 0]))

    def test_against_reference(self):
        rng = random.Random(281)
        for _ in range(130):
            a = [rng.randrange(-7, 8) for _ in range(rng.randrange(12))]
            expected = any(sum(x for i, x in enumerate(a) if mask >> i & 1)*len(a) == sum(a)*mask.bit_count() for mask in range(1, (1 << len(a))-1))
            self.assertEqual(can_split_same_average(a), expected)
