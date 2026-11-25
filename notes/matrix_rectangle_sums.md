# Answer half-open rectangle sums with two-dimensional prefixes

Build a padded two-dimensional prefix table by adding a running row sum to the prefix above it. Each query uses inclusion-exclusion on four corners. Rectangles and queries use half-open row and column boundaries, including empty ranges.

Complexity: O(r + rc + q) time, O((r + 1)(c + 1) + q) space.

- [Implementation](../arrays/matrix_rectangle_sums.py)
- [Tests](../tests/test_matrix_rectangle_sums.py)

Run this exercise: `python -m unittest tests.test_matrix_rectangle_sums -v`
