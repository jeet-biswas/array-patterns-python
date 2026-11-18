import random
import unittest

from arrays.min_end_removals_sum import min_end_removals_sum


class TestMinEndRemovalsSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_end_removals_sum([1, 1, 4, 2, 3], 5), 2)
        self.assertEqual(min_end_removals_sum([3, 2, 20, 1, 1, 3], 10), 5)

    def test_edges(self):
        self.assertEqual(min_end_removals_sum([], 0), 0)
        self.assertEqual(min_end_removals_sum([], 1), -1)
        self.assertEqual(min_end_removals_sum([1, 2], 3), 2)
        self.assertEqual(min_end_removals_sum([0, 0], 0), 0)

    def test_against_reference(self):
        rng = random.Random(89)
        for _ in range(150):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(15))]
            target = rng.randrange(-10, 11)
            n = len(values)
            expected = min((left+right for left in range(n+1) for right in range(n-left+1)
                            if sum(values[:left])+sum(values[n-right:]) == target), default=-1)
            self.assertEqual(min_end_removals_sum(values, target), expected)
