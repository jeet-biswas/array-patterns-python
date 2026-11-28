import random
import unittest

from arrays.max_xor_under_limits import max_xor_under_limits


class TestMaxXorUnderLimits(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_xor_under_limits([0, 1, 2, 3, 4], [(3, 1), (1, 3), (5, 6)]), [3, 3, 7])

    def test_edges(self):
        self.assertEqual(max_xor_under_limits([], [(1, 2)]), [None])
        self.assertEqual(max_xor_under_limits([0], [(0, -1), (0, 0)]), [None, 0])
        with self.assertRaises(ValueError): max_xor_under_limits([-1], [])
        with self.assertRaises(ValueError): max_xor_under_limits([], [(-1, 3)])

    def test_against_reference(self):
        rng = random.Random(314)
        for _ in range(140):
            a = [rng.randrange(128) for _ in range(rng.randrange(40))]
            queries = [(rng.randrange(256), rng.randrange(-3, 140)) for _ in range(25)]
            expected = [max((x ^ value for value in a if value <= limit), default=None) for x, limit in queries]
            self.assertEqual(max_xor_under_limits(a, queries), expected)
