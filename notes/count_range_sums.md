# Count subarray sums inside an inclusive range

Express subarray sums as differences of ordered prefix positions. Recursively sort prefix halves, then use two moving boundaries in the right half to count differences between the inclusive bounds. Counting happens before merging so original position order is respected.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/count_range_sums.py)
- [Tests](../tests/test_count_range_sums.py)

Run this exercise: `python -m unittest tests.test_count_range_sums -v`
