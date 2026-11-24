import random
import unittest

from arrays.max_value_k_events import max_value_k_events


class TestMaxValueKEvents(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_value_k_events([(1, 2, 4), (3, 4, 3), (2, 3, 1)], 2), 7)

    def test_edges(self):
        self.assertEqual(max_value_k_events([], 2), 0)
        self.assertEqual(max_value_k_events([(1, 1, -2)], 1), 0)
        self.assertEqual(max_value_k_events([(1, 2, 5)], 0), 0)
        with self.assertRaises(ValueError): max_value_k_events([], -1)
        with self.assertRaises(ValueError): max_value_k_events([(2, 1, 3)], 1)

    def test_against_reference(self):
        rng = random.Random(197)
        for _ in range(120):
            events = []
            for _ in range(rng.randrange(10)):
                start = rng.randrange(-3, 7)
                events.append((start, start+rng.randrange(4), rng.randrange(-3, 11)))
            k = rng.randrange(5)
            best = 0
            for mask in range(1 << len(events)):
                if mask.bit_count() > k: continue
                chosen = sorted(e for i, e in enumerate(events) if mask >> i & 1)
                if all(a[1] < b[0] for a, b in zip(chosen, chosen[1:])):
                    best = max(best, sum(e[2] for e in chosen))
            self.assertEqual(max_value_k_events(events, k), best)
