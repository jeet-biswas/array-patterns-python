import random
import unittest

from arrays.minimum_travel_ticket_cost import minimum_travel_ticket_cost


class TestMinimumTravelTicketCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_travel_ticket_cost([1, 4, 6, 7, 8, 20], [2, 7, 15]), 11)

    def test_edges(self):
        self.assertEqual(minimum_travel_ticket_cost([], [1, 2, 3]), 0)
        self.assertEqual(minimum_travel_ticket_cost([1, 100], [0, 5, 8]), 0)
        with self.assertRaises(ValueError): minimum_travel_ticket_cost([1, 1], [1, 2, 3])
        with self.assertRaises(ValueError): minimum_travel_ticket_cost([], [1, 2])

    def test_against_reference(self):
        rng = random.Random(270)
        for _ in range(130):
            days = sorted(rng.sample(range(1, 61), rng.randrange(16)))
            costs = [rng.randrange(1, 21) for _ in range(3)]
            travel = set(days)
            dp = [0]*61
            for day in range(1, 61):
                dp[day] = dp[day-1] if day not in travel else min(dp[max(0, day-duration)]+price for duration, price in zip((1, 7, 30), costs))
            self.assertEqual(minimum_travel_ticket_cost(days, costs), dp[-1])
