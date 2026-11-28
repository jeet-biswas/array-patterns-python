# Longest window attaining the maximum possible subarray AND

A subarray AND cannot exceed any of its nonnegative elements, and a singleton containing the largest element achieves the maximum. Any other element retaining all bits of that maximum would have to be at least as large, so the longest optimal window is a consecutive run of the array maximum.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/longest_maximum_and_subarray.py)
- [Tests](../tests/test_longest_maximum_and_subarray.py)

Run this exercise: `python -m unittest tests.test_longest_maximum_and_subarray -v`
