# Sum of every subarray minimum

A monotonic stack counts the subarrays for which each position supplies the minimum. Pop on greater-than-or-equal values: the previous boundary is strictly smaller and the next boundary is smaller-or-equal, assigning duplicate minima exactly once.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/sum_subarray_minimums.py)
- [Tests](../tests/test_sum_subarray_minimums.py)

Run this exercise: `python -m unittest tests.test_sum_subarray_minimums -v`
