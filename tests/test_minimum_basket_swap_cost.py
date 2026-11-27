import random
import unittest

from arrays.minimum_basket_swap_cost import minimum_basket_swap_cost


class TestMinimumBasketSwapCost(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_basket_swap_cost([4, 2, 2, 2], [1, 4, 1, 2]), 1)
        self.assertEqual(minimum_basket_swap_cost([1, 10, 10], [1, 20, 20]), 2)

    def test_edges(self):
        self.assertEqual(minimum_basket_swap_cost([], []), 0)
        self.assertIsNone(minimum_basket_swap_cost([1], [2]))
        with self.assertRaises(ValueError): minimum_basket_swap_cost([0], [0])
        with self.assertRaises(ValueError): minimum_basket_swap_cost([1], [])

    def test_against_reference(self):
        import heapq
        rng = random.Random(277)
        for _ in range(90):
            n = rng.randrange(5)
            a = [rng.randrange(1, 6) for _ in range(n)]
            b = [rng.randrange(1, 6) for _ in range(n)]
            initial = (tuple(sorted(a)), tuple(sorted(b)))
            queue = [(0, initial)]
            costs = {initial: 0}
            expected = None
            while queue:
                cost, state = heapq.heappop(queue)
                if cost != costs[state]: continue
                x, y = state
                if x == y:
                    expected = cost
                    break
                for i in range(n):
                    for j in range(n):
                        left, right = list(x), list(y)
                        left[i], right[j] = right[j], left[i]
                        following = (tuple(sorted(left)), tuple(sorted(right)))
                        price = cost+min(x[i], y[j])
                        if price < costs.get(following, float('inf')):
                            costs[following] = price
                            heapq.heappush(queue, (price, following))
            self.assertEqual(minimum_basket_swap_cost(a, b), expected)
