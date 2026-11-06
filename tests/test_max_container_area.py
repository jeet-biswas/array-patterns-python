import random
import unittest

from arrays.max_container_area import max_container_area


class TestMaxContainerArea(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_container_area([3, 0, 0, 3]), 9)

    def test_edges(self):
        for values in ([], [4], [0, 0]):
            self.assertEqual(max_container_area(values), 0)
        self.assertEqual(max_container_area([2, 2]), 2)
        with self.assertRaises(ValueError):
            max_container_area([1, -2])

    def test_against_brute_force(self):
        rng = random.Random(20)
        for _ in range(100):
            values = [rng.randrange(10) for _ in range(rng.randrange(15))]
            expected = max([0] + [(j-i)*min(values[i], values[j])
                                  for i in range(len(values)) for j in range(i+1, len(values))])
            self.assertEqual(max_container_area(values), expected)
