# Count negatives in a nonincreasing row-and-column matrix

Start at the bottom-left cell. If it is negative, every cell to its right is also negative; count the whole suffix and move up. Otherwise all cells above it are nonnegative, so move right. Shape is checked, while sortedness is a documented precondition to retain the linear boundary walk.

Complexity: O(r + c) time, O(1) space.

- [Implementation](../arrays/count_sorted_matrix_negatives.py)
- [Tests](../tests/test_count_sorted_matrix_negatives.py)

Run this exercise: `python -m unittest tests.test_count_sorted_matrix_negatives -v`
