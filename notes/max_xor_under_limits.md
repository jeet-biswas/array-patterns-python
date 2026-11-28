# Answer maximum-XOR queries with value upper limits

Sort values and queries by the permitted limit. Insert newly eligible values into a binary trie and greedily prefer the opposite bit to maximize each query XOR. Restore answers to input order; no eligible value produces None. B covers both stored values and query values.

Complexity: O(n log n + q log q + (n + q)B) time, O(nB + q) space.

- [Implementation](../arrays/max_xor_under_limits.py)
- [Tests](../tests/test_max_xor_under_limits.py)

Run this exercise: `python -m unittest tests.test_max_xor_under_limits -v`
