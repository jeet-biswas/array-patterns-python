# Insert and merge one closed interval into a sorted array

Copy intervals completely before the insertion. Merge every interval touching its growing boundaries, then append the remaining intervals. Validation ensures the original intervals are sorted and strictly disjoint.

Complexity: O(n) time, O(n) output space.

- [Implementation](../arrays/insert_closed_interval.py)
- [Tests](../tests/test_insert_closed_interval.py)

Run this exercise: `python -m unittest tests.test_insert_closed_interval -v`
