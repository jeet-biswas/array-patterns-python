# Reorder values to maximize the total of requested ranges

A difference array counts how often each position is requested. Pair the largest values with the largest frequencies by sorting both arrays; exchanging any reversed pair cannot decrease the total. Signed values and repeated requests are supported.

Complexity: O(n log n + q) time, O(n) space.

- [Implementation](../arrays/maximize_requested_range_sum.py)
- [Tests](../tests/test_maximize_requested_range_sum.py)

Run this exercise: `python -m unittest tests.test_maximize_requested_range_sum -v`
