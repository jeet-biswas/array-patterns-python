# Search a row-and-column sorted matrix by its boundary

From the top-right corner, a value above the target eliminates its entire column; a value below the target eliminates its entire row. Sortedness is an unchecked precondition, and shape validation costs O(r).

Complexity: O(r + c) time, O(1) space.

- [Implementation](../arrays/contains_sorted_matrix_value.py)
- [Tests](../tests/test_contains_sorted_matrix_value.py)

Run this exercise: `python -m unittest tests.test_contains_sorted_matrix_value -v`
