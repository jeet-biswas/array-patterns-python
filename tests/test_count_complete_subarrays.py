import random
import unittest

from arrays.count_complete_subarrays import count_complete_subarrays


class TestCountCompleteSubarrays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_complete_subarrays([1, 3, 1, 2, 2]), 4)

    def test_edges(self):
        self.assertEqual(count_complete_subarrays([]), 0)
        self.assertEqual(count_complete_subarrays([5, 5, 5]), 6)

    def test_against_reference(self):
        rng = random.Random(155)
        for _ in range(150):
            a = [rng.randrange(5) for _ in range(rng.randrange(12))]
            expected = sum(set(a[i:j]) == set(a) for i in range(len(a)) for j in range(i+1, len(a)+1))
            self.assertEqual(count_complete_subarrays(a), expected)
