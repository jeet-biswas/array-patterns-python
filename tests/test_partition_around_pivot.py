import random
import unittest

from arrays.partition_around_pivot import partition_around_pivot


class TestPartitionAroundPivot(unittest.TestCase):
    def test_examples(self):
        a = [3, 1, 2, 4, 2]
        self.assertEqual(partition_around_pivot(a, 2), (1, 3))
        self.assertEqual(a[1:3], [2, 2])

    def test_edges(self):
        self.assertEqual(partition_around_pivot([], 0), (0, 0))
        a = [1, 1]
        self.assertEqual(partition_around_pivot(a, 2), (2, 2))

    def test_against_reference(self):
        rng = random.Random(296)
        for _ in range(170):
            a = [rng.randrange(-8, 9) for _ in range(rng.randrange(80))]
            original = a.copy()
            pivot = rng.randrange(-10, 11)
            low, high = partition_around_pivot(a, pivot)
            self.assertEqual(low, sum(x < pivot for x in original))
            self.assertEqual(high-low, original.count(pivot))
            self.assertTrue(all(x < pivot for x in a[:low]))
            self.assertTrue(all(x == pivot for x in a[low:high]))
            self.assertTrue(all(x > pivot for x in a[high:]))
            self.assertEqual(sorted(a), sorted(original))
