import random
import unittest

from arrays.min_length_sum import min_length_sum


class TestMinLengthSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_length_sum([2, 3, 1, 2, 4, 3], 7), 2)
        self.assertEqual(min_length_sum([0, 0, 5, 0], 5), 1)

    def test_edges(self):
        self.assertEqual(min_length_sum([], 1), 0)
        self.assertEqual(min_length_sum([1, 1], 3), 0)
        for values, target in [([1], 0), ([1], -1), ([-1, 2], 2)]:
            with self.assertRaises(ValueError):
                min_length_sum(values, target)

    def test_against_brute_force(self):
        rng = random.Random(24)
        for _ in range(100):
            values = [rng.randrange(6) for _ in range(rng.randrange(15))]
            target = rng.randrange(1, 25)
            lengths = [j-i for i in range(len(values)) for j in range(i+1, len(values)+1)
                       if sum(values[i:j]) >= target]
            self.assertEqual(min_length_sum(values, target), min(lengths, default=0))
