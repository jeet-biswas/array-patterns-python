import random
import unittest

from arrays.minimum_range_increments import minimum_range_increments


class TestMinimumRangeIncrements(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_range_increments([1, 2, 3, 2, 1]), 3)
        self.assertEqual(minimum_range_increments([3, 1, 1, 2]), 4)

    def test_edges(self):
        self.assertEqual(minimum_range_increments([]), 0)
        self.assertEqual(minimum_range_increments([0, 0]), 0)
        with self.assertRaises(ValueError): minimum_range_increments([-1])

    def test_against_reference(self):
        from collections import deque
        rng = random.Random(278)
        for _ in range(90):
            target = tuple(rng.randrange(4) for _ in range(rng.randrange(5)))
            initial = (0,)*len(target)
            queue = deque([(initial, 0)])
            seen = {initial}
            while queue:
                state, cost = queue.popleft()
                if state == target:
                    self.assertEqual(minimum_range_increments(list(target)), cost)
                    break
                for left in range(len(target)):
                    for right in range(left+1, len(target)+1):
                        if all(state[i] < target[i] for i in range(left, right)):
                            following = tuple(x+int(left <= i < right) for i, x in enumerate(state))
                            if following not in seen:
                                seen.add(following)
                                queue.append((following, cost+1))
