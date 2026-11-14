import random
import unittest

from arrays.subarrays_exactly_k_distinct import subarrays_exactly_k_distinct


class TestSubarraysExactlyKDistinct(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(subarrays_exactly_k_distinct([1, 2, 1, 2, 3], 2), 7)
        self.assertEqual(subarrays_exactly_k_distinct([1, 1, 1], 1), 6)

    def test_edges(self):
        self.assertEqual(subarrays_exactly_k_distinct([], 1), 0)
        self.assertEqual(subarrays_exactly_k_distinct([1, 2], 0), 0)
        self.assertEqual(subarrays_exactly_k_distinct([1], 3), 0)
        with self.assertRaises(ValueError):
            subarrays_exactly_k_distinct([1], -1)

    def test_against_reference(self):
        rng = random.Random(50)
        for _ in range(150):
            values = [rng.randrange(-2, 4) for _ in range(rng.randrange(15))]
            k = rng.randrange(8)
            expected = sum(len(set(values[i:j])) == k for i in range(len(values))
                           for j in range(i+1, len(values)+1))
            self.assertEqual(subarrays_exactly_k_distinct(values, k), expected)
