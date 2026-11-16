import random
import unittest

from arrays.merge_into_buffer import merge_into_buffer


class TestMergeIntoBuffer(unittest.TestCase):
    def test_examples(self):
        values = [1, 2, 3, 0, 0, 0]
        source = [2, 5, 6]
        self.assertIsNone(merge_into_buffer(values, 3, source))
        self.assertEqual(values, [1, 2, 2, 3, 5, 6])
        self.assertEqual(source, [2, 5, 6])

    def test_edges(self):
        values = [0, 0]
        merge_into_buffer(values, 0, [-2, 3])
        self.assertEqual(values, [-2, 3])
        merge_into_buffer([], 0, [])
        for dest, count, source in [([1], 1, [2]), ([1], -1, [2, 3])]:
            with self.assertRaises(ValueError):
                merge_into_buffer(dest, count, source)
        values = [1]
        with self.assertRaises(ValueError):
            merge_into_buffer(values, 0, values)

    def test_against_reference(self):
        rng = random.Random(61)
        for _ in range(150):
            left = sorted(rng.randrange(-7, 8) for _ in range(rng.randrange(15)))
            right = sorted(rng.randrange(-7, 8) for _ in range(rng.randrange(15)))
            destination = left + [999] * len(right)
            merge_into_buffer(destination, len(left), right)
            self.assertEqual(destination, sorted(left+right))
