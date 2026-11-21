import random
import unittest

from arrays.max_attendable_events import max_attendable_events


class TestMaxAttendableEvents(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_attendable_events([(1, 2), (2, 3), (3, 4)]), 3)

    def test_edges(self):
        self.assertEqual(max_attendable_events([]), 0)
        self.assertEqual(max_attendable_events([(10**12, 10**12)]*3), 1)
        with self.assertRaises(ValueError): max_attendable_events([(2, 1)])

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(176)
        for _ in range(100):
            a = [tuple(sorted((rng.randrange(-2, 5), rng.randrange(-2, 5)))) for _ in range(rng.randrange(8))]
            @lru_cache(None)
            def visit(day, used):
                if day > 4: return 0
                choices = [visit(day+1, used)]
                for i, (start, end) in enumerate(a):
                    if not used >> i & 1 and start <= day <= end:
                        choices.append(1+visit(day+1, used | (1 << i)))
                return max(choices)
            self.assertEqual(max_attendable_events(a), visit(-2, 0))
