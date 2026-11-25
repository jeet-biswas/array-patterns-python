import random
import unittest

from arrays.minimum_job_schedule_difficulty import minimum_job_schedule_difficulty


class TestMinimumJobScheduleDifficulty(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_job_schedule_difficulty([6, 5, 4, 3, 2, 1], 2), 7)

    def test_edges(self):
        self.assertEqual(minimum_job_schedule_difficulty([], 0), 0)
        self.assertIsNone(minimum_job_schedule_difficulty([1], 2))
        self.assertIsNone(minimum_job_schedule_difficulty([1], 0))
        with self.assertRaises(ValueError): minimum_job_schedule_difficulty([-1], 1)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(220)
        for _ in range(120):
            a = [rng.randrange(10) for _ in range(rng.randrange(1, 10))]
            days = rng.randrange(1, len(a)+1)
            candidates = []
            for cuts in combinations(range(1, len(a)), days-1):
                ends = (0,)+cuts+(len(a),)
                candidates.append(sum(max(a[x:y]) for x, y in zip(ends, ends[1:])))
            self.assertEqual(minimum_job_schedule_difficulty(a, days), min(candidates))
