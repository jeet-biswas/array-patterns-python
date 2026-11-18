import random
import unittest

from arrays.max_sum_length_multiple import max_sum_length_multiple


class TestMaxSumLengthMultiple(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_length_multiple([1, 2, -1, 3, 4], 2), 8)
        self.assertEqual(max_sum_length_multiple([-5, -2, -3], 2), -5)

    def test_edges(self):
        self.assertIsNone(max_sum_length_multiple([], 1))
        self.assertIsNone(max_sum_length_multiple([1, 2], 3))
        self.assertEqual(max_sum_length_multiple([-1], 1), -1)
        with self.assertRaises(ValueError):
            max_sum_length_multiple([1], 0)

    def test_against_reference(self):
        rng = random.Random(97)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(18))]
            k = rng.randrange(1, 21)
            expected = max((sum(values[i:j]) for i in range(len(values)) for j in range(i+1, len(values)+1)
                            if (j-i) % k == 0), default=None)
            self.assertEqual(max_sum_length_multiple(values, k), expected)
