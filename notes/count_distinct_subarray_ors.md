# Count distinct OR results of all subarrays

Keep the set of OR values for subarrays ending at the current position. Extending every previous result and adding the singleton generates the next set. Each strict change in a suffix OR adds a bit, bounding the frontier by the input bit width plus one.

Complexity: Expected O(nB) set operations, O(nB) space.

- [Implementation](../arrays/count_distinct_subarray_ors.py)
- [Tests](../tests/test_count_distinct_subarray_ors.py)

Run this exercise: `python -m unittest tests.test_count_distinct_subarray_ors -v`
