import random
import unittest

from arrays.car_pooling_feasible import car_pooling_feasible


class TestCarPoolingFeasible(unittest.TestCase):
    def test_examples(self):
        self.assertFalse(car_pooling_feasible([(2, 1, 5), (3, 3, 7)], 4))
        self.assertTrue(car_pooling_feasible([(2, 1, 5), (3, 5, 7)], 3))

    def test_edges(self):
        self.assertTrue(car_pooling_feasible([], 0))
        with self.assertRaises(ValueError): car_pooling_feasible([], -1)
        with self.assertRaises(ValueError): car_pooling_feasible([(1, 2, 2)], 4)

    def test_against_reference(self):
        rng = random.Random(177)
        for _ in range(150):
            trips = []
            for _ in range(rng.randrange(10)):
                start = rng.randrange(-5, 5)
                trips.append((rng.randrange(6), start, start+rng.randrange(1, 6)))
            capacity = rng.randrange(16)
            expected = all(sum(p for p, start, end in trips if start <= x < end) <= capacity for x in range(-5, 10))
            self.assertEqual(car_pooling_feasible(trips, capacity), expected)
