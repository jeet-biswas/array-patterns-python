import random
import unittest

from arrays.top_k_frequent_values import top_k_frequent_values


class TestTopKFrequentValues(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(top_k_frequent_values([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(top_k_frequent_values([3, 2, 1], 2), [1, 2])

    def test_edges(self):
        self.assertEqual(top_k_frequent_values([], 0), [])
        with self.assertRaises(ValueError): top_k_frequent_values([1, 1], 2)

    def test_against_reference(self):
        rng = random.Random(299)
        for _ in range(170):
            a = [rng.randrange(-10, 11) for _ in range(rng.randrange(100))]
            k = rng.randrange(len(set(a))+1)
            expected = sorted(set(a), key=lambda x: (-a.count(x), x))[:k]
            self.assertEqual(top_k_frequent_values(a, k), expected)
