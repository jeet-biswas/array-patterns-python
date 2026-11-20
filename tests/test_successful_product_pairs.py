import random
import unittest

from arrays.successful_product_pairs import successful_product_pairs


class TestSuccessfulProductPairs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(successful_product_pairs([5, 1, 3], [1, 2, 3, 4, 5], 7), [4, 0, 3])
        self.assertEqual(successful_product_pairs([3, 1, 2], [8, 5, 8], 16), [2, 0, 2])

    def test_edges(self):
        self.assertEqual(successful_product_pairs([], [1], 2), [])
        self.assertEqual(successful_product_pairs([0, 3], [], 0), [0, 0])
        self.assertEqual(successful_product_pairs([0, 1], [0, 2], 0), [2, 2])
        self.assertEqual(successful_product_pairs([0], [5], 1), [0])
        with self.assertRaises(ValueError):
            successful_product_pairs([1], [-1], 1)

    def test_against_reference(self):
        rng = random.Random(139)
        for _ in range(150):
            first = [rng.randrange(15) for _ in range(rng.randrange(20))]
            second = [rng.randrange(15) for _ in range(rng.randrange(20))]
            threshold = rng.randrange(150)
            original = first.copy(), second.copy()
            self.assertEqual(successful_product_pairs(first, second, threshold), [sum(a*b >= threshold for b in second) for a in first])
            self.assertEqual((first, second), original)
