import random
import unittest

from arrays.can_partition_equal_subset import can_partition_equal_subset


class TestCanPartitionEqualSubset(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(can_partition_equal_subset([1, 5, 11, 5]))
        self.assertFalse(can_partition_equal_subset([1, 2, 3, 5]))

    def test_edges(self):
        self.assertTrue(can_partition_equal_subset([]))
        self.assertTrue(can_partition_equal_subset([0, 0]))
        self.assertFalse(can_partition_equal_subset([2]))
        with self.assertRaises(ValueError):
            can_partition_equal_subset([-1, 1])

    def test_against_reference(self):
        rng = random.Random(78)
        for _ in range(100):
            values = [rng.randrange(8) for _ in range(rng.randrange(11))]
            expected = any(2*sum(x for i, x in enumerate(values) if mask & (1 << i)) == sum(values)
                           for mask in range(1 << len(values)))
            self.assertEqual(can_partition_equal_subset(values), expected)
