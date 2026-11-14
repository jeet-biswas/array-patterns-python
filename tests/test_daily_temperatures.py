import random
import unittest

from arrays.daily_temperatures import daily_temperatures


class TestDailyTemperatures(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(daily_temperatures([-2, -2, -1]), [2, 1, 0])

    def test_edges(self):
        self.assertEqual(daily_temperatures([]), [])
        self.assertEqual(daily_temperatures([30, 30]), [0, 0])
        self.assertEqual(daily_temperatures([3, 2, 1]), [0, 0, 0])

    def test_against_reference(self):
        rng = random.Random(43)
        for _ in range(100):
            values = [rng.randrange(-15, 41) for _ in range(rng.randrange(25))]
            expected = [next((j-i for j in range(i+1, len(values)) if values[j] > x), 0)
                        for i, x in enumerate(values)]
            self.assertEqual(daily_temperatures(values), expected)
