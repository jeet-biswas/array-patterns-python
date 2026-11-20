# Minimize paired absolute differences with one replacement

Compute the baseline distance, then find the largest possible saving at one index. Binary search in the sorted original first array locates the nearest allowed replacement to each second-array value.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/min_absolute_sum_difference.py)
- [Tests](../tests/test_min_absolute_sum_difference.py)

Run this exercise: `python -m unittest tests.test_min_absolute_sum_difference -v`
