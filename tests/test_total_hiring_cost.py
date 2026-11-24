import random
import unittest

from arrays.total_hiring_cost import total_hiring_cost


class TestTotalHiringCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(total_hiring_cost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4), 11)

    def test_edges(self):
        self.assertEqual(total_hiring_cost([], 0, 1), 0)
        self.assertEqual(total_hiring_cost([5, 1, 2], 3, 5), 8)
        with self.assertRaises(ValueError): total_hiring_cost([1], 2, 1)
        with self.assertRaises(ValueError): total_hiring_cost([1], 0, 0)
        with self.assertRaises(ValueError): total_hiring_cost([-1], 1, 1)

    def test_against_reference(self):
        rng = random.Random(200)
        for _ in range(180):
            costs = [rng.randrange(8) for _ in range(rng.randrange(15))]
            k, candidates = rng.randrange(len(costs)+1), rng.randrange(1, 18)
            remaining = list(range(len(costs)))
            expected = 0
            for _ in range(k):
                pool = set(remaining[:candidates]+remaining[-candidates:])
                chosen = min(pool, key=lambda i: (costs[i], i))
                expected += costs[chosen]
                remaining.remove(chosen)
            self.assertEqual(total_hiring_cost(costs, k, candidates), expected)
