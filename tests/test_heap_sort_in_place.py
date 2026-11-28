import random
import unittest

from arrays.heap_sort_in_place import heap_sort_in_place


class TestHeapSortInPlace(unittest.TestCase):
    def test_examples(self):
        a = [4, 1, 3, 2]
        self.assertIsNone(heap_sort_in_place(a))
        self.assertEqual(a, [1, 2, 3, 4])

    def test_edges(self):
        for a in ([], [1], [2, 2], [-1, -3]):
            expected = sorted(a)
            heap_sort_in_place(a)
            self.assertEqual(a, expected)

    def test_against_reference(self):
        rng = random.Random(287)
        for _ in range(170):
            a = [rng.randrange(-50, 51) for _ in range(rng.randrange(100))]
            expected = sorted(a)
            heap_sort_in_place(a)
            self.assertEqual(a, expected)
