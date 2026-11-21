import random
import unittest

from arrays.can_pair_doubles import can_pair_doubles


class TestCanPairDoubles(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(can_pair_doubles([4, -2, 2, -4]))
        self.assertFalse(can_pair_doubles([3, 1, 3, 6]))

    def test_edges(self):
        self.assertTrue(can_pair_doubles([]))
        self.assertTrue(can_pair_doubles([0, 0]))
        self.assertFalse(can_pair_doubles([0, 1]))

    def test_against_reference(self):
        def possible(a):
            if not a: return True
            for j in range(1, len(a)):
                if a[0] == 2*a[j] or a[j] == 2*a[0]:
                    if possible(a[1:j]+a[j+1:]): return True
            return False
        rng = random.Random(167)
        for _ in range(180):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(9))]
            self.assertEqual(can_pair_doubles(a), possible(a))
