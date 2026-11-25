import random
import unittest

from arrays.minimum_parallel_resources import minimum_parallel_resources


class TestMinimumParallelResources(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_parallel_resources([(0, 30), (5, 10), (15, 20)]), 2)

    def test_edges(self):
        self.assertEqual(minimum_parallel_resources([]), 0)
        self.assertEqual(minimum_parallel_resources([(1, 2), (2, 3)]), 1)
        with self.assertRaises(ValueError): minimum_parallel_resources([(1, 1)])

    def test_against_reference(self):
        rng = random.Random(208)
        for _ in range(150):
            intervals = [(s, s+rng.randrange(1, 7)) for s in [rng.randrange(-7, 8) for _ in range(rng.randrange(15))]]
            expected = max((sum(start <= point < end for start, end in intervals) for point, _ in intervals), default=0)
            self.assertEqual(minimum_parallel_resources(intervals), expected)
