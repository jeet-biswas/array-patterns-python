# Count subarrays with maximum in an interval

Track the most recent value above the upper bound and the most recent value inside the allowed maximum interval. Valid starts lie after the former and at or before the latter.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_bounded_max.py)
- [Tests](../tests/test_count_bounded_max.py)

Run this exercise: `python -m unittest tests.test_count_bounded_max -v`
