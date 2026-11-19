# Count subarrays with a target XOR

XOR cancels equal prefixes: a previous prefix XOR must equal the current prefix XOR combined with the target. Count prefix frequencies, including the empty prefix, before adding each current prefix.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/count_subarrays_xor.py)
- [Tests](../tests/test_count_subarrays_xor.py)

Run this exercise: `python -m unittest tests.test_count_subarrays_xor -v`
