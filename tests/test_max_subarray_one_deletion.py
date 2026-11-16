import random
import unittest

from arrays.max_subarray_one_deletion import max_subarray_one_deletion


class TestMaxSubarrayOneDeletion(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_subarray_one_deletion([1, -2, 0, 3]), 4)
        self.assertEqual(max_subarray_one_deletion([1, -2, -2, 3]), 3)

    def test_edges(self):
        self.assertEqual(max_subarray_one_deletion([-1, -2, -3]), -1)
        self.assertEqual(max_subarray_one_deletion([-7]), -7)
        self.assertEqual(max_subarray_one_deletion([0, 0]), 0)
        with self.assertRaises(ValueError):
            max_subarray_one_deletion([])

    def test_against_reference(self):
        rng = random.Random(80)
        for _ in range(150):
            values = [rng.randrange(-7, 8) for _ in range(rng.randrange(1, 13))]
            candidates = []
            for i in range(len(values)):
                for j in range(i+1, len(values)+1):
                    total = sum(values[i:j])
                    candidates.append(total)
                    if j-i > 1:
                        candidates.extend(total-values[k] for k in range(i, j))
            self.assertEqual(max_subarray_one_deletion(values), max(candidates))
