import random
import unittest

from arrays.signed_radix_sort import signed_radix_sort


class TestSignedRadixSort(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(signed_radix_sort([170, -45, 75, -90, 802, 24, 2, 66]), [-90, -45, 2, 24, 66, 75, 170, 802])

    def test_edges(self):
        self.assertEqual(signed_radix_sort([]), [])
        self.assertEqual(signed_radix_sort([5, 5]), [5, 5])
        self.assertEqual(signed_radix_sort([10**60, -10**60, 0]), [-10**60, 0, 10**60])

    def test_against_reference(self):
        rng = random.Random(289)
        for _ in range(150):
            a = [rng.randrange(-10**9, 10**9) for _ in range(rng.randrange(100))]
            self.assertEqual(signed_radix_sort(a), sorted(a))
