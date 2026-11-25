import random
import unittest

from arrays.min_adjacent_swaps_alternating import min_adjacent_swaps_alternating


class TestMinAdjacentSwapsAlternating(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_adjacent_swaps_alternating([1, 1, 1, 0, 0, 0]), 3)

    def test_edges(self):
        self.assertEqual(min_adjacent_swaps_alternating([]), 0)
        self.assertEqual(min_adjacent_swaps_alternating([1, 1, 1]), -1)
        with self.assertRaises(ValueError): min_adjacent_swaps_alternating([2])

    def test_against_reference(self):
        from collections import deque
        from itertools import product
        for n in range(7):
            for bits in product((0, 1), repeat=n):
                queue = deque([(bits, 0)])
                seen = {bits}
                expected = -1
                while queue:
                    state, depth = queue.popleft()
                    if all(x != y for x, y in zip(state, state[1:])):
                        expected = depth
                        break
                    for i in range(n-1):
                        after = list(state)
                        after[i], after[i+1] = after[i+1], after[i]
                        after = tuple(after)
                        if after not in seen:
                            seen.add(after)
                            queue.append((after, depth+1))
                self.assertEqual(min_adjacent_swaps_alternating(list(bits)), expected)
