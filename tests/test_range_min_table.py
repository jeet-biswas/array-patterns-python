import random
import unittest

from arrays.range_min_table import RangeMinTable


class TestRangeMinTable(unittest.TestCase):
    def test_examples(self):
        values = [4, 2, 7, -1, 5]
        query = RangeMinTable(values)
        self.assertEqual(query.query(1, 5), -1)
        self.assertEqual(query.query(0, 3), 2)
        values[1] = -100
        self.assertEqual(query.query(0, 3), 2)

    def test_edges(self):
        self.assertEqual(RangeMinTable([7]).query(0, 1), 7)
        for query, start, stop in [(RangeMinTable([]), 0, 0), (RangeMinTable([1]), 0, 0),
                                    (RangeMinTable([1]), -1, 1), (RangeMinTable([1]), 0, 2)]:
            with self.assertRaises(IndexError):
                query.query(start, stop)

    def test_against_reference(self):
        rng = random.Random(114)
        for _ in range(50):
            values = [rng.randrange(-20, 21) for _ in range(rng.randrange(1, 30))]
            query = RangeMinTable(values)
            for start in range(len(values)):
                for stop in range(start+1, len(values)+1):
                    self.assertEqual(query.query(start, stop), min(values[start:stop]))
