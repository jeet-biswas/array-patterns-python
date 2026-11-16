import random
import unittest

from arrays.count_lis import count_lis


class TestCountLis(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_lis([1, 3, 5, 4, 7]), 2)
        self.assertEqual(count_lis([2, 2, 2, 2, 2]), 5)

    def test_edges(self):
        self.assertEqual(count_lis([]), 0)
        self.assertEqual(count_lis([8]), 1)
        self.assertEqual(count_lis([3, 2, 1]), 3)

    def test_against_reference(self):
        rng = random.Random(72)
        for _ in range(100):
            values = [rng.randrange(6) for _ in range(rng.randrange(1, 11))]
            lengths = []
            for mask in range(1, 1 << len(values)):
                sequence = [x for i, x in enumerate(values) if mask & (1 << i)]
                if all(a < b for a, b in zip(sequence, sequence[1:])):
                    lengths.append(len(sequence))
            self.assertEqual(count_lis(values), lengths.count(max(lengths)))
