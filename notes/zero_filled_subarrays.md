# Count all-zero contiguous subarrays

A run of r zeros contributes r new subarrays at its final position. Reset the run on every nonzero value and add the current run length to the answer.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/zero_filled_subarrays.py)
- [Tests](../tests/test_zero_filled_subarrays.py)

Run this exercise: `python -m unittest tests.test_zero_filled_subarrays -v`
