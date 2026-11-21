import random
import unittest

from arrays.recover_doubled_array import recover_doubled_array


class TestRecoverDoubledArray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(recover_doubled_array([1, 3, 4, 2, 6, 8]), [1, 3, 4])

    def test_edges(self):
        self.assertEqual(recover_doubled_array([]), [])
        self.assertEqual(recover_doubled_array([0, 0]), [0])
        self.assertIsNone(recover_doubled_array([0]))
        with self.assertRaises(ValueError): recover_doubled_array([-1, -2])

    def test_against_reference(self):
        from collections import Counter
        from itertools import combinations
        rng = random.Random(166)
        for _ in range(130):
            a = [rng.randrange(9) for _ in range(rng.randrange(9))]
            solutions = [s for s in combinations(a, len(a)//2) if len(a) % 2 == 0 and Counter(s + tuple(2*x for x in s)) == Counter(a)]
            before = a.copy()
            actual = recover_doubled_array(a)
            self.assertEqual(actual is not None, bool(solutions))
            if actual is not None:
                self.assertEqual(Counter(actual + [2*x for x in actual]), Counter(a))
                self.assertEqual(actual, sorted(actual))
            self.assertEqual(a, before)
