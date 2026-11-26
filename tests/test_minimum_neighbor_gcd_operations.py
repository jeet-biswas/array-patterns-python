import random
import unittest

from arrays.minimum_neighbor_gcd_operations import minimum_neighbor_gcd_operations


class TestMinimumNeighborGcdOperations(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_neighbor_gcd_operations([2, 6, 3, 4]), 4)

    def test_edges(self):
        self.assertEqual(minimum_neighbor_gcd_operations([]), 0)
        self.assertEqual(minimum_neighbor_gcd_operations([1, 2, 1, 3]), 2)
        self.assertEqual(minimum_neighbor_gcd_operations([2, 4, 6]), -1)
        with self.assertRaises(ValueError): minimum_neighbor_gcd_operations([0])

    def test_against_reference(self):
        from collections import deque
        from math import gcd
        rng = random.Random(261)
        for _ in range(80):
            a = tuple(rng.randrange(1, 8) for _ in range(rng.randrange(1, 5)))
            queue = deque([(a, 0)])
            seen = {a}
            expected = -1
            while queue:
                state, depth = queue.popleft()
                if all(x == 1 for x in state):
                    expected = depth
                    break
                for i in range(len(state)-1):
                    common = gcd(state[i], state[i+1])
                    for changed in (i, i+1):
                        result = list(state)
                        result[changed] = common
                        result = tuple(result)
                        if result not in seen:
                            seen.add(result)
                            queue.append((result, depth+1))
            self.assertEqual(minimum_neighbor_gcd_operations(list(a)), expected)
