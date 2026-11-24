import random
import unittest

from arrays.count_increasing_remainder_removals import count_increasing_remainder_removals


class TestCountIncreasingRemainderRemovals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_increasing_remainder_removals([6, 5, 7, 8]), 7)

    def test_edges(self):
        self.assertEqual(count_increasing_remainder_removals([]), 0)
        self.assertEqual(count_increasing_remainder_removals([1, 2, 3]), 6)
        self.assertEqual(count_increasing_remainder_removals([2, 2]), 3)

    def test_against_reference(self):
        from itertools import product
        for n in range(7):
            for values in product(range(3), repeat=n):
                a = list(values)
                expected = 0
                for i in range(n):
                    for j in range(i+1, n+1):
                        remaining = a[:i]+a[j:]
                        expected += all(x < y for x, y in zip(remaining, remaining[1:]))
                self.assertEqual(count_increasing_remainder_removals(a), expected)
