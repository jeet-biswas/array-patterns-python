import random
import unittest

from arrays.longest_equal_after_deletions import longest_equal_after_deletions


class TestLongestEqualAfterDeletions(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_equal_after_deletions([1, 3, 2, 3, 1, 3], 3), 3)

    def test_edges(self):
        self.assertEqual(longest_equal_after_deletions([], 0), 0)
        self.assertEqual(longest_equal_after_deletions([1, 1, 2, 1], 0), 2)
        with self.assertRaises(ValueError): longest_equal_after_deletions([], -1)

    def test_against_reference(self):
        rng = random.Random(187)
        for _ in range(120):
            a = [rng.randrange(4) for _ in range(rng.randrange(10))]
            k = rng.randrange(5)
            best = 0
            for mask in range(1 << len(a)):
                if mask.bit_count() > k: continue
                remaining = [x for i, x in enumerate(a) if not mask >> i & 1]
                run = 0
                for i, x in enumerate(remaining):
                    run = run+1 if i and remaining[i-1] == x else 1
                    best = max(best, run)
            self.assertEqual(longest_equal_after_deletions(a, k), best)
