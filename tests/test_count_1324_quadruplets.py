import random
import unittest

from arrays.count_1324_quadruplets import count_1324_quadruplets


class TestCount1324Quadruplets(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_1324_quadruplets([1, 3, 2, 4, 5]), 2)

    def test_edges(self):
        self.assertEqual(count_1324_quadruplets([]), 0)
        self.assertEqual(count_1324_quadruplets([1, 2, 2, 3]), 0)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(280)
        for _ in range(170):
            a = [rng.randrange(-6, 7) for _ in range(rng.randrange(14))]
            expected = sum(w < y < x < z for w, x, y, z in combinations(a, 4))
            self.assertEqual(count_1324_quadruplets(a), expected)
