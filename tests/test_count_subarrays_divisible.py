import random
import unittest

from arrays.count_subarrays_divisible import count_subarrays_divisible


class TestCountSubarraysDivisible(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays_divisible([4, 5, 0, -2, -3, 1], 5), 7)
        self.assertEqual(count_subarrays_divisible([-1, 2, 9], 2), 2)

    def test_edges(self):
        self.assertEqual(count_subarrays_divisible([], 3), 0)
        self.assertEqual(count_subarrays_divisible([0, 0, 0], 1), 6)
        for k in (0, -3):
            with self.assertRaises(ValueError):
                count_subarrays_divisible([1], k)

    def test_against_reference(self):
        rng = random.Random(47)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(16))]
            k = rng.randrange(1, 10)
            expected = sum(sum(values[i:j]) % k == 0 for i in range(len(values))
                           for j in range(i+1, len(values)+1))
            self.assertEqual(count_subarrays_divisible(values, k), expected)
