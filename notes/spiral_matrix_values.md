# Read a rectangular array in clockwise spiral order

Traverse the current top edge, right edge, bottom edge and left edge, shrinking each boundary as it is consumed. Recheck the remaining dimensions before traversing bottom and left edges to avoid duplicating a single row or column.

Complexity: O(r + rc) time, O(rc) output space.

- [Implementation](../arrays/spiral_matrix_values.py)
- [Tests](../tests/test_spiral_matrix_values.py)

Run this exercise: `python -m unittest tests.test_spiral_matrix_values -v`
