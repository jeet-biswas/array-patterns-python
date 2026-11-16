# Maximum absolute subarray sum

Any contiguous sum is the difference of two prefix sums. The largest absolute difference is the global maximum prefix minus the global minimum prefix, regardless of their order.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_absolute_subarray.py)
- [Tests](../tests/test_max_absolute_subarray.py)

Run this exercise: `python -m unittest tests.test_max_absolute_subarray -v`
