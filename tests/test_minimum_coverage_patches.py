import random
import unittest

from arrays.minimum_coverage_patches import minimum_coverage_patches


class TestMinimumCoveragePatches(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_coverage_patches([1, 3], 6), 1)
        self.assertEqual(minimum_coverage_patches([1, 5, 10], 20), 2)

    def test_edges(self):
        self.assertEqual(minimum_coverage_patches([], 0), 0)
        self.assertEqual(minimum_coverage_patches([], 7), 3)
        with self.assertRaises(ValueError): minimum_coverage_patches([0], 3)
        with self.assertRaises(ValueError): minimum_coverage_patches([2, 1], 3)
        with self.assertRaises(ValueError): minimum_coverage_patches([], -1)

    def test_against_reference(self):
        from itertools import combinations_with_replacement
        def covers(values, target):
            reachable = {0}
            for value in values:
                reachable |= {s+value for s in reachable if s+value <= target}
            return all(x in reachable for x in range(1, target+1))
        rng = random.Random(181)
        for _ in range(90):
            a = sorted(rng.randrange(1, 9) for _ in range(rng.randrange(6)))
            target = rng.randrange(11)
            expected = next(k for k in range(target.bit_length()+1) if any(covers(a+list(extra), target) for extra in combinations_with_replacement(range(1, target+1), k)))
            self.assertEqual(minimum_coverage_patches(a, target), expected)
