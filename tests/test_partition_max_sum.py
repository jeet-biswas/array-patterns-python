import random
import unittest

from arrays.partition_max_sum import partition_max_sum


class TestPartitionMaxSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(partition_max_sum([1, 15, 7, 9, 2, 5, 10], 3), 84)

    def test_edges(self):
        self.assertEqual(partition_max_sum([], 2), 0)
        self.assertEqual(partition_max_sum([-3, -1], 2), -2)
        with self.assertRaises(ValueError): partition_max_sum([1], 0)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(145)
        for _ in range(100):
            a = [rng.randrange(-5, 8) for _ in range(rng.randrange(9))]
            k = rng.randrange(1, 5)
            @lru_cache(None)
            def solve(i):
                return max((max(a[i:j])*(j-i)+solve(j) for j in range(i+1, min(len(a), i+k)+1)), default=0)
            self.assertEqual(partition_max_sum(a, k), solve(0))
