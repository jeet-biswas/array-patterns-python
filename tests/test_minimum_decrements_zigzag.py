import random
import unittest

from arrays.minimum_decrements_zigzag import minimum_decrements_zigzag


class TestMinimumDecrementsZigzag(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_decrements_zigzag([9, 6, 1, 6, 2]), 4)

    def test_edges(self):
        self.assertEqual(minimum_decrements_zigzag([]), 0)
        self.assertEqual(minimum_decrements_zigzag([5]), 0)
        self.assertEqual(minimum_decrements_zigzag([2, 2]), 1)

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(214)
        for _ in range(70):
            a = [rng.randrange(4) for _ in range(rng.randrange(1, 6))]
            best = None
            for candidate in product(*(range(-1, x+1) for x in a)):
                valid = any(all((candidate[i] < candidate[i+1]) if i % 2 == parity else (candidate[i] > candidate[i+1]) for i in range(len(a)-1)) for parity in (0, 1))
                if valid:
                    cost = sum(a)-sum(candidate)
                    best = cost if best is None else min(best, cost)
            self.assertEqual(minimum_decrements_zigzag(a), best)
