import random
import unittest

from arrays.prefix_range_sum import PrefixRangeSum


class TestPrefixrangesum(unittest.TestCase):
    def test_examples(self):
        values = [2, -1, 3, 5]
        sums = PrefixRangeSum(values)
        self.assertEqual(sums.sum_range(1, 4), 7)
        values[1] = 100
        self.assertEqual(sums.sum_range(1, 4), 7)

    def test_edges(self):
        self.assertEqual(PrefixRangeSum([]).sum_range(0, 0), 0)
        sums = PrefixRangeSum([1, 2])
        self.assertEqual(sums.sum_range(2, 2), 0)
        for start, stop in [(-1, 1), (2, 1), (0, 3)]:
            with self.assertRaises(IndexError):
                sums.sum_range(start, stop)

    def test_against_slicing(self):
        rng = random.Random(8)
        for _ in range(30):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(15))]
            sums = PrefixRangeSum(values)
            for start in range(len(values) + 1):
                for stop in range(start, len(values) + 1):
                    self.assertEqual(sums.sum_range(start, stop), sum(values[start:stop]))
