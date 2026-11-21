import random
import unittest

from arrays.max_subarray_min_product import max_subarray_min_product


class TestMaxSubarrayMinProduct(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_subarray_min_product([1, 2, 3, 2]), 14)

    def test_edges(self):
        self.assertEqual(max_subarray_min_product([]), 0)
        self.assertEqual(max_subarray_min_product([2, 2, 2]), 12)
        with self.assertRaises(ValueError): max_subarray_min_product([-1])

    def test_against_reference(self):
        rng = random.Random(152)
        for _ in range(150):
            a = [rng.randrange(8) for _ in range(rng.randrange(12))]
            expected = max((sum(a[i:j])*min(a[i:j]) for i in range(len(a)) for j in range(i+1, len(a)+1)), default=0)
            self.assertEqual(max_subarray_min_product(a), expected)
