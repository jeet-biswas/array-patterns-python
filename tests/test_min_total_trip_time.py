import random
import unittest

from arrays.min_total_trip_time import min_total_trip_time


class TestMinTotalTripTime(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_total_trip_time([1, 2, 3], 5), 3)
        self.assertEqual(min_total_trip_time([2], 1), 2)

    def test_edges(self):
        self.assertEqual(min_total_trip_time([], 0), 0)
        self.assertEqual(min_total_trip_time([3, 3], 1), 3)
        for times, trips in [([], 1), ([0], 0), ([-1], 2), ([1], -1)]:
            with self.assertRaises(ValueError):
                min_total_trip_time(times, trips)

    def test_against_reference(self):
        rng = random.Random(137)
        for _ in range(150):
            times = [rng.randrange(1, 9) for _ in range(rng.randrange(1, 7))]
            trips = rng.randrange(20)
            expected = next(t for t in range(min(times)*trips+1) if sum(t // x for x in times) >= trips)
            self.assertEqual(min_total_trip_time(times, trips), expected)
