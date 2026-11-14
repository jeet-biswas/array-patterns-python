# Shortest qualifying subarray with signed values

A monotonic deque stores candidate prefix sums. Remove qualifying prefixes from the front to minimize lengths, and discard larger-or-equal prefixes from the back because the current later, smaller prefix dominates them. Unlike the positive-only sliding window, negative elements are supported.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/shortest_subarray_signed.py)
- [Tests](../tests/test_shortest_subarray_signed.py)

Run this exercise: `python -m unittest tests.test_shortest_subarray_signed -v`
