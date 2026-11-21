import random
import unittest

from arrays.valid_stack_sequences import valid_stack_sequences


class TestValidStackSequences(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(valid_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
        self.assertFalse(valid_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

    def test_edges(self):
        self.assertTrue(valid_stack_sequences([], []))
        self.assertFalse(valid_stack_sequences([1], [2]))
        with self.assertRaises(ValueError): valid_stack_sequences([1, 1], [1, 1])

    def test_against_reference(self):
        from itertools import permutations
        def outputs(pushed, stack=(), result=()):
            if not pushed and not stack:
                return {result}
            found = set()
            if pushed: found |= outputs(pushed[1:], stack+(pushed[0],), result)
            if stack: found |= outputs(pushed, stack[:-1], result+(stack[-1],))
            return found
        for n in range(7):
            pushed = list(range(n))
            possible = outputs(tuple(pushed))
            for popped in permutations(pushed):
                self.assertEqual(valid_stack_sequences(pushed, list(popped)), popped in possible)
