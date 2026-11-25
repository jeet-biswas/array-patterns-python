import random
import unittest

from arrays.max_equal_after_adjustments import max_equal_after_adjustments


class TestMaxEqualAfterAdjustments(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_equal_after_adjustments([4, 6, 1, 2], 2), 3)

    def test_edges(self):
        self.assertEqual(max_equal_after_adjustments([], 0), 0)
        self.assertEqual(max_equal_after_adjustments([2, 2, 1], 0), 2)
        with self.assertRaises(ValueError): max_equal_after_adjustments([], -1)

    def test_against_reference(self):
        rng = random.Random(209)
        for _ in range(150):
            a = [rng.randrange(-10, 11) for _ in range(rng.randrange(15))]
            k = rng.randrange(6)
            expected = max((sum(abs(x-t) <= k for x in a) for t in range(-15, 16)), default=0)
            self.assertEqual(max_equal_after_adjustments(a, k), expected)
