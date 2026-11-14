import random
import unittest

from arrays.longest_ones_after_flips import longest_ones_after_flips


class TestLongestOnesAfterFlips(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_ones_after_flips([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)
        self.assertEqual(longest_ones_after_flips([0, 1, 1, 0], 0), 2)

    def test_edges(self):
        self.assertEqual(longest_ones_after_flips([], 2), 0)
        self.assertEqual(longest_ones_after_flips([0, 0], 10), 2)
        for values, flips in [([1], -1), ([2], 1)]:
            with self.assertRaises(ValueError):
                longest_ones_after_flips(values, flips)

    def test_against_reference(self):
        rng = random.Random(49)
        for _ in range(150):
            values = [rng.randrange(2) for _ in range(rng.randrange(18))]
            flips = rng.randrange(6)
            expected = max((j-i for i in range(len(values)) for j in range(i+1, len(values)+1)
                            if values[i:j].count(0) <= flips), default=0)
            self.assertEqual(longest_ones_after_flips(values, flips), expected)
