import random
import unittest

from arrays.smallest_k_values import smallest_k_values


class TestSmallestKValues(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_k_values([7, 2, 5, 2, 1], 3), [1, 2, 2])

    def test_edges(self):
        self.assertEqual(smallest_k_values([], 0), [])
        with self.assertRaises(ValueError): smallest_k_values([1], 2)
        with self.assertRaises(ValueError): smallest_k_values([1], -1)

    def test_against_reference(self):
        rng = random.Random(298)
        for _ in range(170):
            a = [rng.randrange(-20, 21) for _ in range(rng.randrange(100))]
            k = rng.randrange(len(a)+1)
            self.assertEqual(smallest_k_values(a, k), sorted(a)[:k])
