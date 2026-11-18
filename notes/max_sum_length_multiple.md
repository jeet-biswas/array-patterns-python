# Maximum subarray sum with a divisible length

Subarray length is divisible by k precisely when its two prefix positions have the same remainder modulo k. Keep the smallest prefix sum for each remainder and query it before inserting the current prefix, excluding empty subarrays.

Complexity: Expected O(n) time, O(min(n, k)) space.

- [Implementation](../arrays/max_sum_length_multiple.py)
- [Tests](../tests/test_max_sum_length_multiple.py)

Run this exercise: `python -m unittest tests.test_max_sum_length_multiple -v`
