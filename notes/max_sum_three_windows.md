# Best three disjoint fixed-length windows

Compute all window sums and the best window at each prefix and suffix. For every feasible middle window, combine the best disjoint choices on both sides. Consistent tie handling returns the lexicographically smallest index triple.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_sum_three_windows.py)
- [Tests](../tests/test_max_sum_three_windows.py)

Run this exercise: `python -m unittest tests.test_max_sum_three_windows -v`
