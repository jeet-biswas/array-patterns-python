import random
import unittest

from arrays.max_chunks_sorted import max_chunks_sorted


class TestMaxChunksSorted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_chunks_sorted([2, 1, 3, 4, 4]), 4)
        self.assertEqual(max_chunks_sorted([5, 4, 3, 2, 1]), 1)

    def test_edges(self):
        self.assertEqual(max_chunks_sorted([]), 0)
        self.assertEqual(max_chunks_sorted([2, 2, 2]), 3)
        self.assertEqual(max_chunks_sorted([-2, -1, 0]), 3)

    def test_against_reference(self):
        rng = random.Random(67)
        for _ in range(100):
            values = [rng.randrange(-3, 4) for _ in range(rng.randrange(1, 9))]
            expected = 0
            for mask in range(1 << (len(values)-1)):
                cuts = [0] + [i+1 for i in range(len(values)-1) if mask & (1 << i)] + [len(values)]
                merged = [x for a, b in zip(cuts, cuts[1:]) for x in sorted(values[a:b])]
                if merged == sorted(values):
                    expected = max(expected, len(cuts)-1)
            self.assertEqual(max_chunks_sorted(values), expected)
