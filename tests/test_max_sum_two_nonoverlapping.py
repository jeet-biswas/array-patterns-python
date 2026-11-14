import random
import unittest

from arrays.max_sum_two_nonoverlapping import max_sum_two_nonoverlapping


class TestMaxSumTwoNonoverlapping(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_two_nonoverlapping([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2), 20)
        self.assertEqual(max_sum_two_nonoverlapping([-5, -1, -3], 1, 1), -4)

    def test_edges(self):
        self.assertEqual(max_sum_two_nonoverlapping([1, 2, 3], 1, 2), 6)
        for values, a, b in [([], 1, 1), ([1], 1, 1), ([1, 2], 0, 1), ([1, 2], 1, -1)]:
            with self.assertRaises(ValueError):
                max_sum_two_nonoverlapping(values, a, b)

    def test_against_reference(self):
        rng = random.Random(54)
        for _ in range(150):
            values = [rng.randrange(-7, 10) for _ in range(rng.randrange(2, 14))]
            a = rng.randrange(1, len(values))
            b = rng.randrange(1, len(values)-a+1)
            expected = max(sum(values[i:i+a])+sum(values[j:j+b])
                           for i in range(len(values)-a+1) for j in range(len(values)-b+1)
                           if i+a <= j or j+b <= i)
            self.assertEqual(max_sum_two_nonoverlapping(values, a, b), expected)
