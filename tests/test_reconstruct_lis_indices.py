import random
import unittest

from arrays.reconstruct_lis_indices import reconstruct_lis_indices


class TestReconstructLisIndices(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(reconstruct_lis_indices([3, 1, 2, 5, 4]), [1, 2, 4])

    def test_edges(self):
        self.assertEqual(reconstruct_lis_indices([]), [])
        self.assertEqual(reconstruct_lis_indices([2, 2, 2]), [2])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(258)
        for _ in range(130):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(11))]
            best = max(k for k in range(len(a)+1) if any(all(x < y for x, y in zip(s, s[1:])) for s in combinations(a, k)))
            indices = reconstruct_lis_indices(a)
            self.assertEqual(len(indices), best)
            self.assertTrue(all(0 <= i < len(a) for i in indices))
            self.assertTrue(all(i < j and a[i] < a[j] for i, j in zip(indices, indices[1:])))
