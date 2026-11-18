import random
import unittest

from arrays.gas_station_start import gas_station_start


class TestGasStationStart(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(gas_station_start([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
        self.assertEqual(gas_station_start([2, 3, 4], [3, 4, 3]), -1)

    def test_edges(self):
        self.assertEqual(gas_station_start([], []), -1)
        self.assertEqual(gas_station_start([0], [0]), 0)
        self.assertEqual(gas_station_start([1], [2]), -1)
        for gas, cost in [([1], []), ([-1], [0]), ([0], [-1])]:
            with self.assertRaises(ValueError):
                gas_station_start(gas, cost)

    def test_against_reference(self):
        rng = random.Random(100)
        for _ in range(150):
            n = rng.randrange(15)
            gas = [rng.randrange(8) for _ in range(n)]
            cost = [rng.randrange(8) for _ in range(n)]
            valid = []
            for start in range(n):
                tank = 0
                for step in range(n):
                    i = (start+step) % n
                    tank += gas[i]-cost[i]
                    if tank < 0:
                        break
                else:
                    valid.append(start)
            actual = gas_station_start(gas, cost)
            self.assertIn(actual, valid if valid else [-1])
