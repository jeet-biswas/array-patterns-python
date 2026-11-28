import random
import unittest

from arrays.range_bitwise_and_queries import range_bitwise_and_queries


class TestRangeBitwiseAndQueries(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(range_bitwise_and_queries([7, 3, 5, 1], [(0, 3), (1, 2), (0, 4)]), [1, 3, 1])

    def test_edges(self):
        self.assertEqual(range_bitwise_and_queries([], []), [])
        with self.assertRaises(IndexError): range_bitwise_and_queries([1], [(0, 0)])
        with self.assertRaises(ValueError): range_bitwise_and_queries([-1], [])

    def test_against_reference(self):
        from functools import reduce
        from operator import and_
        rng = random.Random(317)
        for _ in range(140):
            a = [rng.randrange(256) for _ in range(rng.randrange(1, 80))]
            queries = []
            for _ in range(25):
                left = rng.randrange(len(a))
                queries.append((left, rng.randrange(left+1, len(a)+1)))
            self.assertEqual(range_bitwise_and_queries(a, queries), [reduce(and_, a[l:r]) for l, r in queries])
