import random
import unittest

from arrays.longest_consecutive import longest_consecutive


class TestLongestConsecutive(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_consecutive([1, 2, 2, 3]), 3)

    def test_edges(self):
        self.assertEqual(longest_consecutive([]), 0)
        self.assertEqual(longest_consecutive([7]), 1)
        self.assertEqual(longest_consecutive([-2, -1, 0]), 3)

    def test_against_sort(self):
        rng = random.Random(14)
        for _ in range(100):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(25))]
            ordered = sorted(set(values))
            best = run = 0
            previous = None
            for value in ordered:
                run = run + 1 if previous is not None and value == previous + 1 else 1
                previous = value
                best = max(best, run)
            self.assertEqual(longest_consecutive(values), best)
