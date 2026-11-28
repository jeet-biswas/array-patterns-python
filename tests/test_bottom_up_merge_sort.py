import random
import unittest

from arrays.bottom_up_merge_sort import bottom_up_merge_sort


class TestBottomUpMergeSort(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(bottom_up_merge_sort([5, 1, 4, 2, 3]), [1, 2, 3, 4, 5])

    def test_edges(self):
        for a in ([], [2], [-2, -2, -3]):
            result = bottom_up_merge_sort(a)
            self.assertEqual(result, sorted(a))
            self.assertIsNot(result, a)

    def test_against_reference(self):
        rng = random.Random(288)
        for _ in range(150):
            a = [rng.randrange(-100, 101) for _ in range(rng.randrange(100))]
            before = a.copy()
            self.assertEqual(bottom_up_merge_sort(a), sorted(a))
            self.assertEqual(a, before)
