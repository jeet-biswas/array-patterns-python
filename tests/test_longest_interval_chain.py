import random
import unittest

from arrays.longest_interval_chain import longest_interval_chain


class TestLongestIntervalChain(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_interval_chain([(1, 2), (2, 3), (3, 4)]), 2)

    def test_edges(self):
        self.assertEqual(longest_interval_chain([]), 0)
        self.assertEqual(longest_interval_chain([(1, 1), (2, 2)]), 2)
        with self.assertRaises(ValueError): longest_interval_chain([(2, 1)])

    def test_against_reference(self):
        rng = random.Random(207)
        for _ in range(120):
            pairs = [tuple(sorted((rng.randrange(-4, 8), rng.randrange(-4, 8)))) for _ in range(rng.randrange(9))]
            best = 0
            for mask in range(1 << len(pairs)):
                chosen = sorted(p for i, p in enumerate(pairs) if mask >> i & 1)
                if all(a[1] < b[0] for a, b in zip(chosen, chosen[1:])): best = max(best, len(chosen))
            self.assertEqual(longest_interval_chain(pairs), best)
