# Reconstruct indices of a longest increasing subsequence

Track the smallest ending value and its source index for each subsequence length. Parent indices remember the chosen predecessor when a state is replaced, allowing an optimal index sequence to be reconstructed afterward. Equal tails are replaced by the latest index; no lexicographic optimality is claimed.

Complexity: O(n log(n + 1)) time, O(n) space.

- [Implementation](../arrays/reconstruct_lis_indices.py)
- [Tests](../tests/test_reconstruct_lis_indices.py)

Run this exercise: `python -m unittest tests.test_reconstruct_lis_indices -v`
