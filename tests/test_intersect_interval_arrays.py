import random
import unittest

from arrays.intersect_interval_arrays import intersect_interval_arrays


class TestIntersectIntervalArrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(intersect_interval_arrays([(0, 2), (5, 10)], [(1, 5), (8, 12)]), [(1, 2), (5, 5), (8, 10)])

    def test_edges(self):
        self.assertEqual(intersect_interval_arrays([], [(1, 2)]), [])
        with self.assertRaises(ValueError): intersect_interval_arrays([(1, 2), (2, 3)], [])
        with self.assertRaises(ValueError): intersect_interval_arrays([], [(3, 2)])

    def test_against_reference(self):
        rng = random.Random(174)
        def make():
            result = []
            end = -10
            for _ in range(rng.randrange(8)):
                start = end+rng.randrange(1, 4)
                end = start+rng.randrange(4)
                result.append((start, end))
            return result
        for _ in range(150):
            a, b = make(), make()
            expected = sorted((max(x, u), min(y, v)) for x, y in a for u, v in b if max(x, u) <= min(y, v))
            self.assertEqual(intersect_interval_arrays(a, b), expected)
