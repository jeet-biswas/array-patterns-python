import random
import unittest

from arrays.two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(two_sum([3, 3], 6), (0, 1))
        self.assertEqual(two_sum([-3, 0, 3], 0), (0, 2))

    def test_edges(self):
        for values in ([], [3], [1, 2]):
            self.assertIsNone(two_sum(values, 6))
        self.assertEqual(two_sum([1, 1, 3], 4), (0, 2))

    def test_against_brute_force(self):
        rng = random.Random(1)
        for _ in range(100):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(12))]
            target = rng.randrange(-8, 9)
            expected = next(((i, j) for j in range(len(values)) for i in range(j)
                             if values[i] + values[j] == target), None)
            original = values.copy()
            self.assertEqual(two_sum(values, target), expected)
            self.assertEqual(values, original)
