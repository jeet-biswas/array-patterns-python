import random
import unittest

from arrays.equal_value_index_distances import equal_value_index_distances


class TestEqualValueIndexDistances(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(equal_value_index_distances([1, 3, 1, 1, 2]), [5, 0, 3, 4, 0])

    def test_edges(self):
        self.assertEqual(equal_value_index_distances([]), [])
        self.assertEqual(equal_value_index_distances([5, 5, 5]), [3, 2, 3])

    def test_against_reference(self):
        rng = random.Random(204)
        for _ in range(160):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(25))]
            expected = [sum(abs(i-j) for j, y in enumerate(a) if x == y) for i, x in enumerate(a)]
            self.assertEqual(equal_value_index_distances(a), expected)
