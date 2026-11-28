import random
import unittest

from arrays.minimum_multiset_cover_window import minimum_multiset_cover_window


class TestMinimumMultisetCoverWindow(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_multiset_cover_window([1, 2, 1, 3, 2, 1], [1, 1, 2]), (0, 3))

    def test_edges(self):
        self.assertEqual(minimum_multiset_cover_window([], []), (0, 0))
        self.assertIsNone(minimum_multiset_cover_window([1, 2], [1, 1]))

    def test_against_reference(self):
        from collections import Counter
        rng = random.Random(305)
        for _ in range(150):
            a = [rng.randrange(5) for _ in range(rng.randrange(14))]
            required = [rng.randrange(5) for _ in range(rng.randrange(6))]
            need = Counter(required)
            candidates = [(j-i, i, j) for i in range(len(a)+1) for j in range(i, len(a)+1) if not need-Counter(a[i:j])]
            expected = min(candidates)[1:] if candidates else None
            self.assertEqual(minimum_multiset_cover_window(a, required), expected)
