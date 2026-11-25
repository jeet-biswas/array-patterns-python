import random
import unittest

from arrays.max_spliced_array_sum import max_spliced_array_sum


class TestMaxSplicedArraySum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_spliced_array_sum([60, 60, 60], [10, 90, 10]), 210)

    def test_edges(self):
        self.assertEqual(max_spliced_array_sum([], []), 0)
        self.assertEqual(max_spliced_array_sum([-5], [-2]), -2)
        with self.assertRaises(ValueError): max_spliced_array_sum([1], [])

    def test_against_reference(self):
        rng = random.Random(226)
        for _ in range(140):
            n = rng.randrange(12)
            a = [rng.randrange(-9, 10) for _ in range(n)]
            b = [rng.randrange(-9, 10) for _ in range(n)]
            expected = max(max(sum(a[:i]+b[i:j]+a[j:]), sum(b[:i]+a[i:j]+b[j:])) for i in range(n+1) for j in range(i, n+1))
            self.assertEqual(max_spliced_array_sum(a, b), expected)
