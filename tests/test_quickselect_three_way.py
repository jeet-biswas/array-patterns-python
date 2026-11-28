import random
import unittest

from arrays.quickselect_three_way import quickselect_three_way


class TestQuickselectThreeWay(unittest.TestCase):
    def test_examples(self):
        a = [3, 2, 1, 5, 6, 4]
        self.assertEqual(quickselect_three_way(a, 2), 2)

    def test_edges(self):
        self.assertEqual(quickselect_three_way([2, 2, 2], 2), 2)
        with self.assertRaises(ValueError): quickselect_three_way([], 1)
        a = [3, 1]
        with self.assertRaises(ValueError): quickselect_three_way(a, 0)
        self.assertEqual(a, [3, 1])

    def test_against_reference(self):
        rng = random.Random(291)
        for _ in range(180):
            a = [rng.randrange(-20, 21) for _ in range(rng.randrange(1, 100))]
            expected = sorted(a)
            k = rng.randrange(1, len(a)+1)
            self.assertEqual(quickselect_three_way(a, k), expected[k-1])
            self.assertEqual(sorted(a), expected)
