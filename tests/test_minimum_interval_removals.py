import random
import unittest

from arrays.minimum_interval_removals import minimum_interval_removals


class TestMinimumIntervalRemovals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_interval_removals([(1, 2), (2, 3), (3, 4), (1, 3)]), 1)

    def test_edges(self):
        self.assertEqual(minimum_interval_removals([]), 0)
        self.assertEqual(minimum_interval_removals([(1, 2), (1, 2)]), 1)
        with self.assertRaises(ValueError): minimum_interval_removals([(1, 1)])

    def test_against_reference(self):
        rng = random.Random(173)
        for _ in range(120):
            a = [(start, start+rng.randrange(1, 5)) for start in [rng.randrange(-3, 5) for _ in range(rng.randrange(9))]]
            kept = 0
            for mask in range(1 << len(a)):
                chosen = [interval for i, interval in enumerate(a) if mask >> i & 1]
                if all(b <= c or d <= a0 for i, (a0, b) in enumerate(chosen) for c, d in chosen[i+1:]):
                    kept = max(kept, len(chosen))
            self.assertEqual(minimum_interval_removals(a), len(a)-kept)
