import random
import unittest

from arrays.furthest_reachable_building import furthest_reachable_building


class TestFurthestReachableBuilding(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(furthest_reachable_building([4, 2, 7, 6, 9, 14, 12], 5, 1), 4)

    def test_edges(self):
        self.assertEqual(furthest_reachable_building([], 0, 0), -1)
        self.assertEqual(furthest_reachable_building([3, 2, 1], 0, 0), 2)
        with self.assertRaises(ValueError): furthest_reachable_building([1], -1, 0)
        with self.assertRaises(ValueError): furthest_reachable_building([-1], 0, 0)

    def test_against_reference(self):
        rng = random.Random(199)
        for _ in range(140):
            a = [rng.randrange(15) for _ in range(rng.randrange(11))]
            bricks, ladders = rng.randrange(20), rng.randrange(4)
            best = -1
            for end in range(len(a)):
                climbs = [max(0, a[i+1]-a[i]) for i in range(end)]
                feasible = any(mask.bit_count() <= ladders and sum(x for i, x in enumerate(climbs) if not mask >> i & 1) <= bricks for mask in range(1 << len(climbs)))
                if feasible: best = end
            self.assertEqual(furthest_reachable_building(a, bricks, ladders), best)
