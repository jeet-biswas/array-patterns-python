import random
import unittest

from arrays.add_digit_arrays import add_digit_arrays


class TestAddDigitArrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(add_digit_arrays([9, 9], [1]), [1, 0, 0])
        self.assertEqual(add_digit_arrays([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edges(self):
        self.assertEqual(add_digit_arrays([0], [0]), [0])
        for left, right in [([], [1]), ([1], [0, 1]), ([12], [1])]:
            with self.assertRaises(ValueError):
                add_digit_arrays(left, right)

    def test_against_reference(self):
        rng = random.Random(63)
        for _ in range(150):
            a, b = rng.randrange(10**20), rng.randrange(10**20)
            left, right = [int(c) for c in str(a)], [int(c) for c in str(b)]
            original = left.copy(), right.copy()
            self.assertEqual(add_digit_arrays(left, right), [int(c) for c in str(a+b)])
            self.assertEqual((left, right), original)
