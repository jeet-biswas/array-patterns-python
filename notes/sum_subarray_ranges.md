# Sum of all contiguous subarray ranges

A subarray range is its maximum minus its minimum. Use two monotonic-stack contribution passes to count how often each element supplies either extreme. Asymmetric equal-value boundaries prevent double counting.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/sum_subarray_ranges.py)
- [Tests](../tests/test_sum_subarray_ranges.py)

Run this exercise: `python -m unittest tests.test_sum_subarray_ranges -v`
