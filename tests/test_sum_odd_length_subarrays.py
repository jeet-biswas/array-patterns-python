import random
import unittest

from arrays.sum_odd_length_subarrays import sum_odd_length_subarrays


class TestSumOddLengthSubarrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_odd_length_subarrays([1, 4, 2, 5, 3]), 58)
        self.assertEqual(sum_odd_length_subarrays([1, 2]), 3)

    def test_edges(self):
        self.assertEqual(sum_odd_length_subarrays([]), 0)
        self.assertEqual(sum_odd_length_subarrays([-5]), -5)
        self.assertEqual(sum_odd_length_subarrays([0, 0, 0]), 0)

    def test_against_reference(self):
        rng = random.Random(112)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(25))]
            expected = sum(sum(values[i:j]) for i in range(len(values)) for j in range(i+1, len(values)+1, 2))
            self.assertEqual(sum_odd_length_subarrays(values), expected)
