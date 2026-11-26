import random
import unittest

from arrays.count_distinct_value_subsequences import count_distinct_value_subsequences


class TestCountDistinctValueSubsequences(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_distinct_value_subsequences([1, 2, 1]), 6)

    def test_edges(self):
        self.assertEqual(count_distinct_value_subsequences([]), 0)
        self.assertEqual(count_distinct_value_subsequences([5, 5, 5]), 3)

    def test_against_reference(self):
        rng = random.Random(263)
        for _ in range(150):
            a = [rng.randrange(-3, 4) for _ in range(rng.randrange(12))]
            sequences = {tuple(x for i, x in enumerate(a) if mask >> i & 1) for mask in range(1, 1 << len(a))}
            self.assertEqual(count_distinct_value_subsequences(a), len(sequences))
