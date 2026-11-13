# Smallest missing positive integer

Rearrange relevant values so integer x occupies index x-1. A duplicate guard prevents swap cycles. Every successful swap places a value in its final slot; scan for the first mismatch.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/smallest_missing_positive.py)
- [Tests](../tests/test_smallest_missing_positive.py)

Run this exercise: `python -m unittest tests.test_smallest_missing_positive -v`
