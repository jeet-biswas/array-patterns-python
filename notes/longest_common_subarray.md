# Longest contiguous block shared by two arrays

Store the longest common suffix ending at each pair of indices. Equal values extend the diagonal state, while a mismatch resets it to zero. Update the row backward so the diagonal still belongs to the preceding row.

Complexity: O(nm) time, O(m) space.

- [Implementation](../arrays/longest_common_subarray.py)
- [Tests](../tests/test_longest_common_subarray.py)

Run this exercise: `python -m unittest tests.test_longest_common_subarray -v`
