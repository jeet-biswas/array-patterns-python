import random
import unittest

from arrays.minimum_coin_count import minimum_coin_count


class TestMinimumCoinCount(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_coin_count([1, 2, 5], 11), 3)

    def test_edges(self):
        self.assertEqual(minimum_coin_count([], 0), 0)
        self.assertIsNone(minimum_coin_count([2], 3))
        with self.assertRaises(ValueError): minimum_coin_count([0], 1)
        with self.assertRaises(ValueError): minimum_coin_count([], -1)

    def test_against_reference(self):
        from collections import deque
        rng = random.Random(252)
        for _ in range(150):
            coins = [rng.randrange(1, 10) for _ in range(rng.randrange(7))]
            target = rng.randrange(30)
            queue = deque([(0, 0)])
            seen = {0}
            expected = None
            while queue:
                amount, depth = queue.popleft()
                if amount == target:
                    expected = depth
                    break
                for coin in coins:
                    nxt = amount+coin
                    if nxt <= target and nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, depth+1))
            self.assertEqual(minimum_coin_count(coins, target), expected)
