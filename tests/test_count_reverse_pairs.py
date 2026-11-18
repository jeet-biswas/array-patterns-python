import random
import unittest

from arrays.count_reverse_pairs import count_reverse_pairs


class TestCountReversePairs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_reverse_pairs([1, 3, 2, 3, 1]), 2)
        self.assertEqual(count_reverse_pairs([2, 4, 3, 5, 1]), 3)

    def test_edges(self):
        self.assertEqual(count_reverse_pairs([]), 0)
        self.assertEqual(count_reverse_pairs([4]), 0)
        self.assertEqual(count_reverse_pairs([-1, -1]), 1)
        self.assertEqual(count_reverse_pairs([2, 1]), 0)

    def test_against_reference(self):
        rng = random.Random(82)
        for _ in range(150):
            values = [rng.randrange(-20, 21) for _ in range(rng.randrange(25))]
            original = values.copy()
            expected = sum(values[i] > 2*values[j] for i in range(len(values)) for j in range(i+1, len(values)))
            self.assertEqual(count_reverse_pairs(values), expected)
            self.assertEqual(values, original)
