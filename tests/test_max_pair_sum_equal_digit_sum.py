import random
import unittest

from arrays.max_pair_sum_equal_digit_sum import max_pair_sum_equal_digit_sum


class TestMaxPairSumEqualDigitSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_pair_sum_equal_digit_sum([18, 43, 36, 13, 7]), 54)

    def test_edges(self):
        self.assertIsNone(max_pair_sum_equal_digit_sum([]))
        self.assertEqual(max_pair_sum_equal_digit_sum([-12, -21]), -33)
        self.assertEqual(max_pair_sum_equal_digit_sum([0, 0]), 0)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(318)
        for _ in range(170):
            a = [rng.randrange(-1000, 1001) for _ in range(rng.randrange(40))]
            def digits(x): return sum(map(int, str(abs(x))))
            expected = max((x+y for x, y in combinations(a, 2) if digits(x) == digits(y)), default=None)
            self.assertEqual(max_pair_sum_equal_digit_sum(a), expected)
