# Count contiguous arithmetic slices

If the newest difference matches the previous one, every arithmetic slice ending one position earlier can extend, and a new length-three slice begins. Otherwise the ending count resets to zero.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/arithmetic_slices.py)
- [Tests](../tests/test_arithmetic_slices.py)

Run this exercise: `python -m unittest tests.test_arithmetic_slices -v`
