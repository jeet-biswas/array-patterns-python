import random
import unittest

from arrays.second_largest import second_largest


class TestSecondLargest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(second_largest([5, 1, 5, 4]), 4)
        self.assertEqual(second_largest([-8, -2, -5]), -5)

    def test_edges(self):
        for values in ([], [3], [3, 3]):
            self.assertIsNone(second_largest(values))
        self.assertEqual(second_largest([0, -1]), -1)

    def test_against_sort(self):
        rng = random.Random(10)
        for _ in range(100):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(20))]
            distinct = sorted(set(values))
            expected = distinct[-2] if len(distinct) > 1 else None
            self.assertEqual(second_largest(values), expected)
