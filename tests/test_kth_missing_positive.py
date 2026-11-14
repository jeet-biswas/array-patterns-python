import random
import unittest

from arrays.kth_missing_positive import kth_missing_positive


class TestKthMissingPositive(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_missing_positive([2, 3, 4, 7, 11], 5), 9)
        self.assertEqual(kth_missing_positive([1, 2, 3, 4], 2), 6)

    def test_edges(self):
        self.assertEqual(kth_missing_positive([], 4), 4)
        self.assertEqual(kth_missing_positive([5], 1), 1)
        for k in (0, -1):
            with self.assertRaises(ValueError):
                kth_missing_positive([1], k)

    def test_against_reference(self):
        rng = random.Random(53)
        for _ in range(150):
            values = sorted(rng.sample(range(1, 50), rng.randrange(20)))
            k = rng.randrange(1, 30)
            missing = [x for x in range(1, 100) if x not in set(values)]
            self.assertEqual(kth_missing_positive(values, k), missing[k-1])
