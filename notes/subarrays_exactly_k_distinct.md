# Count subarrays with exactly k distinct values

Subtract the number of subarrays with at most k-1 distinct values from those with at most k. Each helper maintains frequencies in a feasible sliding window; all suffixes ending at its right edge qualify.

Complexity: Expected O(n) time, O(min(n, k)) space.

- [Implementation](../arrays/subarrays_exactly_k_distinct.py)
- [Tests](../tests/test_subarrays_exactly_k_distinct.py)

Run this exercise: `python -m unittest tests.test_subarrays_exactly_k_distinct -v`
