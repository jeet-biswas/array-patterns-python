import random
import unittest

from arrays.count_subarrays_below_score import count_subarrays_below_score


class TestCountSubarraysBelowScore(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subarrays_below_score([2, 1, 4, 3, 5], 10), 6)

    def test_edges(self):
        self.assertEqual(count_subarrays_below_score([0, 0], 1), 3)
        self.assertEqual(count_subarrays_below_score([0], 0), 0)
        with self.assertRaises(ValueError): count_subarrays_below_score([-1], 1)

    def test_against_reference(self):
        rng = random.Random(273)
        for _ in range(170):
            a = [rng.randrange(9) for _ in range(rng.randrange(15))]
            limit = rng.randrange(-3, 100)
            expected = sum(sum(a[i:j])*(j-i) < limit for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_subarrays_below_score(a, limit), expected)
