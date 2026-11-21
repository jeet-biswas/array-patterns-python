import random
import unittest

from arrays.delete_and_earn import delete_and_earn


class TestDeleteAndEarn(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(delete_and_earn([2, 2, 3, 3, 3, 4]), 9)

    def test_edges(self):
        self.assertEqual(delete_and_earn([]), 0)
        self.assertEqual(delete_and_earn([0, 0]), 0)
        with self.assertRaises(ValueError): delete_and_earn([-1])

    def test_against_reference(self):
        rng = random.Random(146)
        for _ in range(120):
            a = [rng.randrange(7) for _ in range(rng.randrange(12))]
            keys = sorted(set(a))
            best = 0
            for mask in range(1 << len(keys)):
                chosen = {v for i, v in enumerate(keys) if mask >> i & 1}
                if all(v+1 not in chosen for v in chosen):
                    best = max(best, sum(v for v in a if v in chosen))
            self.assertEqual(delete_and_earn(a), best)
