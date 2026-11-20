import random
import unittest

from arrays.running_medians import running_medians


class TestRunningMedians(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(running_medians([5, 15, 1, 3]), [5.0, 10.0, 5.0, 4.0])
        self.assertEqual(running_medians([-3, -1, -2]), [-3.0, -2.0, -2.0])

    def test_edges(self):
        self.assertEqual(running_medians([]), [])
        self.assertEqual(running_medians([2, 2, 2]), [2.0, 2.0, 2.0])
        self.assertEqual(running_medians([0]), [0.0])

    def test_against_reference(self):
        from statistics import median
        rng = random.Random(122)
        for _ in range(150):
            values = [rng.randrange(-30, 31) for _ in range(rng.randrange(35))]
            original = values.copy()
            self.assertEqual(running_medians(values), [median(values[:stop]) for stop in range(1, len(values)+1)])
            self.assertEqual(values, original)
