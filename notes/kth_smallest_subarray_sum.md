# Kth smallest sum among all nonempty subarrays

Binary-search the candidate sum. For nonnegative inputs a sliding window counts all subarrays whose sum is at most that candidate in linear time. The first candidate with at least k qualifying subarrays is the desired value; duplicate sums count separately. S is the total sum.

Complexity: O(n log(S + 1)) time, O(1) space.

- [Implementation](../arrays/kth_smallest_subarray_sum.py)
- [Tests](../tests/test_kth_smallest_subarray_sum.py)

Run this exercise: `python -m unittest tests.test_kth_smallest_subarray_sum -v`
