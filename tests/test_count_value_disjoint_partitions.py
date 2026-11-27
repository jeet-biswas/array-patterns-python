import random
import unittest

from arrays.count_value_disjoint_partitions import count_value_disjoint_partitions


class TestCountValueDisjointPartitions(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_value_disjoint_partitions([1, 2, 1, 3, 4, 3]), 2)
        self.assertEqual(count_value_disjoint_partitions([1, 2, 3, 4]), 8)

    def test_edges(self):
        self.assertEqual(count_value_disjoint_partitions([]), 1)
        self.assertEqual(count_value_disjoint_partitions([2, 2, 2]), 1)

    def test_against_reference(self):
        rng = random.Random(284)
        for _ in range(140):
            a = [rng.randrange(-3, 4) for _ in range(rng.randrange(1, 12))]
            expected = 0
            for mask in range(1 << (len(a)-1)):
                ends = [0]+[i+1 for i in range(len(a)-1) if mask >> i & 1]+[len(a)]
                blocks = [set(a[left:right]) for left, right in zip(ends, ends[1:])]
                expected += sum(map(len, blocks)) == len(set(a))
            self.assertEqual(count_value_disjoint_partitions(a), expected)
