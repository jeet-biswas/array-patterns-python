import random
import unittest

from arrays.missing_numbers_one_to_n import missing_numbers_one_to_n


class TestMissingNumbersOneToN(unittest.TestCase):
    def test_examples(self):
        a = [4, 3, 2, 7, 8, 2, 3, 1]
        self.assertEqual(missing_numbers_one_to_n(a), [5, 6])
        self.assertEqual(a, [4, 3, 2, 7, 8, 2, 3, 1])

    def test_edges(self):
        self.assertEqual(missing_numbers_one_to_n([]), [])
        a = [1, -2]
        with self.assertRaises(ValueError): missing_numbers_one_to_n(a)
        self.assertEqual(a, [1, -2])

    def test_against_reference(self):
        rng = random.Random(300)
        for _ in range(170):
            n = rng.randrange(1, 80)
            a = [rng.randrange(1, n+1) for _ in range(n)]
            before = a.copy()
            self.assertEqual(missing_numbers_one_to_n(a), sorted(set(range(1, n+1))-set(a)))
            self.assertEqual(a, before)
