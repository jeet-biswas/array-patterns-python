# Maximum sum of exactly k equal-width windows

Dynamic programming over prefix length and selected-window count either skips the last position or ends a window there. Keep only the previous count layer, and use None for impossible states so negative totals remain valid.

Complexity: O(nk) time, O(n) space.

- [Implementation](../arrays/max_sum_k_windows.py)
- [Tests](../tests/test_max_sum_k_windows.py)

Run this exercise: `python -m unittest tests.test_max_sum_k_windows -v`
