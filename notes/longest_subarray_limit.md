# Longest window with bounded value spread

Maintain decreasing maximum and increasing minimum deques of indices. Shrink the left boundary until their difference satisfies the limit. Each index enters and leaves each deque at most once.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/longest_subarray_limit.py)
- [Tests](../tests/test_longest_subarray_limit.py)

Run this exercise: `python -m unittest tests.test_longest_subarray_limit -v`
