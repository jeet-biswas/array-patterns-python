# Next strictly greater element on the right

Scan backwards with a decreasing stack of candidate values. Discard candidates no larger than the current value; the remaining top is the first greater value. Use None for absence so negative results remain unambiguous.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/next_greater_right.py)
- [Tests](../tests/test_next_greater_right.py)

Run this exercise: `python -m unittest tests.test_next_greater_right -v`
