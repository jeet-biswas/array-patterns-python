import random
import unittest

from arrays.min_absolute_sum_difference import min_absolute_sum_difference


class TestMinAbsoluteSumDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_absolute_sum_difference([1, 7, 5], [2, 3, 5]), 3)
        self.assertEqual(min_absolute_sum_difference([-5, 0], [0, 0]), 0)

    def test_edges(self):
        self.assertEqual(min_absolute_sum_difference([], []), 0)
        self.assertEqual(min_absolute_sum_difference([3], [7]), 4)
        self.assertEqual(min_absolute_sum_difference([1, 2], [1, 2]), 0)
        with self.assertRaises(ValueError):
            min_absolute_sum_difference([1], [])

    def test_against_reference(self):
        rng = random.Random(140)
        for _ in range(150):
            n = rng.randrange(15)
            first, second = [rng.randrange(-10, 11) for _ in range(n)], [rng.randrange(-10, 11) for _ in range(n)]
            baseline = sum(abs(a-b) for a, b in zip(first, second))
            expected = min([baseline] + [sum(abs((value if j == i else first[j])-second[j]) for j in range(n))
                                        for i in range(n) for value in first])
            original = first.copy(), second.copy()
            self.assertEqual(min_absolute_sum_difference(first, second), expected)
            self.assertEqual((first, second), original)
