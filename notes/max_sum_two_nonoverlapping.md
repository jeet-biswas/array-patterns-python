# Best sum of two fixed-length disjoint subarrays

Use prefix sums for constant-time window totals. Sweep the second window while remembering the best first window that ends before it. Repeat with the lengths reversed to cover both possible orders, including all-negative inputs.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_sum_two_nonoverlapping.py)
- [Tests](../tests/test_max_sum_two_nonoverlapping.py)

Run this exercise: `python -m unittest tests.test_max_sum_two_nonoverlapping -v`
