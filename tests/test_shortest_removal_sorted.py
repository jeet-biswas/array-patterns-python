import random
import unittest

from arrays.shortest_removal_sorted import shortest_removal_sorted


class TestShortestRemovalSorted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_removal_sorted([1, 2, 3, 10, 4, 2, 3, 5]), 3)

    def test_edges(self):
        self.assertEqual(shortest_removal_sorted([]), 0)
        self.assertEqual(shortest_removal_sorted([3, 2, 1]), 2)
        self.assertEqual(shortest_removal_sorted([1, 1]), 0)

    def test_against_reference(self):
        rng = random.Random(151)
        for _ in range(150):
            a = [rng.randrange(-3, 5) for _ in range(rng.randrange(12))]
            best = len(a)
            for i in range(len(a)+1):
                for j in range(i, len(a)+1):
                    remaining = a[:i]+a[j:]
                    if remaining == sorted(remaining): best = min(best, j-i)
            self.assertEqual(shortest_removal_sorted(a), best)
