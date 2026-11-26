# Count right-and-down paths avoiding blocked cells

A blocked cell resets its path count to zero. An open cell receives paths from the cell above and the cell to the left. One DP row suffices, and Python integers preserve the exact count.

Complexity: O(r + rc) time, O(c) auxiliary space.

- [Implementation](../arrays/count_grid_paths_obstacles.py)
- [Tests](../tests/test_count_grid_paths_obstacles.py)

Run this exercise: `python -m unittest tests.test_count_grid_paths_obstacles -v`
