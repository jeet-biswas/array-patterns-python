# Longest arithmetic subsequence

For each endpoint, map a common difference to the longest arithmetic subsequence ending there. A previous compatible endpoint extends its state; a new pair starts with length two.

Complexity: Expected O(n squared) time, O(n squared) space.

- [Implementation](../arrays/longest_arithmetic_subsequence.py)
- [Tests](../tests/test_longest_arithmetic_subsequence.py)

Run this exercise: `python -m unittest tests.test_longest_arithmetic_subsequence -v`
