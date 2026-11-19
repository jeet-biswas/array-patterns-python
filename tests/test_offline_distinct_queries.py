import random
import unittest

from arrays.offline_distinct_queries import offline_distinct_queries


class TestOfflineDistinctQueries(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(offline_distinct_queries([1, 2, 1, 3, 2], [(0, 5), (1, 4), (2, 3), (0, 2)]), [3, 3, 1, 2])
        self.assertEqual(offline_distinct_queries([2, 2], [(0, 2), (0, 2)]), [1, 1])

    def test_edges(self):
        self.assertEqual(offline_distinct_queries([], [(0, 0)]), [0])
        self.assertEqual(offline_distinct_queries([1], []), [])
        for queries in [[(-1, 1)], [(1, 0)], [(0, 2)], [(0,)]]:
            with self.assertRaises(ValueError):
                offline_distinct_queries([1], queries)

    def test_against_reference(self):
        rng = random.Random(116)
        for _ in range(100):
            values = [rng.randrange(-4, 5) for _ in range(rng.randrange(25))]
            queries = [tuple(sorted((rng.randrange(len(values)+1), rng.randrange(len(values)+1)))) for _ in range(30)]
            original = values.copy(), queries.copy()
            self.assertEqual(offline_distinct_queries(values, queries), [len(set(values[a:b])) for a, b in queries])
            self.assertEqual((values, queries), original)
