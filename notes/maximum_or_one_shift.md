# Largest array OR after shifting one chosen value

Precompute suffix OR values and scan with a prefix OR. Shifting the current value and combining it with the unaffected prefix and suffix evaluates that choice in constant many bitwise operations. Integer-operation costs depend on input width and shift size.

Complexity: O(n) bitwise operations, O(n) auxiliary integer slots.

- [Implementation](../arrays/maximum_or_one_shift.py)
- [Tests](../tests/test_maximum_or_one_shift.py)

Run this exercise: `python -m unittest tests.test_maximum_or_one_shift -v`
