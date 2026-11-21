import random
import unittest

from arrays.count_increasing_subarrays import count_increasing_subarrays


class TestCountIncreasingSubarrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_increasing_subarrays([1, 2, 3, 2, 4]), 9)

    def test_edges(self):
        self.assertEqual(count_increasing_subarrays([]), 0)
        self.assertEqual(count_increasing_subarrays([2, 2, 2]), 3)

    def test_against_reference(self):
        rng = random.Random(157)
        for _ in range(150):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(12))]
            expected = sum(all(a[k] < a[k+1] for k in range(i, j-1)) for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_increasing_subarrays(a), expected)
