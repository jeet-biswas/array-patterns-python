# Largest all-one rectangle in a binary matrix

Each row extends a histogram of consecutive ones above it. For each histogram, a monotone index stack finalizes maximal rectangles when a lower height arrives. A virtual trailing zero flushes all remaining bars.

Complexity: O(r + rc) time, O(c) auxiliary space.

- [Implementation](../arrays/max_binary_matrix_rectangle.py)
- [Tests](../tests/test_max_binary_matrix_rectangle.py)

Run this exercise: `python -m unittest tests.test_max_binary_matrix_rectangle -v`
