# Minimum top-to-bottom path with neighboring columns

For each cell, choose the smallest predecessor from the previous row at the same column or either adjacent column. Separate old and new rows prevent an updated value being reused in the same row.

Complexity: O(r + rc) time, O(c) auxiliary space.

- [Implementation](../arrays/minimum_falling_path_sum.py)
- [Tests](../tests/test_minimum_falling_path_sum.py)

Run this exercise: `python -m unittest tests.test_minimum_falling_path_sum -v`
