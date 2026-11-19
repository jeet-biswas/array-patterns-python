# Equalize array values with per-element costs

The weighted absolute-distance objective is minimized at a weighted median. Sort value-weight pairs, find where cumulative weight reaches half the total, then evaluate the cost at that value. Zero weights do not constrain the target.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/min_cost_equal_weighted.py)
- [Tests](../tests/test_min_cost_equal_weighted.py)

Run this exercise: `python -m unittest tests.test_min_cost_equal_weighted -v`
