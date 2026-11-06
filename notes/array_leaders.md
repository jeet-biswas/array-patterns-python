# Strict leaders from the right

An element is a leader if it is strictly greater than every element to its right. Scan backwards with the maximum seen so far, then reverse the output to restore input order.

Complexity: O(n) time, O(n) output space.

- [Implementation](../arrays/array_leaders.py)
- [Tests](../tests/test_array_leaders.py)

Run this exercise: `python -m unittest tests.test_array_leaders -v`
