import random
import unittest

from arrays.minimum_deletions_unequal_pairs import minimum_deletions_unequal_pairs


class TestMinimumDeletionsUnequalPairs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_deletions_unequal_pairs([1, 1, 2, 3, 5]), 1)
        self.assertEqual(minimum_deletions_unequal_pairs([1, 1, 2, 2, 3, 3]), 2)

    def test_edges(self):
        self.assertEqual(minimum_deletions_unequal_pairs([]), 0)
        self.assertEqual(minimum_deletions_unequal_pairs([7, 7, 7]), 3)

    def test_against_reference(self):
        rng = random.Random(274)
        for _ in range(140):
            a = [rng.randrange(-2, 3) for _ in range(rng.randrange(12))]
            kept = 0
            for mask in range(1 << len(a)):
                s = [x for i, x in enumerate(a) if mask >> i & 1]
                if len(s) % 2 == 0 and all(s[i] != s[i+1] for i in range(0, len(s), 2)):
                    kept = max(kept, len(s))
            self.assertEqual(minimum_deletions_unequal_pairs(a), len(a)-kept)
