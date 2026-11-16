import random
import unittest

from arrays.find_min_rotated import find_min_rotated


class TestFindMinRotated(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_min_rotated([3, 4, 5, 1, 2]), 1)
        self.assertEqual(find_min_rotated([2, 2, 2, 0, 1]), 0)

    def test_edges(self):
        self.assertEqual(find_min_rotated([7]), 7)
        self.assertEqual(find_min_rotated([1, 1, 1]), 1)
        self.assertEqual(find_min_rotated([1, 2, 3]), 1)
        with self.assertRaises(ValueError):
            find_min_rotated([])

    def test_against_reference(self):
        rng = random.Random(58)
        for _ in range(150):
            ordered = sorted(rng.randrange(-7, 8) for _ in range(rng.randrange(1, 25)))
            for cut in range(len(ordered)):
                values = ordered[cut:] + ordered[:cut]
                self.assertEqual(find_min_rotated(values), min(values))
