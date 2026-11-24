# Longest equal-value block after limited deletions

Group positions by value. Between two occurrences, span length minus occurrence count is exactly the number of other elements that must be deleted. A two-pointer scan over each position list finds the largest affordable group.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/longest_equal_after_deletions.py)
- [Tests](../tests/test_longest_equal_after_deletions.py)

Run this exercise: `python -m unittest tests.test_longest_equal_after_deletions -v`
