# Next lexicographic permutation

Find the rightmost increasing pivot, exchange it with the smallest larger suffix value, then reverse the descending suffix. The last permutation wraps to ascending order.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/next_permutation.py)
- [Tests](../tests/test_next_permutation.py)

Run this exercise: `python -m unittest tests.test_next_permutation -v`
