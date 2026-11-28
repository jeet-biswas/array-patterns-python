# Count index pairs whose XOR lies in an inclusive interval

A counted binary trie stores earlier values. For a strict XOR upper bound, each one bit in the bound allows all same-bit branches at that level while continuing down the opposite-bit branch. Subtract counts below low from counts below high+1. Insert only after querying to exclude self-pairs.

Complexity: O(nB) bit operations, O(nB) space.

- [Implementation](../arrays/count_pairs_xor_interval.py)
- [Tests](../tests/test_count_pairs_xor_interval.py)

Run this exercise: `python -m unittest tests.test_count_pairs_xor_interval -v`
