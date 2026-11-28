import random
import unittest

from arrays.stable_counting_sort_records import stable_counting_sort_records


class TestStableCountingSortRecords(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(stable_counting_sort_records([(2, 7), (1, 8), (2, 9)], 3), [(1, 8), (2, 7), (2, 9)])

    def test_edges(self):
        self.assertEqual(stable_counting_sort_records([], 0), [])
        with self.assertRaises(ValueError): stable_counting_sort_records([(2, 1)], 2)
        with self.assertRaises(ValueError): stable_counting_sort_records([], -1)

    def test_against_reference(self):
        rng = random.Random(290)
        for _ in range(150):
            k = rng.randrange(1, 25)
            a = [(rng.randrange(k), i) for i in range(rng.randrange(100))]
            self.assertEqual(stable_counting_sort_records(a, k), sorted(a, key=lambda pair: pair[0]))
