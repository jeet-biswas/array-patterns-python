import random
import unittest

from arrays.min_replacements_continuous import min_replacements_continuous


class TestMinReplacementsContinuous(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_replacements_continuous([1, 2, 3, 5, 6]), 1)

    def test_edges(self):
        self.assertEqual(min_replacements_continuous([]), 0)
        self.assertEqual(min_replacements_continuous([7, 7, 7]), 2)

    def test_against_reference(self):
        rng = random.Random(165)
        for _ in range(130):
            a = [rng.randrange(-8, 9) for _ in range(rng.randrange(10))]
            if a:
                kept = max(len(set(a) & set(range(start, start+len(a)))) for start in range(min(a)-len(a), max(a)+1))
                expected = len(a)-kept
            else: expected = 0
            self.assertEqual(min_replacements_continuous(a), expected)
