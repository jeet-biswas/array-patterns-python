# Count visible people to the right by height

Scan from right to left. Shorter people popped from the stack are visible, and the first remaining taller person is visible but blocks everyone farther away. Distinct positive heights make the visibility relation strict and avoid equal-height ambiguity.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/visible_people_right.py)
- [Tests](../tests/test_visible_people_right.py)

Run this exercise: `python -m unittest tests.test_visible_people_right -v`
