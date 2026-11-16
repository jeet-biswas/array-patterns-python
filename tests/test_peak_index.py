import random
import unittest

from arrays.peak_index import peak_index


class TestPeakIndex(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(peak_index([1, 2, 3, 1]), 2)
        self.assertIn(peak_index([1, 2, 1, 3, 1]), (1, 3))

    def test_edges(self):
        self.assertEqual(peak_index([]), -1)
        self.assertEqual(peak_index([-4]), 0)
        self.assertEqual(peak_index([1, 2, 3]), 2)
        self.assertEqual(peak_index([3, 2, 1]), 0)

    def test_against_reference(self):
        rng = random.Random(59)
        for _ in range(150):
            values = []
            for _ in range(rng.randrange(1, 30)):
                candidates = [x for x in range(-6, 7) if not values or x != values[-1]]
                values.append(rng.choice(candidates))
            i = peak_index(values)
            self.assertTrue(0 <= i < len(values))
            self.assertTrue(i == 0 or values[i] > values[i-1])
            self.assertTrue(i == len(values)-1 or values[i] > values[i+1])
