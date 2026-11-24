import random
import unittest

from arrays.count_global_max_occurrences import count_global_max_occurrences


class TestCountGlobalMaxOccurrences(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_global_max_occurrences([1, 3, 2, 3, 3], 2), 6)

    def test_edges(self):
        self.assertEqual(count_global_max_occurrences([], 1), 0)
        self.assertEqual(count_global_max_occurrences([1, 1], 3), 0)
        with self.assertRaises(ValueError): count_global_max_occurrences([], 0)

    def test_against_reference(self):
        rng = random.Random(186)
        for _ in range(150):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(12))]
            k = rng.randrange(1, 5)
            expected = sum(a[i:j].count(max(a)) >= k for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_global_max_occurrences(a, k), expected)
