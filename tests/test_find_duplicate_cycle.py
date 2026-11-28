import random
import unittest

from arrays.find_duplicate_cycle import find_duplicate_cycle


class TestFindDuplicateCycle(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_duplicate_cycle([1, 3, 4, 2, 2]), 2)

    def test_edges(self):
        self.assertEqual(find_duplicate_cycle([1, 1]), 1)
        self.assertEqual(find_duplicate_cycle([2, 2, 2]), 2)
        with self.assertRaises(ValueError): find_duplicate_cycle([])
        with self.assertRaises(ValueError): find_duplicate_cycle([0, 1])

    def test_against_reference(self):
        rng = random.Random(301)
        for _ in range(170):
            n = rng.randrange(1, 80)
            duplicate = rng.randrange(1, n+1)
            copies = rng.randrange(2, n+2)
            others = [x for x in range(1, n+1) if x != duplicate]
            a = [duplicate]*copies+rng.sample(others, n+1-copies)
            rng.shuffle(a)
            before = a.copy()
            self.assertEqual(find_duplicate_cycle(a), duplicate)
            self.assertEqual(a, before)
