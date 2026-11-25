# Maximum subarray sum after squaring exactly one element

Track best suffix sums before and after the one required squaring. The modified suffix may start here, square this value after an unmodified suffix, or extend an already modified suffix. Initialize with a squared element so the operation cannot be skipped.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_subarray_one_square.py)
- [Tests](../tests/test_max_subarray_one_square.py)

Run this exercise: `python -m unittest tests.test_max_subarray_one_square -v`
