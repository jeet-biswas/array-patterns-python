import random
import unittest

from arrays.fenwick_range_sum import FenwickRangeSum


class TestFenwickRangeSum(unittest.TestCase):
    def test_examples(self):
        values = [1, 3, 5]
        query = FenwickRangeSum(values)
        self.assertEqual(query.query(0, 3), 9)
        self.assertIsNone(query.add(1, -2))
        self.assertEqual(query.query(0, 3), 7)
        self.assertEqual(values, [1, 3, 5])

    def test_edges(self):
        self.assertEqual(FenwickRangeSum([]).query(0, 0), 0)
        query = FenwickRangeSum([2])
        for index in (-1, 1):
            with self.assertRaises(IndexError):
                query.add(index, 1)
        for start, stop in [(-1, 1), (1, 0), (0, 2)]:
            with self.assertRaises(IndexError):
                query.query(start, stop)
        self.assertEqual(query.query(0, 1), 2)

    def test_against_reference(self):
        rng = random.Random(115)
        for _ in range(30):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 25))]
            query = FenwickRangeSum(values)
            for _ in range(100):
                if rng.randrange(2):
                    index, delta = rng.randrange(len(values)), rng.randrange(-5, 6)
                    values[index] += delta
                    query.add(index, delta)
                else:
                    start, stop = sorted((rng.randrange(len(values)+1), rng.randrange(len(values)+1)))
                    self.assertEqual(query.query(start, stop), sum(values[start:stop]))
