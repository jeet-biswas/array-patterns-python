import random
import unittest

from arrays.max_subarray_one_square import max_subarray_one_square


class TestMaxSubarrayOneSquare(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_subarray_one_square([2, -1, -4, -3]), 17)

    def test_edges(self):
        self.assertEqual(max_subarray_one_square([-5]), 25)
        self.assertEqual(max_subarray_one_square([0, 0]), 0)
        with self.assertRaises(ValueError): max_subarray_one_square([])

    def test_against_reference(self):
        rng = random.Random(225)
        for _ in range(150):
            a = [rng.randrange(-8, 9) for _ in range(rng.randrange(1, 12))]
            expected = max(sum(a[i:j])-a[k]+a[k]**2 for i in range(len(a)) for j in range(i+1, len(a)+1) for k in range(i, j))
            self.assertEqual(max_subarray_one_square(a), expected)
