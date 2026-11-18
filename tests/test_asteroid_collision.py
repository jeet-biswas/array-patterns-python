import random
import unittest

from arrays.asteroid_collision import asteroid_collision


class TestAsteroidCollision(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(asteroid_collision([5, 10, -5]), [5, 10])
        self.assertEqual(asteroid_collision([10, 2, -5]), [10])
        self.assertEqual(asteroid_collision([8, -8]), [])

    def test_edges(self):
        self.assertEqual(asteroid_collision([]), [])
        self.assertEqual(asteroid_collision([-2, -1, 1, 2]), [-2, -1, 1, 2])
        with self.assertRaises(ValueError):
            asteroid_collision([1, 0, -2])

    def test_against_reference(self):
        rng = random.Random(93)
        for _ in range(150):
            values = [rng.choice([-5, -3, -1, 1, 3, 5]) for _ in range(rng.randrange(20))]
            expected = values.copy()
            while True:
                i = next((i for i in range(len(expected)-1) if expected[i] > 0 > expected[i+1]), None)
                if i is None:
                    break
                a, b = expected[i:i+2]
                replacement = [a] if a > -b else ([b] if a < -b else [])
                expected[i:i+2] = replacement
            original = values.copy()
            self.assertEqual(asteroid_collision(values), expected)
            self.assertEqual(values, original)
