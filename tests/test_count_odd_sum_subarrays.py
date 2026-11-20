import random
import unittest

from arrays.count_odd_sum_subarrays import count_odd_sum_subarrays


class TestCountOddSumSubarrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_odd_sum_subarrays([1, 3, 5]), 4)
        self.assertEqual(count_odd_sum_subarrays([2, 4, 6]), 0)

    def test_edges(self):
        self.assertEqual(count_odd_sum_subarrays([]), 0)
        self.assertEqual(count_odd_sum_subarrays([-1, 2]), 2)
        self.assertEqual(count_odd_sum_subarrays([0, 0]), 0)

    def test_against_reference(self):
        rng = random.Random(128)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(25))]
            expected = sum(sum(values[i:j]) % 2 == 1 for i in range(len(values)) for j in range(i+1, len(values)+1))
            self.assertEqual(count_odd_sum_subarrays(values), expected)
