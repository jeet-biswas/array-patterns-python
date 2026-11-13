import random
import unittest

from arrays.inversion_count import inversion_count


class TestInversionCount(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(inversion_count([2, 4, 1, 3, 5]), 3)
        self.assertEqual(inversion_count([3, 2, 1]), 3)

    def test_edges(self):
        for values in ([], [1], [1, 2, 3], [2, 2, 2]):
            self.assertEqual(inversion_count(values), 0)
        self.assertEqual(inversion_count([-1, -2, -3]), 3)

    def test_against_pairs(self):
        rng = random.Random(34)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(25))]
            original = values.copy()
            expected = sum(values[i] > values[j] for i in range(len(values)) for j in range(i+1, len(values)))
            self.assertEqual(inversion_count(values), expected)
            self.assertEqual(values, original)
