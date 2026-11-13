# Sorted squares of a sorted array

The largest remaining square comes from one of the two ends. Fill the result backwards, advancing the end with greater absolute value. The input must be sorted.

Complexity: O(n) time, O(n) output space.

- [Implementation](../arrays/sorted_squares.py)
- [Tests](../tests/test_sorted_squares.py)

Run this exercise: `python -m unittest tests.test_sorted_squares -v`
