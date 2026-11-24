import random
import unittest

from arrays.max_distinct_window_sum import max_distinct_window_sum


class TestMaxDistinctWindowSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_distinct_window_sum([1, 5, 4, 2, 9, 9, 9], 3), 15)

    def test_edges(self):
        self.assertIsNone(max_distinct_window_sum([2, 2], 2))
        self.assertIsNone(max_distinct_window_sum([], 1))
        self.assertEqual(max_distinct_window_sum([-4, -2, -3], 2), -5)
        with self.assertRaises(ValueError): max_distinct_window_sum([], 0)

    def test_against_reference(self):
        rng = random.Random(184)
        for _ in range(150):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(13))]
            k = rng.randrange(1, 15)
            expected = max((sum(a[i:i+k]) for i in range(len(a)-k+1) if len(set(a[i:i+k])) == k), default=None)
            self.assertEqual(max_distinct_window_sum(a, k), expected)
