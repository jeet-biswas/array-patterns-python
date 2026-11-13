import random
import unittest

from arrays.smallest_missing_positive import smallest_missing_positive


class TestSmallestMissingPositive(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_missing_positive([3, 4, -1, 1]), 2)
        self.assertEqual(smallest_missing_positive([1, 2, 0]), 3)

    def test_edges(self):
        self.assertEqual(smallest_missing_positive([]), 1)
        self.assertEqual(smallest_missing_positive([1, 1]), 2)
        self.assertEqual(smallest_missing_positive([-5, 0, 100]), 1)

    def test_against_set(self):
        rng = random.Random(30)
        for _ in range(150):
            values = [rng.randrange(-5, 20) for _ in range(rng.randrange(20))]
            original = values.copy()
            present = set(values)
            expected = next(x for x in range(1, len(values)+2) if x not in present)
            self.assertEqual(smallest_missing_positive(values), expected)
            self.assertEqual(sorted(values), sorted(original))
