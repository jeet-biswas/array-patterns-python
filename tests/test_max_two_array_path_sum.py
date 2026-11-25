import random
import unittest

from arrays.max_two_array_path_sum import max_two_array_path_sum


class TestMaxTwoArrayPathSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_two_array_path_sum([2, 4, 5, 8, 10], [4, 6, 8, 9]), 30)

    def test_edges(self):
        self.assertEqual(max_two_array_path_sum([], [1, 2]), 3)
        self.assertEqual(max_two_array_path_sum([], []), 0)
        with self.assertRaises(ValueError): max_two_array_path_sum([1, 1], [])
        with self.assertRaises(ValueError): max_two_array_path_sum([-1], [])

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(227)
        for _ in range(130):
            arrays = [sorted(rng.sample(range(20), rng.randrange(10))) for _ in range(2)]
            @lru_cache(None)
            def walk(side, index):
                if index == len(arrays[side]): return 0
                value = arrays[side][index]
                options = [walk(side, index+1)]
                if value in arrays[1-side]:
                    options.append(walk(1-side, arrays[1-side].index(value)+1))
                return value+max(options)
            self.assertEqual(max_two_array_path_sum(*arrays), max(walk(0, 0), walk(1, 0)))
