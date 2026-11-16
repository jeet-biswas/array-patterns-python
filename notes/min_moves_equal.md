# Minimum unit moves to equalize an array

A median minimizes the sum of absolute distances. Sorting a copy identifies a median; sum each value's distance from it. For even lengths, either central value gives the same minimum.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/min_moves_equal.py)
- [Tests](../tests/test_min_moves_equal.py)

Run this exercise: `python -m unittest tests.test_min_moves_equal -v`
