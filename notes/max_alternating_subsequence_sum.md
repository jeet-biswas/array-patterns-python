# Maximum alternating signed subsequence sum

Keep the best sums for an even and an odd number of selected elements. Each value can be skipped or extend the opposite parity. An unreachable odd state prevents starting with subtraction; signed inputs are supported.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_alternating_subsequence_sum.py)
- [Tests](../tests/test_max_alternating_subsequence_sum.py)

Run this exercise: `python -m unittest tests.test_max_alternating_subsequence_sum -v`
