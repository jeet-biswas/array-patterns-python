import random
import unittest

from arrays.plus_one import plus_one


class TestPlusOne(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(plus_one([1, 2, 9]), [1, 3, 0])
        self.assertEqual(plus_one([9, 9]), [1, 0, 0])

    def test_edges(self):
        self.assertEqual(plus_one([0]), [1])
        for digits in ([], [0, 1], [10], [-1]):
            with self.assertRaises(ValueError):
                plus_one(digits)

    def test_against_reference(self):
        rng = random.Random(62)
        for _ in range(150):
            number = rng.randrange(10**20)
            digits = [int(c) for c in str(number)]
            original = digits.copy()
            self.assertEqual(plus_one(digits), [int(c) for c in str(number+1)])
            self.assertEqual(digits, original)
