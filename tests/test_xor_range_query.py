import random
import unittest

from arrays.xor_range_query import XorRangeQuery


class TestXorRangeQuery(unittest.TestCase):
    def test_examples(self):
        values = [1, 3, 4, 8]
        query = XorRangeQuery(values)
        self.assertEqual(query.query(1, 4), 15)
        values[1] = 99
        self.assertEqual(query.query(1, 4), 15)

    def test_edges(self):
        self.assertEqual(XorRangeQuery([]).query(0, 0), 0)
        query = XorRangeQuery([2, 3])
        self.assertEqual(query.query(1, 1), 0)
        for start, stop in [(-1, 1), (2, 1), (0, 3)]:
            with self.assertRaises(IndexError):
                query.query(start, stop)

    def test_against_reference(self):
        from functools import reduce
        from operator import xor
        rng = random.Random(107)
        for _ in range(50):
            values = [rng.randrange(-8, 16) for _ in range(rng.randrange(20))]
            query = XorRangeQuery(values)
            for start in range(len(values)+1):
                for stop in range(start, len(values)+1):
                    self.assertEqual(query.query(start, stop), reduce(xor, values[start:stop], 0))
