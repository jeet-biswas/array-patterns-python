# Count all strictly smaller array elements for each position

Aggregate equal values, sort distinct keys, and record the cumulative frequency before each key. Looking up that prefix frequency for every original element produces its strictly smaller count, without assigning different ranks to duplicates.

Complexity: O(n + u log u) time, O(n + u) space.

- [Implementation](../arrays/count_smaller_values.py)
- [Tests](../tests/test_count_smaller_values.py)

Run this exercise: `python -m unittest tests.test_count_smaller_values -v`
