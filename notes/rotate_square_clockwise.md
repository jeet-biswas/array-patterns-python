# Rotate a square array clockwise in place

Transpose across the main diagonal, then reverse each row. The composition sends each original cell at (row,column) to (column,n-1-row). Validate all row lengths before mutating anything.

Complexity: O(n squared) time, O(1) auxiliary space.

- [Implementation](../arrays/rotate_square_clockwise.py)
- [Tests](../tests/test_rotate_square_clockwise.py)

Run this exercise: `python -m unittest tests.test_rotate_square_clockwise -v`
