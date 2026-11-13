import random
import unittest

from arrays.kth_largest import kth_largest


class TestKthLargest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(kth_largest([5, 5, 4], 2), 5)

    def test_edges(self):
        self.assertEqual(kth_largest([-3, -1, -2], 3), -3)
        self.assertEqual(kth_largest([7], 1), 7)
        for values, k in [([], 1), ([1], 0), ([1], 2), ([1], -1)]:
            with self.assertRaises(ValueError):
                kth_largest(values, k)

    def test_against_sort(self):
        rng = random.Random(28)
        for _ in range(100):
            values = [rng.randrange(-9, 10) for _ in range(rng.randrange(1, 25))]
            original = values.copy()
            k = rng.randrange(1, len(values)+1)
            self.assertEqual(kth_largest(values, k), sorted(values, reverse=True)[k-1])
            self.assertEqual(values, original)
