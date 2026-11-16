import random
import unittest

from arrays.max_sum_divisible_three import max_sum_divisible_three


class TestMaxSumDivisibleThree(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_divisible_three([3, 6, 5, 1, 8]), 18)
        self.assertEqual(max_sum_divisible_three([-1, 4]), 3)

    def test_edges(self):
        self.assertEqual(max_sum_divisible_three([]), 0)
        self.assertEqual(max_sum_divisible_three([4]), 0)
        self.assertEqual(max_sum_divisible_three([-3, -6]), 0)
        self.assertEqual(max_sum_divisible_three([0, 0]), 0)

    def test_against_reference(self):
        rng = random.Random(75)
        for _ in range(100):
            values = [rng.randrange(-5, 10) for _ in range(rng.randrange(11))]
            totals = [sum(x for i, x in enumerate(values) if mask & (1 << i))
                      for mask in range(1 << len(values))]
            self.assertEqual(max_sum_divisible_three(values), max(total for total in totals if total % 3 == 0))
