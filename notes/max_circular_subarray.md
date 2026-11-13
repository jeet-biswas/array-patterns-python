# Maximum circular subarray sum

A best circular subarray either does not wrap, or excludes a minimum-sum middle segment. Track both maximum and minimum contiguous sums. Handle all-negative arrays separately to avoid selecting the empty complement.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_circular_subarray.py)
- [Tests](../tests/test_max_circular_subarray.py)

Run this exercise: `python -m unittest tests.test_max_circular_subarray -v`
