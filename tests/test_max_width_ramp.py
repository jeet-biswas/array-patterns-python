import random
import unittest

from arrays.max_width_ramp import max_width_ramp


class TestMaxWidthRamp(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_width_ramp([6, 0, 8, 2, 1, 5]), 4)
        self.assertEqual(max_width_ramp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]), 7)

    def test_edges(self):
        self.assertEqual(max_width_ramp([]), 0)
        self.assertEqual(max_width_ramp([4]), 0)
        self.assertEqual(max_width_ramp([3, 2, 1]), 0)
        self.assertEqual(max_width_ramp([2, 2, 2]), 2)

    def test_against_reference(self):
        rng = random.Random(45)
        for _ in range(150):
            values = [rng.randrange(-7, 8) for _ in range(rng.randrange(25))]
            expected = max((j-i for i in range(len(values)) for j in range(i+1, len(values))
                            if values[i] <= values[j]), default=0)
            self.assertEqual(max_width_ramp(values), expected)
