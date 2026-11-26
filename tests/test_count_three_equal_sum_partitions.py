import random
import unittest

from arrays.count_three_equal_sum_partitions import count_three_equal_sum_partitions


class TestCountThreeEqualSumPartitions(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_three_equal_sum_partitions([1, 2, 3, 0, 3]), 2)

    def test_edges(self):
        self.assertEqual(count_three_equal_sum_partitions([]), 0)
        self.assertEqual(count_three_equal_sum_partitions([0, 0, 0, 0]), 3)
        self.assertEqual(count_three_equal_sum_partitions([-1, -1, -1]), 1)

    def test_against_reference(self):
        rng = random.Random(249)
        for _ in range(180):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(15))]
            expected = sum(sum(a[:i]) == sum(a[i:j]) == sum(a[j:]) for i in range(1, len(a)) for j in range(i+1, len(a)))
            self.assertEqual(count_three_equal_sum_partitions(a), expected)
