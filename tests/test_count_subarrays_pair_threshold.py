import random
import unittest

from arrays.count_subarrays_pair_threshold import count_subarrays_pair_threshold


class TestCountSubarraysPairThreshold(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays_pair_threshold([1, 1, 1, 1, 1], 10), 1)
        self.assertEqual(count_subarrays_pair_threshold([1, 1, 1], 1), 3)

    def test_edges(self):
        self.assertEqual(count_subarrays_pair_threshold([], 0), 0)
        self.assertEqual(count_subarrays_pair_threshold([2, 3], 0), 3)
        with self.assertRaises(ValueError): count_subarrays_pair_threshold([], -1)

    def test_against_reference(self):
        rng = random.Random(154)
        for _ in range(120):
            a = [rng.randrange(4) for _ in range(rng.randrange(10))]
            k = rng.randrange(9)
            expected = 0
            for i in range(len(a)):
                for j in range(i+1, len(a)+1):
                    pairs = sum(a[x] == a[y] for x in range(i, j) for y in range(x+1, j))
                    expected += pairs >= k
            self.assertEqual(count_subarrays_pair_threshold(a, k), expected)
