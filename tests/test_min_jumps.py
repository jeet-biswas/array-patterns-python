import random
import unittest

from arrays.min_jumps import min_jumps


class TestMinJumps(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4]), 2)
        self.assertEqual(min_jumps([3, 2, 1, 0, 4]), -1)

    def test_edges(self):
        self.assertEqual(min_jumps([]), 0)
        self.assertEqual(min_jumps([0]), 0)
        self.assertEqual(min_jumps([0, 1]), -1)
        self.assertEqual(min_jumps([100, 0, 0]), 1)
        with self.assertRaises(ValueError):
            min_jumps([1, -1])

    def test_against_dynamic_programming(self):
        rng = random.Random(33)
        for _ in range(150):
            values = [rng.randrange(5) for _ in range(rng.randrange(1, 18))]
            distance = [float('inf')] * len(values)
            distance[0] = 0
            for i in range(len(values)):
                for j in range(i+1, min(len(values), i+values[i]+1)):
                    distance[j] = min(distance[j], distance[i]+1)
            expected = -1 if distance[-1] == float('inf') else distance[-1]
            self.assertEqual(min_jumps(values), expected)
