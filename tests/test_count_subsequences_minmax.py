import random
import unittest

from arrays.count_subsequences_minmax import count_subsequences_minmax


class TestCountSubsequencesMinmax(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_subsequences_minmax([3, 5, 6, 7], 9), 4)
        self.assertEqual(count_subsequences_minmax([3, 3, 6, 8], 10), 6)

    def test_edges(self):
        self.assertEqual(count_subsequences_minmax([], 0), 0)
        self.assertEqual(count_subsequences_minmax([2], 3), 0)
        self.assertEqual(count_subsequences_minmax([0, 0, 0], 0), 7)
        self.assertEqual(count_subsequences_minmax([-3], -6), 1)

    def test_against_reference(self):
        rng = random.Random(134)
        for _ in range(100):
            values = [rng.randrange(-5, 8) for _ in range(rng.randrange(11))]
            target = rng.randrange(-10, 16)
            expected = 0
            for mask in range(1, 1 << len(values)):
                sequence = [x for i, x in enumerate(values) if mask & (1 << i)]
                expected += min(sequence)+max(sequence) <= target
            self.assertEqual(count_subsequences_minmax(values, target), expected)
