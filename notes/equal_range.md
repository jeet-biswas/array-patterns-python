# Lower and upper bounds in a sorted array

Two binary searches find the first value at least the target and the first value greater than it. The half-open interval contains all occurrences; an absent target produces two equal insertion positions.

Complexity: O(log(n + 1)) time, O(1) space.

- [Implementation](../arrays/equal_range.py)
- [Tests](../tests/test_equal_range.py)

Run this exercise: `python -m unittest tests.test_equal_range -v`
