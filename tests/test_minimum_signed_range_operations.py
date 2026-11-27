import random
import unittest

from arrays.minimum_signed_range_operations import minimum_signed_range_operations


class TestMinimumSignedRangeOperations(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_signed_range_operations([0, 0, 0], [2, -1, 2]), 5)
        self.assertEqual(minimum_signed_range_operations([1, 2, 3], [3, 4, 5]), 2)

    def test_edges(self):
        self.assertEqual(minimum_signed_range_operations([], []), 0)
        self.assertEqual(minimum_signed_range_operations([2], [-3]), 5)
        with self.assertRaises(ValueError): minimum_signed_range_operations([1], [])

    def test_against_reference(self):
        from collections import deque
        rng = random.Random(279)
        for _ in range(70):
            n = rng.randrange(1, 4)
            delta = tuple(rng.randrange(-1, 2) for _ in range(n))
            initial = (0,)*n
            queue = deque([(initial, 0)])
            seen = {initial}
            while queue:
                state, cost = queue.popleft()
                if state == delta:
                    source = [rng.randrange(-4, 5) for _ in range(n)]
                    target = [x+d for x, d in zip(source, delta)]
                    self.assertEqual(minimum_signed_range_operations(source, target), cost)
                    break
                for left in range(n):
                    for right in range(left+1, n+1):
                        for step in (-1, 1):
                            following = tuple(x+step*int(left <= i < right) for i, x in enumerate(state))
                            if all(-2 <= x <= 2 for x in following) and following not in seen:
                                seen.add(following)
                                queue.append((following, cost+1))
