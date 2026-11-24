import random
import unittest

from arrays.max_unique_subarray_sum import max_unique_subarray_sum


class TestMaxUniqueSubarraySum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_unique_subarray_sum([4, 2, 4, 5, 6]), 17)

    def test_edges(self):
        self.assertEqual(max_unique_subarray_sum([]), 0)
        self.assertEqual(max_unique_subarray_sum([0, 0]), 0)
        with self.assertRaises(ValueError): max_unique_subarray_sum([-2])

    def test_against_reference(self):
        rng = random.Random(185)
        for _ in range(150):
            a = [rng.randrange(8) for _ in range(rng.randrange(13))]
            expected = max((sum(a[i:j]) for i in range(len(a)) for j in range(i+1, len(a)+1) if len(set(a[i:j])) == j-i), default=0)
            self.assertEqual(max_unique_subarray_sum(a), expected)
