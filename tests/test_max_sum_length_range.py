import random
import unittest

from arrays.max_sum_length_range import max_sum_length_range


class TestMaxSumLengthRange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_length_range([1, -2, 3, 4, -1], 2, 3), 7)

    def test_edges(self):
        self.assertIsNone(max_sum_length_range([], 1, 2))
        self.assertEqual(max_sum_length_range([-5, -2, -3], 1, 2), -2)
        with self.assertRaises(ValueError): max_sum_length_range([1], 0, 1)
        with self.assertRaises(ValueError): max_sum_length_range([1], 3, 2)

    def test_against_reference(self):
        rng = random.Random(190)
        for _ in range(160):
            a = [rng.randrange(-8, 9) for _ in range(rng.randrange(15))]
            low = rng.randrange(1, 8)
            high = rng.randrange(low, 16)
            expected = max((sum(a[i:j]) for i in range(len(a)) for j in range(i+1, len(a)+1) if low <= j-i <= high), default=None)
            self.assertEqual(max_sum_length_range(a, low, high), expected)
