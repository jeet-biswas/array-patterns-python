import random
import unittest

from arrays.minimum_absolute_pairing_cost import minimum_absolute_pairing_cost


class TestMinimumAbsolutePairingCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_absolute_pairing_cost([3, 1, 2], [2, 3, 1]), 0)
        self.assertEqual(minimum_absolute_pairing_cost([1, 4], [2, 8]), 5)

    def test_edges(self):
        self.assertEqual(minimum_absolute_pairing_cost([], []), 0)
        self.assertEqual(minimum_absolute_pairing_cost([-3, -3], [-1, 2]), 7)
        with self.assertRaises(ValueError): minimum_absolute_pairing_cost([1], [])

    def test_against_reference(self):
        from itertools import permutations
        rng = random.Random(266)
        for _ in range(100):
            n = rng.randrange(8)
            a = [rng.randrange(-6, 7) for _ in range(n)]
            b = [rng.randrange(-6, 7) for _ in range(n)]
            expected = min(sum(abs(x-y) for x, y in zip(a, order)) for order in permutations(b))
            before_a, before_b = a.copy(), b.copy()
            self.assertEqual(minimum_absolute_pairing_cost(a, b), expected)
            self.assertEqual(a, before_a)
            self.assertEqual(b, before_b)
