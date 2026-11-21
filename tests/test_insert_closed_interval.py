import random
import unittest

from arrays.insert_closed_interval import insert_closed_interval


class TestInsertClosedInterval(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(insert_closed_interval([(1, 3), (6, 9)], (2, 5)), [(1, 5), (6, 9)])

    def test_edges(self):
        self.assertEqual(insert_closed_interval([], (1, 1)), [(1, 1)])
        with self.assertRaises(ValueError): insert_closed_interval([(2, 1)], (0, 1))
        with self.assertRaises(ValueError): insert_closed_interval([], (2, 1))

    def test_against_reference(self):
        rng = random.Random(175)
        for _ in range(120):
            a = []
            end = -10
            for _ in range(rng.randrange(8)):
                start = end+rng.randrange(1, 4)
                end = start+rng.randrange(4)
                a.append((start, end))
            new = tuple(sorted((rng.randrange(-12, 20), rng.randrange(-12, 20))))
            # Half-unit grid preserves both endpoint contacts and gaps between integer intervals.
            points = {p for x, y in a+[new] for p in range(2*x, 2*y+1)}
            runs = []
            for p in sorted(points):
                if not runs or p > runs[-1][1]+1: runs.append([p, p])
                else: runs[-1][1] = p
            expected = [(x//2, y//2) for x, y in runs]
            self.assertEqual(insert_closed_interval(a, new), expected)
