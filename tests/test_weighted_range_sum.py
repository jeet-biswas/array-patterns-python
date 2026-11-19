import random
import unittest

from arrays.weighted_range_sum import WeightedRangeSum


class TestWeightedRangeSum(unittest.TestCase):
    def test_examples(self):
        values = [2, 3, 5, 7]
        query = WeightedRangeSum(values)
        self.assertEqual(query.query(1, 4), 34)
        values[1] = 100
        self.assertEqual(query.query(1, 4), 34)

    def test_edges(self):
        self.assertEqual(WeightedRangeSum([]).query(0, 0), 0)
        query = WeightedRangeSum([-2, 3])
        self.assertEqual(query.query(1, 1), 0)
        for start, stop in [(-1, 1), (2, 1), (0, 3)]:
            with self.assertRaises(IndexError):
                query.query(start, stop)

    def test_against_reference(self):
        rng = random.Random(113)
        for _ in range(50):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(20))]
            query = WeightedRangeSum(values)
            for start in range(len(values)+1):
                for stop in range(start, len(values)+1):
                    expected = sum((j+1)*x for j, x in enumerate(values[start:stop]))
                    self.assertEqual(query.query(start, stop), expected)
