import random
import unittest

from arrays.minimize_max_after_left_moves import minimize_max_after_left_moves


class TestMinimizeMaxAfterLeftMoves(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimize_max_after_left_moves([3, 7, 1, 6]), 5)

    def test_edges(self):
        self.assertEqual(minimize_max_after_left_moves([]), 0)
        self.assertEqual(minimize_max_after_left_moves([10, 1]), 10)
        with self.assertRaises(ValueError): minimize_max_after_left_moves([-1])

    def test_against_reference(self):
        rng = random.Random(211)
        for _ in range(70):
            a = tuple(rng.randrange(4) for _ in range(rng.randrange(1, 5)))
            seen, pending = {a}, [a]
            while pending:
                state = pending.pop()
                for i in range(1, len(state)):
                    if state[i]:
                        following = list(state)
                        following[i] -= 1
                        following[i-1] += 1
                        following = tuple(following)
                        if following not in seen:
                            seen.add(following)
                            pending.append(following)
            self.assertEqual(minimize_max_after_left_moves(list(a)), min(max(s) for s in seen))
