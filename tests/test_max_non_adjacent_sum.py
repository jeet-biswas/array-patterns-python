import random
import unittest

from arrays.max_non_adjacent_sum import max_non_adjacent_sum


class TestMaxNonAdjacentSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_non_adjacent_sum([2, 7, 9, 3, 1]), 12)
        self.assertEqual(max_non_adjacent_sum([5, 1, 1, 5]), 10)

    def test_edges(self):
        self.assertEqual(max_non_adjacent_sum([]), 0)
        self.assertEqual(max_non_adjacent_sum([-3, -1, -7]), 0)
        self.assertEqual(max_non_adjacent_sum([8]), 8)

    def test_against_reference(self):
        rng = random.Random(39)
        for _ in range(100):
            values = [rng.randrange(-5, 10) for _ in range(rng.randrange(11))]
            expected = max(sum(x for i, x in enumerate(values) if mask & (1 << i))
                           for mask in range(1 << len(values)) if not mask & (mask << 1))
            self.assertEqual(max_non_adjacent_sum(values), expected)
