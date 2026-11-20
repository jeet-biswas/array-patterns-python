# Earliest day for disjoint adjacent bouquets

For a proposed day, sweep consecutive bloomed flowers and consume every full bouquet-sized run. Feasibility is monotonic in the day, allowing binary search. Each flower can belong to only one bouquet.

Complexity: O(n log(D + 1)) time, O(1) space.

- [Implementation](../arrays/min_bouquet_day.py)
- [Tests](../tests/test_min_bouquet_day.py)

Run this exercise: `python -m unittest tests.test_min_bouquet_day -v`
