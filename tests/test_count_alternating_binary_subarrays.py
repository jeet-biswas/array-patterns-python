import random
import unittest

from arrays.count_alternating_binary_subarrays import count_alternating_binary_subarrays


class TestCountAlternatingBinarySubarrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_alternating_binary_subarrays([0, 1, 1, 1]), 5)

    def test_edges(self):
        self.assertEqual(count_alternating_binary_subarrays([]), 0)
        self.assertEqual(count_alternating_binary_subarrays([1, 0, 1]), 6)
        with self.assertRaises(ValueError): count_alternating_binary_subarrays([2])

    def test_against_reference(self):
        from itertools import product
        for n in range(8):
            for bits in product((0, 1), repeat=n):
                a = list(bits)
                expected = sum(all(a[k] != a[k+1] for k in range(i, j-1)) for i in range(n) for j in range(i+1, n+1))
                self.assertEqual(count_alternating_binary_subarrays(a), expected)
