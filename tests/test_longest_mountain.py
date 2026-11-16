import random
import unittest

from arrays.longest_mountain import longest_mountain


class TestLongestMountain(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_mountain([2, 1, 4, 7, 3, 2, 5]), 5)
        self.assertEqual(longest_mountain([1, 3, 2, 4, 5, 1]), 4)

    def test_edges(self):
        for values in ([], [1, 2], [1, 2, 3], [3, 2, 1], [2, 2, 2], [1, 2, 2, 1]):
            self.assertEqual(longest_mountain(values), 0)

    def test_against_reference(self):
        rng = random.Random(65)
        for _ in range(100):
            values = [rng.randrange(5) for _ in range(rng.randrange(12))]
            expected = 0
            for start in range(len(values)):
                for stop in range(start+3, len(values)+1):
                    for peak in range(start+1, stop-1):
                        if (all(values[i] < values[i+1] for i in range(start, peak))
                                and all(values[i] > values[i+1] for i in range(peak, stop-1))):
                            expected = max(expected, stop-start)
            self.assertEqual(longest_mountain(values), expected)
