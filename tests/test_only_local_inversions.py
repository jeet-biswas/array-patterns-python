import random
import unittest

from arrays.only_local_inversions import only_local_inversions


class TestOnlyLocalInversions(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(only_local_inversions([1, 0, 2]))
        self.assertFalse(only_local_inversions([1, 2, 0]))

    def test_edges(self):
        self.assertTrue(only_local_inversions([]))
        self.assertTrue(only_local_inversions([2, 2, 2]))

    def test_against_reference(self):
        rng = random.Random(168)
        for _ in range(170):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(13))]
            expected = all(a[i] <= a[j] for i in range(len(a)) for j in range(i+2, len(a)))
            self.assertEqual(only_local_inversions(a), expected)
