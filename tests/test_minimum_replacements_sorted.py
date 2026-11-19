import random
import unittest

from arrays.minimum_replacements_sorted import minimum_replacements_sorted


class TestMinimumReplacementsSorted(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_replacements_sorted([3, 9, 3]), 2)
        self.assertEqual(minimum_replacements_sorted([12, 9, 7, 6, 17, 19, 21]), 6)

    def test_edges(self):
        self.assertEqual(minimum_replacements_sorted([]), 0)
        self.assertEqual(minimum_replacements_sorted([1, 2, 3]), 0)
        self.assertEqual(minimum_replacements_sorted([5, 1]), 4)
        for values in ([0], [-1, 2]):
            with self.assertRaises(ValueError):
                minimum_replacements_sorted(values)

    def test_against_reference(self):
        from functools import lru_cache
        @lru_cache(None)
        def partitions(total, minimum=1):
            if total == 0:
                return ((),)
            return tuple((first,)+tail for first in range(minimum, total+1)
                         for tail in partitions(total-first, first))
        rng = random.Random(121)
        for _ in range(100):
            values = [rng.randrange(1, 8) for _ in range(rng.randrange(6))]
            states = {0: 0}
            for value in values:
                updated = {}
                for previous, cost in states.items():
                    for pieces in partitions(value):
                        if pieces[0] >= previous:
                            candidate = cost + len(pieces)-1
                            updated[pieces[-1]] = min(updated.get(pieces[-1], candidate), candidate)
                states = updated
            original = values.copy()
            self.assertEqual(minimum_replacements_sorted(values), min(states.values()))
            self.assertEqual(values, original)
