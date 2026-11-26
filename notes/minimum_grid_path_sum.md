# Minimum right-and-down path sum through a matrix

Each cell is reached from above or from the left. A single DP row holds both the previous-row costs and the already updated left cost. Signed cell costs are safe because the movement graph has no cycles.

Complexity: O(r + rc) time, O(c) auxiliary space.

- [Implementation](../arrays/minimum_grid_path_sum.py)
- [Tests](../tests/test_minimum_grid_path_sum.py)

Run this exercise: `python -m unittest tests.test_minimum_grid_path_sum -v`
