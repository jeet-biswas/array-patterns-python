import random
import unittest

from arrays.count_bad_pairs import count_bad_pairs


class TestCountBadPairs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_bad_pairs([4, 1, 3, 3]), 5)
        self.assertEqual(count_bad_pairs([1, 2, 3, 4, 5]), 0)

    def test_edges(self):
        self.assertEqual(count_bad_pairs([]), 0)
        self.assertEqual(count_bad_pairs([7]), 0)
        self.assertEqual(count_bad_pairs([0, 0, 0]), 3)
        self.assertEqual(count_bad_pairs([-3, -2, -1]), 0)

    def test_against_reference(self):
        rng = random.Random(130)
        for _ in range(150):
            values = [rng.randrange(-10, 11) for _ in range(rng.randrange(25))]
            expected = sum(j-i != values[j]-values[i] for i in range(len(values)) for j in range(i+1, len(values)))
            self.assertEqual(count_bad_pairs(values), expected)
