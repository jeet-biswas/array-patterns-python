# Merge sorted arrays into an existing buffer

Fill the destination from the back, choosing the larger remaining source element. This protects unread destination elements and uses only the buffer already supplied by the caller.

Complexity: O(n + m) time, O(1) space.

- [Implementation](../arrays/merge_into_buffer.py)
- [Tests](../tests/test_merge_into_buffer.py)

Run this exercise: `python -m unittest tests.test_merge_into_buffer -v`
