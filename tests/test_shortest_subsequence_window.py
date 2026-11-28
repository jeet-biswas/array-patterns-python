import random
import unittest

from arrays.shortest_subsequence_window import shortest_subsequence_window


class TestShortestSubsequenceWindow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_subsequence_window([1, 2, 3, 4, 2, 3, 4], [2, 4]), (1, 4))

    def test_edges(self):
        self.assertEqual(shortest_subsequence_window([], []), (0, 0))
        self.assertIsNone(shortest_subsequence_window([1], [1, 1]))

    def test_against_reference(self):
        rng = random.Random(306)
        for _ in range(160):
            a = [rng.randrange(4) for _ in range(rng.randrange(14))]
            pattern = [rng.randrange(4) for _ in range(rng.randrange(6))]
            def contains(window):
                at = 0
                for x in window:
                    if at < len(pattern) and x == pattern[at]: at += 1
                return at == len(pattern)
            candidates = [(j-i, i, j) for i in range(len(a)+1) for j in range(i, len(a)+1) if contains(a[i:j])]
            self.assertEqual(shortest_subsequence_window(a, pattern), min(candidates)[1:] if candidates else None)
