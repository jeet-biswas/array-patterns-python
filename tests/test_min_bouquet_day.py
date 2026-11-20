import random
import unittest

from arrays.min_bouquet_day import min_bouquet_day


class TestMinBouquetDay(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_bouquet_day([1, 10, 3, 10, 2], 3, 1), 3)
        self.assertEqual(min_bouquet_day([7, 7, 7, 7, 12, 7, 7], 2, 3), 12)

    def test_edges(self):
        self.assertEqual(min_bouquet_day([], 0, 1), 0)
        self.assertEqual(min_bouquet_day([1, 2], 2, 2), -1)
        self.assertEqual(min_bouquet_day([0, 0], 1, 2), 0)
        for days, count, size in [([-1], 1, 1), ([1], -1, 1), ([1], 1, 0)]:
            with self.assertRaises(ValueError):
                min_bouquet_day(days, count, size)

    def test_against_reference(self):
        rng = random.Random(138)
        for _ in range(150):
            days = [rng.randrange(9) for _ in range(rng.randrange(12))]
            count, size = rng.randrange(5), rng.randrange(1, 5)
            expected = -1
            for day in range(max(days, default=0)+1):
                dp = [0] * (len(days)+1)
                for stop in range(1, len(days)+1):
                    dp[stop] = dp[stop-1]
                    if stop >= size and all(x <= day for x in days[stop-size:stop]):
                        dp[stop] = max(dp[stop], dp[stop-size]+1)
                if dp[-1] >= count:
                    expected = day
                    break
            self.assertEqual(min_bouquet_day(days, count, size), expected)
