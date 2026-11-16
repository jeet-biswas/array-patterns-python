import random
import unittest

from arrays.partition_disjoint import partition_disjoint


class TestPartitionDisjoint(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(partition_disjoint([5, 0, 3, 8, 6]), 3)
        self.assertEqual(partition_disjoint([1, 1, 1, 0, 6, 12]), 4)

    def test_edges(self):
        self.assertEqual(partition_disjoint([2, 2, 2]), 1)
        for values in ([], [1], [3, 2, 1]):
            self.assertIsNone(partition_disjoint(values))

    def test_against_reference(self):
        rng = random.Random(66)
        for _ in range(150):
            values = [rng.randrange(-6, 7) for _ in range(rng.randrange(20))]
            expected = next((i for i in range(1, len(values)) if max(values[:i]) <= min(values[i:])), None)
            self.assertEqual(partition_disjoint(values), expected)
