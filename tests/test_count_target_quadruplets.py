import random
import unittest

from arrays.count_target_quadruplets import count_target_quadruplets


class TestCountTargetQuadruplets(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_target_quadruplets([0, 0, 0, 0, 0], 0), 5)

    def test_edges(self):
        self.assertEqual(count_target_quadruplets([], 0), 0)
        self.assertEqual(count_target_quadruplets([1, 2, 3, 4], 10), 1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(216)
        for _ in range(150):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(13))]
            target = rng.randrange(-10, 11)
            self.assertEqual(count_target_quadruplets(a, target), sum(sum(s) == target for s in combinations(a, 4)))
