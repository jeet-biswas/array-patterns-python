import random
import unittest

from arrays.longest_turbulent_subarray import longest_turbulent_subarray


class TestLongestTurbulentSubarray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_turbulent_subarray([9, 4, 2, 10, 7, 8, 8, 1, 9]), 5)
        self.assertEqual(longest_turbulent_subarray([4, 8, 12, 16]), 2)

    def test_edges(self):
        self.assertEqual(longest_turbulent_subarray([]), 0)
        self.assertEqual(longest_turbulent_subarray([3]), 1)
        self.assertEqual(longest_turbulent_subarray([2, 2, 2]), 1)
        self.assertEqual(longest_turbulent_subarray([-1, -3, -2]), 3)

    def test_against_reference(self):
        rng = random.Random(127)
        for _ in range(150):
            values = [rng.randrange(-5, 6) for _ in range(rng.randrange(18))]
            expected = 0
            for i in range(len(values)):
                for j in range(i+1, len(values)+1):
                    differences = [values[t+1]-values[t] for t in range(i, j-1)]
                    if all(d != 0 for d in differences) and all(a*b < 0 for a, b in zip(differences, differences[1:])):
                        expected = max(expected, j-i)
            self.assertEqual(longest_turbulent_subarray(values), expected)
