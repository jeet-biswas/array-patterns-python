# Longest subsequence with a specified difference

Store the best subsequence length ending at each value. A new value extends only the state at value minus difference. Read that state before replacing it, which also handles zero difference.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/longest_fixed_difference_subsequence.py)
- [Tests](../tests/test_longest_fixed_difference_subsequence.py)

Run this exercise: `python -m unittest tests.test_longest_fixed_difference_subsequence -v`
