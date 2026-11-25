import random
import unittest

from arrays.has_valid_block_partition import has_valid_block_partition


class TestHasValidBlockPartition(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(has_valid_block_partition([4, 4, 4, 5, 6]))
        self.assertFalse(has_valid_block_partition([1, 1, 1, 2]))

    def test_edges(self):
        self.assertTrue(has_valid_block_partition([]))
        self.assertFalse(has_valid_block_partition([1]))
        self.assertTrue(has_valid_block_partition([-2, -1, 0]))

    def test_against_reference(self):
        from functools import lru_cache
        from itertools import product
        @lru_cache(None)
        def reference(s):
            if not s: return True
            if len(s) >= 2 and s[0] == s[1] and reference(s[2:]): return True
            return len(s) >= 3 and (len(set(s[:3])) == 1 or s[1]-s[0] == s[2]-s[1] == 1) and reference(s[3:])
        for n in range(8):
            for a in product(range(3), repeat=n):
                self.assertEqual(has_valid_block_partition(list(a)), reference(a))
