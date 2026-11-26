# Traverse matrix diagonals in alternating directions

Cells on a diagonal share row-plus-column. Enumerate each diagonal's valid row bounds; traverse rows downward on odd diagonals and upward on even diagonals to alternate direction.

Complexity: O(r + rc) time, O(rc) output space.

- [Implementation](../arrays/diagonal_zigzag_values.py)
- [Tests](../tests/test_diagonal_zigzag_values.py)

Run this exercise: `python -m unittest tests.test_diagonal_zigzag_values -v`
