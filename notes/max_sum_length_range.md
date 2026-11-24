# Maximum subarray sum with length inside a range

For each right endpoint, the eligible starting prefix sums lie in an index interval. Keep their minimum in an increasing deque, adding newly eligible prefixes and expiring old ones. Subtract that minimum from the current prefix sum; signed values work without special cases.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/max_sum_length_range.py)
- [Tests](../tests/test_max_sum_length_range.py)

Run this exercise: `python -m unittest tests.test_max_sum_length_range -v`
