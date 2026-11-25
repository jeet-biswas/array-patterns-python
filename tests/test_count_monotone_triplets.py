import random
import unittest

from arrays.count_monotone_triplets import count_monotone_triplets


class TestCountMonotoneTriplets(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_monotone_triplets([2, 5, 3, 4, 1]), 3)

    def test_edges(self):
        self.assertEqual(count_monotone_triplets([]), 0)
        self.assertEqual(count_monotone_triplets([2, 2, 2]), 0)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(215)
        for _ in range(140):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(15))]
            self.assertEqual(count_monotone_triplets(a), sum(x < y < z or x > y > z for x, y, z in combinations(a, 3)))
