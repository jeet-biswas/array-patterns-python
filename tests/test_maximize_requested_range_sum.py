import random
import unittest

from arrays.maximize_requested_range_sum import maximize_requested_range_sum


class TestMaximizeRequestedRangeSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximize_requested_range_sum([1, 2, 3, 4, 5], [(1, 4), (0, 2)]), 19)

    def test_edges(self):
        self.assertEqual(maximize_requested_range_sum([], [(0, 0)]), 0)
        self.assertEqual(maximize_requested_range_sum([-5, -2], [(0, 1)]), -2)
        with self.assertRaises(IndexError): maximize_requested_range_sum([1], [(0, 2)])

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(267)
        for _ in range(80):
            n = rng.randrange(8)
            a = [rng.randrange(-5, 6) for _ in range(n)]
            requests = [tuple(sorted((rng.randrange(n+1), rng.randrange(n+1)))) for _ in range(rng.randrange(8))]
            expected = max(sum(sum(order[left:right]) for left, right in requests) for order in permutations(a))
            self.assertEqual(maximize_requested_range_sum(a, requests), expected)
