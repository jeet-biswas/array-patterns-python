import random
import unittest

from arrays.maximum_distance_between_arrays import maximum_distance_between_arrays


class TestMaximumDistanceBetweenArrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximum_distance_between_arrays([[1, 2, 3], [4, 5], [1, 2, 3]]), 4)

    def test_edges(self):
        self.assertEqual(maximum_distance_between_arrays([[1, 100], [50]]), 50)
        with self.assertRaises(ValueError): maximum_distance_between_arrays([[1]])
        with self.assertRaises(ValueError): maximum_distance_between_arrays([[1], []])

    def test_against_reference(self):
        rng = random.Random(325)
        for _ in range(150):
            arrays = [sorted(rng.randrange(-30, 31) for _ in range(rng.randrange(1, 10))) for _ in range(rng.randrange(2, 8))]
            expected = max(abs(x-y) for i in range(len(arrays)) for j in range(i+1, len(arrays)) for x in arrays[i] for y in arrays[j])
            self.assertEqual(maximum_distance_between_arrays(arrays), expected)
