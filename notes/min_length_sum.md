# Shortest subarray reaching a positive target

With nonnegative elements, expanding a window cannot decrease its sum. Shrink each qualifying window until it falls below the target. Negative elements are rejected because they invalidate this monotonicity.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/min_length_sum.py)
- [Tests](../tests/test_min_length_sum.py)

Run this exercise: `python -m unittest tests.test_min_length_sum -v`
