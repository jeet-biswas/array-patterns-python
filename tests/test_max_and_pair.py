import random
import unittest

from arrays.max_and_pair import max_and_pair


class TestMaxAndPair(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_and_pair([4, 8, 12, 16]), 8)
        self.assertEqual(max_and_pair([7, 3, 5]), 5)

    def test_edges(self):
        self.assertEqual(max_and_pair([0, 0]), 0)
        self.assertEqual(max_and_pair([5, 5]), 5)
        self.assertEqual(max_and_pair([1 << 80, (1 << 80)+1]), 1 << 80)
        for values in ([], [1], [-1, 2]):
            with self.assertRaises(ValueError):
                max_and_pair(values)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(110)
        for _ in range(150):
            values = [rng.randrange(1024) for _ in range(rng.randrange(2, 25))]
            self.assertEqual(max_and_pair(values), max(a & b for a, b in combinations(values, 2)))
