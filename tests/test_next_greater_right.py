import random
import unittest

from arrays.next_greater_right import next_greater_right


class TestNextGreaterRight(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(next_greater_right([2, 1, 2, 4, 3]), [4, 2, 4, None, None])
        self.assertEqual(next_greater_right([-3, -1]), [-1, None])

    def test_edges(self):
        self.assertEqual(next_greater_right([]), [])
        self.assertEqual(next_greater_right([2, 2]), [None, None])
        self.assertEqual(next_greater_right([3, 2, 1]), [None, None, None])

    def test_against_reference(self):
        rng = random.Random(42)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(25))]
            expected = [next((y for y in values[i+1:] if y > x), None) for i, x in enumerate(values)]
            self.assertEqual(next_greater_right(values), expected)
