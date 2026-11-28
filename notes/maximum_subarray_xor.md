# Largest XOR over all contiguous nonempty subarrays

A subarray XOR equals the XOR of two prefix XORs. Store earlier prefixes in a binary trie, beginning with zero, and query the best partner for each new prefix. Query before inserting to ensure a nonempty interval.

Complexity: O(nB) bit operations, O(nB) space.

- [Implementation](../arrays/maximum_subarray_xor.py)
- [Tests](../tests/test_maximum_subarray_xor.py)

Run this exercise: `python -m unittest tests.test_maximum_subarray_xor -v`
