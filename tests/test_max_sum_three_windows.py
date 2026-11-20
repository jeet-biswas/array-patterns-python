import random
import unittest

from arrays.max_sum_three_windows import max_sum_three_windows


class TestMaxSumThreeWindows(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_sum_three_windows([1, 2, 1, 2, 6, 7, 5, 1], 2), (0, 3, 5))
        self.assertEqual(max_sum_three_windows([1, 1, 1, 1, 1, 1], 1), (0, 1, 2))

    def test_edges(self):
        self.assertEqual(max_sum_three_windows([-5, -2, -3], 1), (0, 1, 2))
        for values, width in [([], 1), ([1, 2], 1), ([1, 2, 3], 0)]:
            with self.assertRaises(ValueError):
                max_sum_three_windows(values, width)

    def test_against_reference(self):
        from itertools import combinations
        rng = random.Random(123)
        for _ in range(120):
            values = [rng.randrange(-8, 9) for _ in range(rng.randrange(3, 16))]
            width = rng.randrange(1, len(values)//3+1)
            candidates = [starts for starts in combinations(range(len(values)-width+1), 3)
                          if starts[0]+width <= starts[1] and starts[1]+width <= starts[2]]
            expected = min(candidates, key=lambda starts: (-sum(sum(values[i:i+width]) for i in starts), starts))
            self.assertEqual(max_sum_three_windows(values, width), expected)
