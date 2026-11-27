import random
import unittest

from arrays.count_square_sum_permutations import count_square_sum_permutations


class TestCountSquareSumPermutations(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_square_sum_permutations([1, 17, 8]), 2)
        self.assertEqual(count_square_sum_permutations([2, 2, 2]), 1)

    def test_edges(self):
        self.assertEqual(count_square_sum_permutations([]), 1)
        self.assertEqual(count_square_sum_permutations([0, 0]), 1)
        self.assertEqual(count_square_sum_permutations([1, 1]), 0)
        with self.assertRaises(ValueError): count_square_sum_permutations([-1])

    def test_against_reference(self):
        from itertools import permutations
        from math import isqrt
        rng = random.Random(286)
        for _ in range(100):
            a = [rng.choice([0, 1, 2, 3, 6, 8, 10, 17]) for _ in range(rng.randrange(8))]
            expected = sum(all(isqrt(x+y)**2 == x+y for x, y in zip(order, order[1:])) for order in set(permutations(a)))
            self.assertEqual(count_square_sum_permutations(a), expected)
