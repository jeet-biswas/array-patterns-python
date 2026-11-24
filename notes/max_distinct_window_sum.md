# Largest sum of a fixed-size window with distinct values

Maintain the sum and frequency map of the last k elements. A full window qualifies precisely when its distinct count equals k. Use None when no window qualifies so negative best sums remain valid.

Complexity: Expected O(n) time, O(min(n, k)) space.

- [Implementation](../arrays/max_distinct_window_sum.py)
- [Tests](../tests/test_max_distinct_window_sum.py)

Run this exercise: `python -m unittest tests.test_max_distinct_window_sum -v`
