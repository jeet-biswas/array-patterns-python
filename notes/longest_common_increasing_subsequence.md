# Longest strictly increasing subsequence common to two arrays

For each value in the first array, scan the second while tracking the best common subsequence ending in a smaller value. Equal values can extend that best state. Strict comparison prevents current equal-value updates from being reused in the same pass.

Complexity: O(nm) time, O(m) space.

- [Implementation](../arrays/longest_common_increasing_subsequence.py)
- [Tests](../tests/test_longest_common_increasing_subsequence.py)

Run this exercise: `python -m unittest tests.test_longest_common_increasing_subsequence -v`
