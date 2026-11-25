# Count all square submatrices filled with ones

At each one cell, the largest square ending there is one plus the minimum of the top, left and diagonal square sizes. That size also counts all squares ending at the cell, one per possible side length. Only the previous DP row is needed.

Complexity: O(r + rc) time, O(c) auxiliary space.

- [Implementation](../arrays/count_all_one_squares.py)
- [Tests](../tests/test_count_all_one_squares.py)

Run this exercise: `python -m unittest tests.test_count_all_one_squares -v`
