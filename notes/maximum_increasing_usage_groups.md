# Maximum increasing-size groups under per-value usage limits

Sort the usage limits and accumulate capacity. With each new value, at most one larger group can become possible. If capacity reaches the triangular requirement for one more group, increase the group count. Sorting prevents excess capacity of a few values from being mistaken for enough distinct members.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/maximum_increasing_usage_groups.py)
- [Tests](../tests/test_maximum_increasing_usage_groups.py)

Run this exercise: `python -m unittest tests.test_maximum_increasing_usage_groups -v`
