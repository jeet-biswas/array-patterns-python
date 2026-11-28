import random
import unittest

from arrays.count_smaller_values import count_smaller_values


class TestCountSmallerValues(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_smaller_values([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])

    def test_edges(self):
        self.assertEqual(count_smaller_values([]), [])
        self.assertEqual(count_smaller_values([4, 4, 4]), [0, 0, 0])

    def test_against_reference(self):
        rng = random.Random(323)
        for _ in range(180):
            a = [rng.randrange(-15, 16) for _ in range(rng.randrange(100))]
            self.assertEqual(count_smaller_values(a), [sum(y < x for y in a) for x in a])
