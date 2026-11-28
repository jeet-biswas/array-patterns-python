import random
import unittest

from arrays.count_triplets_target_multiplicity import count_triplets_target_multiplicity


class TestCountTripletsTargetMultiplicity(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_triplets_target_multiplicity([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8), 20)

    def test_edges(self):
        self.assertEqual(count_triplets_target_multiplicity([], 0), 0)
        self.assertEqual(count_triplets_target_multiplicity([0]*5, 0), 10)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(322)
        for _ in range(180):
            a = [rng.randrange(-6, 7) for _ in range(rng.randrange(24))]
            target = rng.randrange(-15, 16)
            self.assertEqual(count_triplets_target_multiplicity(a, target), sum(sum(s) == target for s in combinations(a, 3)))
