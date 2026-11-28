# Count specified values inside many half-open array ranges

Store the sorted occurrence positions of each value. A frequency query is the difference between two lower-bound searches in that value's position list. Missing values use an empty list and return zero.

Complexity: O(n + q log(n + 1)) time, O(n + q) space.

- [Implementation](../arrays/range_value_frequencies.py)
- [Tests](../tests/test_range_value_frequencies.py)

Run this exercise: `python -m unittest tests.test_range_value_frequencies -v`
