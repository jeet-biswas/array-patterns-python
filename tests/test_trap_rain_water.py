import random
import unittest

from arrays.trap_rain_water import trap_rain_water


class TestTrapRainWater(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap_rain_water([3, 0, 0, 3]), 6)

    def test_edges(self):
        for values in ([], [4], [1, 2, 3], [3, 2, 1]):
            self.assertEqual(trap_rain_water(values), 0)
        with self.assertRaises(ValueError):
            trap_rain_water([2, -1, 2])

    def test_against_brute_force(self):
        rng = random.Random(13)
        for _ in range(100):
            values = [rng.randrange(8) for _ in range(rng.randrange(15))]
            expected = sum(min(max(values[:i+1]), max(values[i:]))-x
                           for i, x in enumerate(values))
            self.assertEqual(trap_rain_water(values), expected)
