import random
import unittest

from arrays.circular_next_greater import circular_next_greater


class TestCircularNextGreater(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(circular_next_greater([1, 2, 1]), [2, None, 2])
        self.assertEqual(circular_next_greater([3, 1, 2]), [None, 2, 3])

    def test_edges(self):
        self.assertEqual(circular_next_greater([]), [])
        self.assertEqual(circular_next_greater([4]), [None])
        self.assertEqual(circular_next_greater([2, 2]), [None, None])
        self.assertEqual(circular_next_greater([-2, -1]), [-1, None])

    def test_against_reference(self):
        rng = random.Random(92)
        for _ in range(150):
            values = [rng.randrange(-6, 7) for _ in range(rng.randrange(20))]
            n = len(values)
            expected = [next((values[(i+step) % n] for step in range(1, n)
                              if values[(i+step) % n] > value), None) for i, value in enumerate(values)]
            self.assertEqual(circular_next_greater(values), expected)
