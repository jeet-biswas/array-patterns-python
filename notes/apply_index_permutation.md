# Rearrange values in place using a destination permutation

Validate that destinations form a permutation, then follow each cycle while carrying one displaced value. Each original item moves directly to its destination and each cycle is visited once. The destination array remains unchanged.

Complexity: O(n) time, O(n) auxiliary space.

- [Implementation](../arrays/apply_index_permutation.py)
- [Tests](../tests/test_apply_index_permutation.py)

Run this exercise: `python -m unittest tests.test_apply_index_permutation -v`
