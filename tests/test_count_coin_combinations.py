import random
import unittest

from arrays.count_coin_combinations import count_coin_combinations


class TestCountCoinCombinations(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_coin_combinations([1, 2, 5], 5), 4)

    def test_edges(self):
        self.assertEqual(count_coin_combinations([], 0), 1)
        self.assertEqual(count_coin_combinations([2, 2], 4), 1)
        self.assertEqual(count_coin_combinations([], 1), 0)
        with self.assertRaises(ValueError): count_coin_combinations([-1], 2)

    def test_against_reference(self):
        from functools import lru_cache
        rng = random.Random(253)
        for _ in range(150):
            coins = [rng.randrange(1, 9) for _ in range(rng.randrange(7))]
            target = rng.randrange(25)
            unique = sorted(set(coins))
            @lru_cache(None)
            def choose(i, left):
                if i == len(unique): return int(left == 0)
                return sum(choose(i+1, left-count*unique[i]) for count in range(left//unique[i]+1))
            self.assertEqual(count_coin_combinations(coins, target), choose(0, target))
