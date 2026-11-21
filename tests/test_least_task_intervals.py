import random
import unittest

from arrays.least_task_intervals import least_task_intervals


class TestLeastTaskIntervals(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(least_task_intervals([1, 1, 1, 2, 2, 2], 2), 8)

    def test_edges(self):
        self.assertEqual(least_task_intervals([], 3), 0)
        self.assertEqual(least_task_intervals([1, 1, 2], 0), 3)
        with self.assertRaises(ValueError): least_task_intervals([], -1)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(178)
        for _ in range(70):
            tasks = [rng.randrange(3) for _ in range(rng.randrange(8))]
            gap = rng.randrange(4)
            counts = tuple(tasks.count(i) for i in range(3))
            @lru_cache(None)
            def schedule(remaining, waits):
                if not any(remaining): return 0
                ready = [i for i in range(3) if remaining[i] and waits[i] == 0]
                next_waits = tuple(max(0, w-1) for w in waits)
                if not ready: return 1+schedule(remaining, next_waits)
                scores = []
                for i in ready:
                    left, after = list(remaining), list(next_waits)
                    left[i] -= 1
                    after[i] = gap
                    scores.append(1+schedule(tuple(left), tuple(after)))
                return min(scores)
            self.assertEqual(least_task_intervals(tasks, gap), schedule(counts, (0, 0, 0)))
