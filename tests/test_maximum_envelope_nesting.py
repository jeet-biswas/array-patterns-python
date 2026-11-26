import random
import unittest

from arrays.maximum_envelope_nesting import maximum_envelope_nesting


class TestMaximumEnvelopeNesting(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maximum_envelope_nesting([(5, 4), (6, 4), (6, 7), (2, 3)]), 3)

    def test_edges(self):
        self.assertEqual(maximum_envelope_nesting([]), 0)
        self.assertEqual(maximum_envelope_nesting([(2, 1), (2, 2), (2, 3)]), 1)
        with self.assertRaises(ValueError): maximum_envelope_nesting([(0, 1)])

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(257)
        for _ in range(120):
            a = [(rng.randrange(1, 8), rng.randrange(1, 8)) for _ in range(rng.randrange(10))]
            expected = 0
            for k in range(len(a)+1):
                for subset in combinations(a, k):
                    s = sorted(subset)
                    if all(x[0] < y[0] and x[1] < y[1] for x, y in zip(s, s[1:])): expected = max(expected, k)
            self.assertEqual(maximum_envelope_nesting(a), expected)
