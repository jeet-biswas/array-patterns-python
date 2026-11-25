# Kth smallest element of a row-and-column sorted matrix

Validate the rectangular matrix and its row/column ordering. Merge the sorted rows with a heap holding one current element per row, advancing the row that supplies each minimum. Equal values count separately; r and c are matrix dimensions.

Complexity: O(rc + k log(r + 1)) time, O(r) space.

- [Implementation](../arrays/kth_smallest_sorted_matrix.py)
- [Tests](../tests/test_kth_smallest_sorted_matrix.py)

Run this exercise: `python -m unittest tests.test_kth_smallest_sorted_matrix -v`
