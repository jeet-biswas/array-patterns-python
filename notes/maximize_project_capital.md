# Maximize capital by selecting affordable projects

Sort projects by their required capital, then add newly affordable profits to a max-heap. Selecting the largest available nonnegative profit maximizes the capital available to unlock future projects. Each project can be chosen once; requirements are thresholds, not deducted costs.

Complexity: O(n log n + k log(n + 1)) time, O(n) space.

- [Implementation](../arrays/maximize_project_capital.py)
- [Tests](../tests/test_maximize_project_capital.py)

Run this exercise: `python -m unittest tests.test_maximize_project_capital -v`
