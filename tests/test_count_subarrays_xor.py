import random
import unittest

from arrays.count_subarrays_xor import count_subarrays_xor


class TestCountSubarraysXor(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays_xor([4, 2, 2, 6, 4], 6), 4)
        self.assertEqual(count_subarrays_xor([0, 0, 0], 0), 6)

    def test_edges(self):
        self.assertEqual(count_subarrays_xor([], 0), 0)
        self.assertEqual(count_subarrays_xor([-1], -1), 1)
        self.assertEqual(count_subarrays_xor([3], 0), 0)

    def test_against_reference(self):
        from functools import reduce
        from operator import xor
        rng = random.Random(105)
        for _ in range(150):
            values = [rng.randrange(-8, 16) for _ in range(rng.randrange(18))]
            target = rng.randrange(-8, 16)
            expected = sum(reduce(xor, values[i:j], 0) == target for i in range(len(values)) for j in range(i+1, len(values)+1))
            self.assertEqual(count_subarrays_xor(values, target), expected)
