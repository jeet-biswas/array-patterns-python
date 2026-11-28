import random
import unittest

from arrays.wiggle_sort_non_strict import wiggle_sort_non_strict


class TestWiggleSortNonStrict(unittest.TestCase):
    def test_examples(self):
        a = [3, 5, 2, 1, 6, 4]
        self.assertIsNone(wiggle_sort_non_strict(a))
        self.assertEqual(a, [3, 5, 1, 6, 2, 4])

    def test_edges(self):
        for a in ([], [1], [2, 2, 2]):
            before = a.copy()
            wiggle_sort_non_strict(a)
            self.assertEqual(a, before)

    def test_against_reference(self):
        rng = random.Random(297)
        for _ in range(180):
            a = [rng.randrange(-20, 21) for _ in range(rng.randrange(100))]
            original = sorted(a)
            wiggle_sort_non_strict(a)
            self.assertEqual(sorted(a), original)
            self.assertTrue(all(a[i-1] <= a[i] if i % 2 else a[i-1] >= a[i] for i in range(1, len(a))))
