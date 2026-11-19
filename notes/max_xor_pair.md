# Maximum XOR of two array elements

Insert prior values into a binary trie stored as child-index arrays. For each new value, prefer the opposite bit at every level to maximize XOR from most significant to least significant. Query before insertion so the pair uses distinct indices.

Complexity: O(nB) time, O(nB) space.

- [Implementation](../arrays/max_xor_pair.py)
- [Tests](../tests/test_max_xor_pair.py)

Run this exercise: `python -m unittest tests.test_max_xor_pair -v`
