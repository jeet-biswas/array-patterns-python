import random
import unittest

from arrays.min_swaps_permutation import min_swaps_permutation


class TestMinSwapsPermutation(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_swaps_permutation([2, 0, 1]), 2)
        self.assertEqual(min_swaps_permutation([1, 0, 3, 2]), 2)

    def test_edges(self):
        self.assertEqual(min_swaps_permutation([]), 0)
        self.assertEqual(min_swaps_permutation([0, 1, 2]), 0)
        for values in ([0, 0], [-1], [1, 2]):
            with self.assertRaises(ValueError):
                min_swaps_permutation(values)

    def test_against_reference(self):
        from collections import deque
        for n in range(6):
            start = tuple(range(n))
            distances = {start: 0}
            queue = deque([start])
            while queue:
                state = queue.popleft()
                for i in range(n):
                    for j in range(i+1, n):
                        candidate = list(state)
                        candidate[i], candidate[j] = candidate[j], candidate[i]
                        candidate = tuple(candidate)
                        if candidate not in distances:
                            distances[candidate] = distances[state]+1
                            queue.append(candidate)
            for state, expected in distances.items():
                values = list(state)
                self.assertEqual(min_swaps_permutation(values), expected)
                self.assertEqual(values, list(state))
