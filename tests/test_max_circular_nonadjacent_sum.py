import random
import unittest

from arrays.max_circular_nonadjacent_sum import max_circular_nonadjacent_sum


class TestMaxCircularNonadjacentSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_circular_nonadjacent_sum([2, 3, 2]), 3)
        self.assertEqual(max_circular_nonadjacent_sum([1, 2, 3, 1]), 4)

    def test_edges(self):
        self.assertEqual(max_circular_nonadjacent_sum([]), 0)
        self.assertEqual(max_circular_nonadjacent_sum([-1]), 0)
        self.assertEqual(max_circular_nonadjacent_sum([8]), 8)

    def test_against_reference(self):
        rng = random.Random(147)
        for _ in range(120):
            a = [rng.randrange(-5, 10) for _ in range(rng.randrange(10))]
            scores = [0]
            for mask in range(1 << len(a)):
                if len(a) > 1 and any(mask >> i & 1 and mask >> ((i+1) % len(a)) & 1 for i in range(len(a))):
                    continue
                scores.append(sum(x for i, x in enumerate(a) if mask >> i & 1))
            self.assertEqual(max_circular_nonadjacent_sum(a), max(scores))
