# Minimum arbitrary swaps to sort a permutation

A permutation decomposes into independent cycles. Sorting a cycle of length c requires exactly c-1 arbitrary swaps. Validate the complete 0..n-1 permutation before traversing cycles.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/min_swaps_permutation.py)
- [Tests](../tests/test_min_swaps_permutation.py)

Run this exercise: `python -m unittest tests.test_min_swaps_permutation -v`
