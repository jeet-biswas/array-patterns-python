import random
import unittest

from arrays.max_score_containing_index import max_score_containing_index


class TestMaxScoreContainingIndex(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_score_containing_index([1, 4, 3, 7, 4, 5], 3), 15)

    def test_edges(self):
        self.assertEqual(max_score_containing_index([0], 0), 0)
        with self.assertRaises(IndexError): max_score_containing_index([], 0)
        with self.assertRaises(ValueError): max_score_containing_index([-1], 0)

    def test_against_reference(self):
        rng = random.Random(153)
        for _ in range(150):
            a = [rng.randrange(9) for _ in range(rng.randrange(1, 12))]
            k = rng.randrange(len(a))
            expected = max(min(a[i:j])*(j-i) for i in range(k+1) for j in range(k+1, len(a)+1))
            self.assertEqual(max_score_containing_index(a, k), expected)
