import random
import unittest

from arrays.shortest_suffix_or_windows import shortest_suffix_or_windows


class TestShortestSuffixOrWindows(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_suffix_or_windows([1, 0, 2, 1, 3]), [3, 3, 2, 2, 1])

    def test_edges(self):
        self.assertEqual(shortest_suffix_or_windows([]), [])
        self.assertEqual(shortest_suffix_or_windows([0, 0]), [1, 1])
        with self.assertRaises(ValueError): shortest_suffix_or_windows([-1])

    def test_against_reference(self):
        from functools import reduce
        from operator import or_
        rng = random.Random(309)
        for _ in range(160):
            a = [rng.randrange(64) for _ in range(rng.randrange(20))]
            expected = []
            for i in range(len(a)):
                target = reduce(or_, a[i:], 0)
                expected.append(next(j-i for j in range(i+1, len(a)+1) if reduce(or_, a[i:j], 0) == target))
            self.assertEqual(shortest_suffix_or_windows(a), expected)
