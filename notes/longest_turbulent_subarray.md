# Longest alternating contiguous comparison run

Track contiguous lengths ending in a rise and in a fall. A rise can only extend the preceding fall and resets the fall length to one; equal neighbors reset both. Unlike a subsequence, skipped elements are not allowed.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/longest_turbulent_subarray.py)
- [Tests](../tests/test_longest_turbulent_subarray.py)

Run this exercise: `python -m unittest tests.test_longest_turbulent_subarray -v`
