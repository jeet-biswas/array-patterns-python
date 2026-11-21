# Maximum dot product of two nonempty subsequences

A prefix-pair DP either skips one endpoint, starts a new pair, or extends a previous paired subsequence. Unreachable states use None so all-negative dot products cannot incorrectly choose an empty selection.

Complexity: O(nm) time, O(m) space.

- [Implementation](../arrays/max_subsequence_dot_product.py)
- [Tests](../tests/test_max_subsequence_dot_product.py)

Run this exercise: `python -m unittest tests.test_max_subsequence_dot_product -v`
