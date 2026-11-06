# First occurrence binary search

Use a half-open interval to locate the first value not less than the target, then check equality. This makes duplicate handling deterministic without a linear scan.

Complexity: O(log n) time, O(1) space.

- [Implementation](../arrays/binary_search.py)
- [Tests](../tests/test_binary_search.py)

Run this exercise: `python -m unittest tests.test_binary_search -v`
