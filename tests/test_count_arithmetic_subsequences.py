import random
import unittest

from arrays.count_arithmetic_subsequences import count_arithmetic_subsequences


class TestCountArithmeticSubsequences(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_arithmetic_subsequences([2, 4, 6, 8, 10]), 7)

    def test_edges(self):
        self.assertEqual(count_arithmetic_subsequences([]), 0)
        self.assertEqual(count_arithmetic_subsequences([7, 7, 7, 7]), 5)

    def test_against_reference(self):
        rng = random.Random(160)
        for _ in range(120):
            a = [rng.randrange(-3, 4) for _ in range(rng.randrange(10))]
            expected = 0
            for mask in range(1 << len(a)):
                s = [x for i, x in enumerate(a) if mask >> i & 1]
                expected += len(s) >= 3 and len({y-x for x, y in zip(s, s[1:])}) == 1
            self.assertEqual(count_arithmetic_subsequences(a), expected)
