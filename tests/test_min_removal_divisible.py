import random
import unittest

from arrays.min_removal_divisible import min_removal_divisible


class TestMinRemovalDivisible(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_removal_divisible([3, 1, 4, 2], 6), 1)
        self.assertEqual(min_removal_divisible([6, 3, 5, 2], 9), 2)

    def test_edges(self):
        self.assertEqual(min_removal_divisible([], 3), 0)
        self.assertEqual(min_removal_divisible([1, 2, 3], 3), 0)
        self.assertEqual(min_removal_divisible([1, 2], 7), -1)
        with self.assertRaises(ValueError):
            min_removal_divisible([1], 0)

    def test_against_reference(self):
        rng = random.Random(88)
        for _ in range(150):
            values = [rng.randrange(-6, 7) for _ in range(rng.randrange(1, 15))]
            p = rng.randrange(1, 10)
            expected = min((j-i for i in range(len(values)+1) for j in range(i, len(values)+1)
                            if j-i < len(values) and (sum(values)-sum(values[i:j])) % p == 0), default=-1)
            self.assertEqual(min_removal_divisible(values, p), expected)
