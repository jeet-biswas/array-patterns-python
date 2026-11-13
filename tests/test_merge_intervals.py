import random
import unittest

from arrays.merge_intervals import merge_intervals


class TestMergeIntervals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(merge_intervals([(8, 10), (1, 3), (2, 6), (15, 18)]), [(1, 6), (8, 10), (15, 18)])
        self.assertEqual(merge_intervals([(1, 4), (4, 5), (2, 3)]), [(1, 5)])

    def test_edges(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([(1, 1), (2, 2)]), [(1, 1), (2, 2)])
        for intervals in [[(3, 1)], [(1,)], [(1, 2, 3)]]:
            with self.assertRaises(ValueError):
                merge_intervals(intervals)

    def test_coverage_and_disjointness(self):
        rng = random.Random(29)
        for _ in range(100):
            intervals = [tuple(sorted((rng.randrange(-5, 6), rng.randrange(-5, 6))))
                         for _ in range(rng.randrange(12))]
            original = intervals.copy()
            result = merge_intervals(intervals)
            self.assertEqual(intervals, original)
            self.assertTrue(all(result[i][1] < result[i+1][0] for i in range(len(result)-1)))
            # Integer and half-integer probes detect gaps between integer endpoints.
            for doubled in range(-12, 13):
                expected = any(2*a <= doubled <= 2*b for a, b in intervals)
                self.assertEqual(any(2*a <= doubled <= 2*b for a, b in result), expected)
