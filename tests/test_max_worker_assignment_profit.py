import random
import unittest

from arrays.max_worker_assignment_profit import max_worker_assignment_profit


class TestMaxWorkerAssignmentProfit(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_worker_assignment_profit([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]), 100)

    def test_edges(self):
        self.assertEqual(max_worker_assignment_profit([], [], [1, 2]), 0)
        with self.assertRaises(ValueError): max_worker_assignment_profit([1], [], [])
        with self.assertRaises(ValueError): max_worker_assignment_profit([], [], [-1])

    def test_against_reference(self):
        rng = random.Random(271)
        for _ in range(170):
            n = rng.randrange(15)
            difficulty = [rng.randrange(15) for _ in range(n)]
            profit = [rng.randrange(30) for _ in range(n)]
            workers = [rng.randrange(18) for _ in range(rng.randrange(15))]
            expected = sum(max((p for d, p in zip(difficulty, profit) if d <= ability), default=0) for ability in workers)
            self.assertEqual(max_worker_assignment_profit(difficulty, profit, workers), expected)
