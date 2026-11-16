import random
import unittest

from arrays.arithmetic_slices import arithmetic_slices


class TestArithmeticSlices(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(arithmetic_slices([1, 2, 3, 4]), 3)
        self.assertEqual(arithmetic_slices([1, 3, 5, 8, 11]), 2)

    def test_edges(self):
        self.assertEqual(arithmetic_slices([]), 0)
        self.assertEqual(arithmetic_slices([1, 2]), 0)
        self.assertEqual(arithmetic_slices([7, 7, 7, 7]), 3)
        self.assertEqual(arithmetic_slices([3, 2, 1]), 1)

    def test_against_reference(self):
        rng = random.Random(74)
        for _ in range(150):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(18))]
            expected = sum(len({values[t+1]-values[t] for t in range(i, j-1)}) == 1
                           for i in range(len(values)) for j in range(i+3, len(values)+1))
            self.assertEqual(arithmetic_slices(values), expected)
