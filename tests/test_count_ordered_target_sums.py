import random
import unittest

from arrays.count_ordered_target_sums import count_ordered_target_sums


class TestCountOrderedTargetSums(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_ordered_target_sums([1, 2, 3], 4), 7)

    def test_edges(self):
        self.assertEqual(count_ordered_target_sums([], 0), 1)
        self.assertEqual(count_ordered_target_sums([2, 2], 4), 1)
        self.assertEqual(count_ordered_target_sums([3], 2), 0)
        with self.assertRaises(ValueError): count_ordered_target_sums([0], 3)

    def test_against_reference(self):
        rng = random.Random(254)
        for _ in range(100):
            a = [rng.randrange(1, 6) for _ in range(rng.randrange(5))]
            target = rng.randrange(10)
            pending = [0]
            expected = 0
            while pending:
                total = pending.pop()
                if total == target: expected += 1
                else:
                    pending.extend(total+x for x in set(a) if total+x <= target)
            self.assertEqual(count_ordered_target_sums(a, target), expected)
