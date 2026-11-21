import random
import unittest

from arrays.zero_filled_subarrays import zero_filled_subarrays


class TestZeroFilledSubarrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(zero_filled_subarrays([0, 0, 1, 0]), 4)

    def test_edges(self):
        self.assertEqual(zero_filled_subarrays([]), 0)
        self.assertEqual(zero_filled_subarrays([-1, 2]), 0)

    def test_against_reference(self):
        rng = random.Random(142)
        for _ in range(150):
            a = [rng.randrange(-1, 2) for _ in range(rng.randrange(15))]
            expected = sum(all(x == 0 for x in a[i:j]) for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(zero_filled_subarrays(a), expected)
