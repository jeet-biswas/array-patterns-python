# Zero every row and column containing an original zero

Use the first row and column as marker storage after remembering whether they originally contained zeros. Mark the remaining zero locations, clear indicated interior cells, and finally clear the first row or column when their original flags require it.

Complexity: O(r + rc) time, O(1) auxiliary space.

- [Implementation](../arrays/zero_matrix_rows_columns.py)
- [Tests](../tests/test_zero_matrix_rows_columns.py)

Run this exercise: `python -m unittest tests.test_zero_matrix_rows_columns -v`
