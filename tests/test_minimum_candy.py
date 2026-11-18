import random
import unittest

from arrays.minimum_candy import minimum_candy


class TestMinimumCandy(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimum_candy([1, 0, 2]), 5)
        self.assertEqual(minimum_candy([1, 2, 2]), 4)

    def test_edges(self):
        self.assertEqual(minimum_candy([]), 0)
        self.assertEqual(minimum_candy([-5]), 1)
        self.assertEqual(minimum_candy([3, 3, 3]), 3)
        self.assertEqual(minimum_candy([3, 2, 1]), 6)

    def test_against_reference(self):
        from itertools import product
        rng = random.Random(99)
        for _ in range(70):
            ratings = [rng.randrange(-2, 3) for _ in range(rng.randrange(6))]
            n = len(ratings)
            expected = min(sum(candies) for candies in product(range(1, n+1), repeat=n)
                           if all((ratings[i] <= ratings[i+1] or candies[i] > candies[i+1])
                                  and (ratings[i] >= ratings[i+1] or candies[i] < candies[i+1])
                                  for i in range(n-1)))
            self.assertEqual(minimum_candy(ratings), expected)
