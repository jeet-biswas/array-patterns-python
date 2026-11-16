# Count longest increasing subsequences

Track both the maximum subsequence length ending at each index and the number of ways to achieve it. Replace counts for a better length and add counts for an equal length; subsequences are distinguished by indices.

Complexity: O(n squared) time, O(n) space.

- [Implementation](../arrays/count_lis.py)
- [Tests](../tests/test_count_lis.py)

Run this exercise: `python -m unittest tests.test_count_lis -v`
