import random
import unittest

from arrays.minimum_balanced_partition_difference import minimum_balanced_partition_difference


class TestMinimumBalancedPartitionDifference(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_balanced_partition_difference([3, 9, 7, 3]), 2)
        self.assertEqual(minimum_balanced_partition_difference([-36, 36]), 72)

    def test_edges(self):
        self.assertEqual(minimum_balanced_partition_difference([]), 0)
        self.assertEqual(minimum_balanced_partition_difference([10**30, 10**30+1]), 1)
        with self.assertRaises(ValueError): minimum_balanced_partition_difference([1])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(283)
        for _ in range(130):
            a = [rng.randrange(-20, 21) for _ in range(2*rng.randrange(7))]
            expected = min(abs(sum(a)-2*sum(s)) for s in combinations(a, len(a)//2))
            self.assertEqual(minimum_balanced_partition_difference(a), expected)
