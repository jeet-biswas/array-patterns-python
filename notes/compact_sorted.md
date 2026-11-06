# Remove duplicates from a sorted array

Keep a write boundary for the unique prefix. Input must already be sorted in nondecreasing order; the returned length identifies the meaningful prefix and the tail is unspecified.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/compact_sorted.py)
- [Tests](../tests/test_compact_sorted.py)

Run this exercise: `python -m unittest tests.test_compact_sorted -v`
