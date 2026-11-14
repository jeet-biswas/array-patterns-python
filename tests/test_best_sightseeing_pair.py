import random
import unittest

from arrays.best_sightseeing_pair import best_sightseeing_pair


class TestBestSightseeingPair(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(best_sightseeing_pair([8, 1, 5, 2, 6]), 11)
        self.assertEqual(best_sightseeing_pair([-5, -1, -3]), -5)

    def test_edges(self):
        self.assertEqual(best_sightseeing_pair([1, 2]), 2)
        self.assertEqual(best_sightseeing_pair([0, 0, 0]), -1)
        for values in ([], [1]):
            with self.assertRaises(ValueError):
                best_sightseeing_pair(values)

    def test_against_reference(self):
        rng = random.Random(56)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(2, 25))]
            expected = max(values[i]+values[j]+i-j for i in range(len(values)) for j in range(i+1, len(values)))
            self.assertEqual(best_sightseeing_pair(values), expected)
