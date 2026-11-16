import random
import unittest

from arrays.duplicate_zeros import duplicate_zeros


class TestDuplicateZeros(unittest.TestCase):
    def test_examples(self):
        values = [1, 0, 2, 3, 0, 4, 5, 0]
        self.assertIsNone(duplicate_zeros(values))
        self.assertEqual(values, [1, 0, 0, 2, 3, 0, 0, 4])

    def test_edges(self):
        for values in ([], [0], [0, 0, 0], [1, 2, 3]):
            original = values.copy()
            duplicate_zeros(values)
            self.assertEqual(values, original)
        values = [1, 2, 0]
        duplicate_zeros(values)
        self.assertEqual(values, [1, 2, 0])

    def test_against_reference(self):
        rng = random.Random(60)
        for _ in range(150):
            values = [rng.randrange(-2, 3) for _ in range(rng.randrange(25))]
            expected = [part for value in values for part in ([0, 0] if value == 0 else [value])][:len(values)]
            duplicate_zeros(values)
            self.assertEqual(values, expected)
