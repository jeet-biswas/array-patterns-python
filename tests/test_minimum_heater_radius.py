import random
import unittest

from arrays.minimum_heater_radius import minimum_heater_radius


class TestMinimumHeaterRadius(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_heater_radius([1, 2, 3, 4], [1, 4]), 1)

    def test_edges(self):
        self.assertEqual(minimum_heater_radius([], []), 0)
        self.assertIsNone(minimum_heater_radius([1], []))
        self.assertEqual(minimum_heater_radius([-5, 5], [0]), 5)

    def test_against_reference(self):
        rng = random.Random(326)
        for _ in range(180):
            houses = [rng.randrange(-100, 101) for _ in range(rng.randrange(30))]
            heaters = [rng.randrange(-100, 101) for _ in range(rng.randrange(15))]
            expected = 0 if not houses else None if not heaters else max(min(abs(h-t) for t in heaters) for h in houses)
            self.assertEqual(minimum_heater_radius(houses, heaters), expected)
