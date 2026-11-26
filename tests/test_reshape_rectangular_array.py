import random
import unittest

from arrays.reshape_rectangular_array import reshape_rectangular_array


class TestReshapeRectangularArray(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(reshape_rectangular_array([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]])

    def test_edges(self):
        self.assertIsNone(reshape_rectangular_array([[1, 2]], 2, 2))
        self.assertEqual(reshape_rectangular_array([], 3, 0), [[], [], []])
        with self.assertRaises(ValueError): reshape_rectangular_array([[1], []], 1, 1)
        with self.assertRaises(ValueError): reshape_rectangular_array([], -1, 0)

    def test_against_reference(self):
        rng = random.Random(248)
        for _ in range(120):
            r, c = rng.randrange(1, 8), rng.randrange(1, 8)
            a = [[rng.randrange(-8, 9) for _ in range(c)] for _ in range(r)]
            flat = [x for row in a for x in row]
            rows = rng.choice([d for d in range(1, r*c+1) if r*c % d == 0])
            columns = r*c//rows
            result = reshape_rectangular_array(a, rows, columns)
            self.assertEqual(result, [flat[i:i+columns] for i in range(0, len(flat), columns)])
            self.assertEqual(len({id(row) for row in result}), rows)
            self.assertFalse({id(row) for row in result} & {id(row) for row in a})
