# Longest subarray with an exact sum

Store the earliest position of each prefix sum, because an earlier matching prefix gives a longer subarray. Unlike a nonnegative sliding window, this works with arbitrary signed integers.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/longest_subarray_sum.py)
- [Tests](../tests/test_longest_subarray_sum.py)

Run this exercise: `python -m unittest tests.test_longest_subarray_sum -v`
