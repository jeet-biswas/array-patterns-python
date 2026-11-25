import random
import unittest

from arrays.minimum_array_deviation import minimum_array_deviation


class TestMinimumArrayDeviation(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_array_deviation([1, 2, 3, 4]), 1)
        self.assertEqual(minimum_array_deviation([4, 1, 5, 20, 3]), 3)

    def test_edges(self):
        self.assertEqual(minimum_array_deviation([]), 0)
        self.assertEqual(minimum_array_deviation([7]), 0)
        with self.assertRaises(ValueError): minimum_array_deviation([0])

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(228)
        for _ in range(120):
            a = [rng.randrange(1, 25) for _ in range(rng.randrange(1, 7))]
            options = []
            for value in a:
                reachable = {value}
                pending = [value]
                while pending:
                    x = pending.pop()
                    after = x*2 if x % 2 else x//2
                    if after not in reachable:
                        reachable.add(after)
                        pending.append(after)
                options.append(reachable)
            expected = min(max(s)-min(s) for s in product(*options))
            self.assertEqual(minimum_array_deviation(a), expected)
