# Largest sum of a duplicate-free contiguous window

Keep a window of unique values and its sum. On a repeated value, remove elements from the left through its previous occurrence. Nonnegative elements ensure the longest valid suffix is also a best-sum suffix for that endpoint.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/max_unique_subarray_sum.py)
- [Tests](../tests/test_max_unique_subarray_sum.py)

Run this exercise: `python -m unittest tests.test_max_unique_subarray_sum -v`
