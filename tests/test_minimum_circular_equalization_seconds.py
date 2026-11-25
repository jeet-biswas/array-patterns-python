import random
import unittest

from arrays.minimum_circular_equalization_seconds import minimum_circular_equalization_seconds


class TestMinimumCircularEqualizationSeconds(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_circular_equalization_seconds([1, 2, 1, 2]), 1)

    def test_edges(self):
        self.assertEqual(minimum_circular_equalization_seconds([]), 0)
        self.assertEqual(minimum_circular_equalization_seconds([4, 4]), 0)

    def test_against_reference(self):
        rng = random.Random(212)
        for _ in range(150):
            a = [rng.randrange(5) for _ in range(rng.randrange(1, 20))]
            delays = []
            for target in set(a):
                reached = {i for i, x in enumerate(a) if x == target}
                seconds = 0
                while len(reached) < len(a):
                    reached = reached | {(i-1) % len(a) for i in reached} | {(i+1) % len(a) for i in reached}
                    seconds += 1
                delays.append(seconds)
            self.assertEqual(minimum_circular_equalization_seconds(a), min(delays))
