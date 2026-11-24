import random
import unittest

from arrays.minimum_refuel_stops import minimum_refuel_stops


class TestMinimumRefuelStops(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_refuel_stops(100, 10, [(10, 60), (20, 30), (30, 30), (60, 40)]), 2)

    def test_edges(self):
        self.assertEqual(minimum_refuel_stops(0, 0, []), 0)
        self.assertEqual(minimum_refuel_stops(10, 0, []), -1)
        self.assertEqual(minimum_refuel_stops(5, 0, [(0, 5)]), 1)
        with self.assertRaises(ValueError): minimum_refuel_stops(10, 1, [(2, 2), (1, 2)])
        with self.assertRaises(ValueError): minimum_refuel_stops(1, -1, [])

    def test_against_reference(self):
        rng = random.Random(198)
        for _ in range(140):
            target, fuel = rng.randrange(16), rng.randrange(10)
            stations = sorted((rng.randrange(16), rng.randrange(9)) for _ in range(rng.randrange(9)))
            best = None
            for mask in range(1 << len(stations)):
                reach, used = fuel, 0
                for i, (position, amount) in enumerate(stations):
                    if reach >= target: break
                    if mask >> i & 1:
                        if position > reach: break
                        reach += amount
                        used += 1
                if reach >= target: best = used if best is None else min(best, used)
            self.assertEqual(minimum_refuel_stops(target, fuel, stations), -1 if best is None else best)
