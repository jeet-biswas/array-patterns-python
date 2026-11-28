import random
import unittest

from arrays.count_triplets_below_sum import count_triplets_below_sum


class TestCountTripletsBelowSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_triplets_below_sum([-2, 0, 1, 3], 2), 2)

    def test_edges(self):
        self.assertEqual(count_triplets_below_sum([], 0), 0)
        self.assertEqual(count_triplets_below_sum([0, 0, 0, 0], 1), 4)
        self.assertEqual(count_triplets_below_sum([0, 0, 0], 0), 0)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(321)
        for _ in range(180):
            a = [rng.randrange(-10, 11) for _ in range(rng.randrange(20))]
            target = rng.randrange(-20, 21)
            self.assertEqual(count_triplets_below_sum(a, target), sum(sum(s) < target for s in combinations(a, 3)))
