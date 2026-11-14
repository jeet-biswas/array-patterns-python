import random
import unittest

from arrays.range_additions import range_additions


class TestRangeAdditions(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(range_additions(5, [(1, 4, 2), (2, 5, 3), (0, 3, -2)]), [-2, 0, 3, 5, 3])
        self.assertEqual(range_additions(3, [(0, 3, 4), (1, 1, 9)]), [4, 4, 4])

    def test_edges(self):
        self.assertEqual(range_additions(0, [(0, 0, 5)]), [])
        self.assertEqual(range_additions(2, []), [0, 0])
        for length, updates in [(-1, []), (3, [(-1, 2, 1)]), (3, [(2, 1, 1)]),
                                (3, [(0, 4, 1)]), (3, [(0, 1)])]:
            with self.assertRaises(ValueError):
                range_additions(length, updates)

    def test_against_reference(self):
        rng = random.Random(55)
        for _ in range(150):
            length = rng.randrange(20)
            updates = []
            expected = [0] * length
            for _ in range(rng.randrange(20)):
                start, stop = sorted((rng.randrange(length+1), rng.randrange(length+1)))
                delta = rng.randrange(-8, 9)
                updates.append((start, stop, delta))
                for i in range(start, stop):
                    expected[i] += delta
            original = updates.copy()
            self.assertEqual(range_additions(length, updates), expected)
            self.assertEqual(updates, original)
