import random
import unittest

from arrays.majority_over_third import majority_over_third


class TestMajorityOverThird(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(majority_over_third([1, 1, 1, 3, 3, 2, 2, 2]), [1, 2])

    def test_edges(self):
        self.assertEqual(majority_over_third([]), [])
        self.assertEqual(majority_over_third([1, 2, 3]), [])
        self.assertEqual(majority_over_third([2]), [2])

    def test_against_reference(self):
        rng = random.Random(302)
        for _ in range(200):
            a = [rng.randrange(-3, 4) for _ in range(rng.randrange(100))]
            expected = sorted(x for x in set(a) if 3*a.count(x) > len(a))
            self.assertEqual(majority_over_third(a), expected)
