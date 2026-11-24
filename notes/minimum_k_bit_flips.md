# Fewest fixed-length bit flips to obtain all ones

Sweep left to right with the parity of active flips and an expiration array. If the current effective bit is zero, a flip starting here is forced: later flips cannot change this position. Return -1 when that forced flip would exceed the array.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/minimum_k_bit_flips.py)
- [Tests](../tests/test_minimum_k_bit_flips.py)

Run this exercise: `python -m unittest tests.test_minimum_k_bit_flips -v`
