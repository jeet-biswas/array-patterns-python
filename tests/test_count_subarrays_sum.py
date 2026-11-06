import random
import unittest

from arrays.count_subarrays_sum import count_subarrays_sum


class TestCountSubarraysSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays_sum([1, 1, 1], 2), 2)
        self.assertEqual(count_subarrays_sum([1, -1, 0], 0), 3)

    def test_edges(self):
        self.assertEqual(count_subarrays_sum([], 0), 0)
        self.assertEqual(count_subarrays_sum([0, 0, 0], 0), 6)
        self.assertEqual(count_subarrays_sum([4], 4), 1)

    def test_against_brute_force(self):
        rng = random.Random(15)
        for _ in range(100):
            values = [rng.randrange(-3, 4) for _ in range(rng.randrange(15))]
            target = rng.randrange(-6, 7)
            expected = sum(sum(values[i:j]) == target for i in range(len(values))
                           for j in range(i+1, len(values)+1))
            self.assertEqual(count_subarrays_sum(values, target), expected)
