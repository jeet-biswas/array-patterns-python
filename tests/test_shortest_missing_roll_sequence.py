import random
import unittest

from arrays.shortest_missing_roll_sequence import shortest_missing_roll_sequence


class TestShortestMissingRollSequence(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(shortest_missing_roll_sequence([1, 1, 2, 2], 2), 2)

    def test_edges(self):
        self.assertEqual(shortest_missing_roll_sequence([], 3), 1)
        self.assertEqual(shortest_missing_roll_sequence([1, 1, 1], 1), 4)
        with self.assertRaises(ValueError): shortest_missing_roll_sequence([0], 2)
        with self.assertRaises(ValueError): shortest_missing_roll_sequence([], 0)

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(250)
        for _ in range(140):
            k = rng.randrange(1, 4)
            a = [rng.randrange(1, k+1) for _ in range(rng.randrange(10))]
            def present(candidate):
                at = 0
                for x in a:
                    if at < len(candidate) and candidate[at] == x: at += 1
                return at == len(candidate)
            expected = next(size for size in range(1, len(a)+2) if any(not present(s) for s in product(range(1, k+1), repeat=size)))
            self.assertEqual(shortest_missing_roll_sequence(a, k), expected)
