# Construct the inverse of an index permutation

The inverse maps each destination back to its source. Allocate the result once and assign inverse[permutation[i]] = i. Validate the full domain and uniqueness before constructing the mapping.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/inverse_index_permutation.py)
- [Tests](../tests/test_inverse_index_permutation.py)

Run this exercise: `python -m unittest tests.test_inverse_index_permutation -v`
