# Sum the clipped square neighborhood of every matrix cell

Build a padded two-dimensional prefix table. Clip each cell's radius-k neighborhood to the matrix bounds, then use four prefix entries to recover its sum. Radius larger than either dimension is handled without scanning larger windows.

Complexity: O(r + rc) time, O((r + 1)(c + 1)) space.

- [Implementation](../arrays/matrix_block_sums.py)
- [Tests](../tests/test_matrix_block_sums.py)

Run this exercise: `python -m unittest tests.test_matrix_block_sums -v`
