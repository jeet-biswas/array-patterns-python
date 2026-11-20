# Minimum range after at most three value changes

After sorting, changing extremes is sufficient: distribute the three allowed changes between the smallest and largest values in four possible ways. With at most four elements, all values can be made equal using three changes.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/minimum_range_three_changes.py)
- [Tests](../tests/test_minimum_range_three_changes.py)

Run this exercise: `python -m unittest tests.test_minimum_range_three_changes -v`
