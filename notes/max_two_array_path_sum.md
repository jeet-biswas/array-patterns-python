# Maximum forward path sum across two sorted arrays

Accumulate the two path sums independently between common values. At a common value, either path may be chosen, so synchronize both sums to their larger value plus the common element once. Continue until both arrays end.

Complexity: O(n + m) time, O(1) auxiliary space.

- [Implementation](../arrays/max_two_array_path_sum.py)
- [Tests](../tests/test_max_two_array_path_sum.py)

Run this exercise: `python -m unittest tests.test_max_two_array_path_sum -v`
