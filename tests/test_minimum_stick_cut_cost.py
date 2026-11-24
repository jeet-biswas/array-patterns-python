import random
import unittest

from arrays.minimum_stick_cut_cost import minimum_stick_cut_cost


class TestMinimumStickCutCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_stick_cut_cost(7, [1, 3, 4, 5]), 16)

    def test_edges(self):
        self.assertEqual(minimum_stick_cut_cost(5, []), 0)
        self.assertEqual(minimum_stick_cut_cost(5, [2]), 5)
        with self.assertRaises(ValueError): minimum_stick_cut_cost(5, [2, 2])
        with self.assertRaises(ValueError): minimum_stick_cut_cost(5, [5])
        with self.assertRaises(ValueError): minimum_stick_cut_cost(0, [])

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(206)
        for _ in range(80):
            length = rng.randrange(2, 13)
            cuts = rng.sample(range(1, length), rng.randrange(min(6, length-1)+1))
            best = None
            for order in permutations(cuts):
                boundaries = [0, length]
                cost = 0
                for cut in order:
                    left = max(x for x in boundaries if x < cut)
                    right = min(x for x in boundaries if x > cut)
                    cost += right-left
                    boundaries.append(cut)
                best = cost if best is None else min(best, cost)
            before = cuts.copy()
            self.assertEqual(minimum_stick_cut_cost(length, cuts), best)
            self.assertEqual(cuts, before)
