import random
import unittest

from arrays.count_equal_xor_triplets import count_equal_xor_triplets


class TestCountEqualXorTriplets(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_equal_xor_triplets([2, 3, 1, 6, 7]), 4)
        self.assertEqual(count_equal_xor_triplets([1, 1, 1, 1, 1]), 10)

    def test_edges(self):
        self.assertEqual(count_equal_xor_triplets([]), 0)
        self.assertEqual(count_equal_xor_triplets([0]), 0)
        self.assertEqual(count_equal_xor_triplets([0, 0, 0]), 4)
        self.assertEqual(count_equal_xor_triplets([-1, -1]), 1)

    def test_against_reference(self):
        from functools import reduce
        from operator import xor
        rng = random.Random(111)
        for _ in range(100):
            values = [rng.randrange(-4, 8) for _ in range(rng.randrange(12))]
            expected = sum(reduce(xor, values[i:j], 0) == reduce(xor, values[j:k+1], 0)
                           for i in range(len(values)) for j in range(i+1, len(values)) for k in range(j, len(values)))
            self.assertEqual(count_equal_xor_triplets(values), expected)
