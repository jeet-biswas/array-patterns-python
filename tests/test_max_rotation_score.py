import random
import unittest

from arrays.max_rotation_score import max_rotation_score


class TestMaxRotationScore(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_rotation_score([4, 3, 2, 6]), 26)
        self.assertEqual(max_rotation_score([-1, -2, -3]), -5)

    def test_edges(self):
        self.assertEqual(max_rotation_score([]), 0)
        self.assertEqual(max_rotation_score([8]), 0)
        self.assertEqual(max_rotation_score([2, 2, 2]), 6)

    def test_against_reference(self):
        rng = random.Random(91)
        for _ in range(150):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(20))]
            expected = max((sum(i*x for i, x in enumerate(values[k:]+values[:k]))
                            for k in range(len(values))), default=0)
            self.assertEqual(max_rotation_score(values), expected)
