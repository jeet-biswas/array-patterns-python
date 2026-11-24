import random
import unittest

from arrays.longest_disjoint_bit_window import longest_disjoint_bit_window


class TestLongestDisjointBitWindow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_disjoint_bit_window([1, 3, 8, 48, 10]), 3)

    def test_edges(self):
        self.assertEqual(longest_disjoint_bit_window([]), 0)
        self.assertEqual(longest_disjoint_bit_window([0, 0, 0]), 3)
        with self.assertRaises(ValueError): longest_disjoint_bit_window([-1])

    def test_against_reference(self):
        rng = random.Random(183)
        for _ in range(150):
            a = [rng.randrange(32) for _ in range(rng.randrange(12))]
            expected = max((j-i for i in range(len(a)) for j in range(i+1, len(a)+1) if all(a[x] & a[y] == 0 for x in range(i, j) for y in range(x+1, j))), default=0)
            self.assertEqual(longest_disjoint_bit_window(a), expected)
