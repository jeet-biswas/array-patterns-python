import random
import unittest

from arrays.visible_people_right import visible_people_right


class TestVisiblePeopleRight(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(visible_people_right([10, 6, 8, 5, 11, 9]), [3, 1, 2, 1, 1, 0])

    def test_edges(self):
        self.assertEqual(visible_people_right([]), [])
        self.assertEqual(visible_people_right([3]), [0])
        with self.assertRaises(ValueError): visible_people_right([2, 2])
        with self.assertRaises(ValueError): visible_people_right([0])

    def test_against_reference(self):
        rng = random.Random(171)
        for _ in range(150):
            a = rng.sample(range(1, 40), rng.randrange(15))
            expected = [sum(all(a[k] < min(a[i], a[j]) for k in range(i+1, j)) for j in range(i+1, len(a))) for i in range(len(a))]
            self.assertEqual(visible_people_right(a), expected)
