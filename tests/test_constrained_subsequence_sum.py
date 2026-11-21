import random
import unittest

from arrays.constrained_subsequence_sum import constrained_subsequence_sum


class TestConstrainedSubsequenceSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(constrained_subsequence_sum([10, 2, -10, 5, 20], 2), 37)

    def test_edges(self):
        self.assertEqual(constrained_subsequence_sum([-5, -2, -3], 1), -2)
        with self.assertRaises(ValueError): constrained_subsequence_sum([], 1)
        with self.assertRaises(ValueError): constrained_subsequence_sum([1], 0)

    def test_against_reference(self):
        rng = random.Random(150)
        for _ in range(100):
            a = [rng.randrange(-7, 8) for _ in range(rng.randrange(1, 10))]
            k = rng.randrange(1, 5)
            best = min(a)
            for mask in range(1, 1 << len(a)):
                indices = [i for i in range(len(a)) if mask >> i & 1]
                if all(y-x <= k for x, y in zip(indices, indices[1:])):
                    best = max(best, sum(a[i] for i in indices))
            self.assertEqual(constrained_subsequence_sum(a, k), best)
