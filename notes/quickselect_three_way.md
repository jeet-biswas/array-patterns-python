# Select an order statistic using three-way in-place partitioning

Partition the active range into values below, equal to and above a chosen middle-position pivot. Discard the side not containing the requested rank. Equal values are resolved together. The deterministic pivot has quadratic worst-case behavior, stated explicitly.

Complexity: O(n) typical, O(n squared) worst-case time, O(1) auxiliary space.

- [Implementation](../arrays/quickselect_three_way.py)
- [Tests](../tests/test_quickselect_three_way.py)

Run this exercise: `python -m unittest tests.test_quickselect_three_way -v`
