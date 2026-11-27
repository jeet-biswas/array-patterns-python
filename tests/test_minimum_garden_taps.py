import random
import unittest

from arrays.minimum_garden_taps import minimum_garden_taps


class TestMinimumGardenTaps(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_garden_taps([3, 4, 1, 1, 0, 0]), 1)

    def test_edges(self):
        self.assertEqual(minimum_garden_taps([0]), 0)
        self.assertIsNone(minimum_garden_taps([0, 0, 0]))
        with self.assertRaises(ValueError): minimum_garden_taps([])
        with self.assertRaises(ValueError): minimum_garden_taps([-1])

    def test_against_reference(self):
        rng = random.Random(269)
        for _ in range(130):
            a = [rng.randrange(5) for _ in range(rng.randrange(1, 9))]
            n = len(a)-1
            best = None
            for mask in range(1 << len(a)):
                intervals = sorted((max(0, i-x), min(n, i+x)) for i, x in enumerate(a) if mask >> i & 1)
                end = 0
                for left, right in intervals:
                    if left > end: break
                    end = max(end, right)
                if end == n: best = mask.bit_count() if best is None else min(best, mask.bit_count())
            self.assertEqual(minimum_garden_taps(a), best)
