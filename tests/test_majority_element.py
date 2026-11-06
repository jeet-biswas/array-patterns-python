import random
import unittest

from arrays.majority_element import majority_element


class TestMajorityElement(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(majority_element([2, 2, 1, 2]), 2)
        self.assertEqual(majority_element([-1, 2, -1]), -1)

    def test_edges(self):
        self.assertIsNone(majority_element([]))
        self.assertIsNone(majority_element([1, 1, 2, 2]))
        self.assertEqual(majority_element([0]), 0)

    def test_against_counts(self):
        from collections import Counter
        rng = random.Random(9)
        for _ in range(100):
            values = [rng.randrange(4) for _ in range(rng.randrange(20))]
            expected = next((x for x, count in Counter(values).items()
                             if count > len(values) // 2), None)
            self.assertEqual(majority_element(values), expected)
