import random
import unittest

from arrays.subset_sum_count import subset_sum_count


class TestSubsetSumCount(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(subset_sum_count([1, 2, 3, 3], 6), 3)
        self.assertEqual(subset_sum_count([-1, 1, 0], 0), 4)

    def test_edges(self):
        self.assertEqual(subset_sum_count([], 0), 1)
        self.assertEqual(subset_sum_count([], 1), 0)
        self.assertEqual(subset_sum_count([0, 0, 0], 0), 8)
        self.assertEqual(subset_sum_count([1, 1], 1), 2)

    def test_against_reference(self):
        rng = random.Random(79)
        for _ in range(100):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(11))]
            target = rng.randrange(-8, 9)
            expected = sum(sum(x for i, x in enumerate(values) if mask & (1 << i)) == target
                           for mask in range(1 << len(values)))
            self.assertEqual(subset_sum_count(values, target), expected)
