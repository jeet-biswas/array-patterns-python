# Select and order values for the largest time-weighted sum

An exchange argument puts smaller selected values earlier. Build the selection from largest to smallest: adding a new first value increases the total by the sum of all selected values including it. Stop once that marginal gain is nonpositive.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/max_time_weighted_satisfaction.py)
- [Tests](../tests/test_max_time_weighted_satisfaction.py)

Run this exercise: `python -m unittest tests.test_max_time_weighted_satisfaction -v`
