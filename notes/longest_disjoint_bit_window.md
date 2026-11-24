# Longest window whose elements share no set bits

Maintain the bitwise union of a valid window. When the next value overlaps it, remove left elements until the conflict vanishes. Because current elements have disjoint set bits, XOR removes exactly the departing bits. Bit-operation cost depends on integer width.

Complexity: O(n) bitwise operations, O(1) auxiliary slots.

- [Implementation](../arrays/longest_disjoint_bit_window.py)
- [Tests](../tests/test_longest_disjoint_bit_window.py)

Run this exercise: `python -m unittest tests.test_longest_disjoint_bit_window -v`
