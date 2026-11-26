# Reshape a rectangular array while preserving row-major order

Check that source and requested cell counts agree, then map each destination flat index back to a source row and column. Rows are newly allocated and independent. r and c describe the source; R is the requested row count.

Complexity: O(r + R + rc) time, O(R + rc) output space.

- [Implementation](../arrays/reshape_rectangular_array.py)
- [Tests](../tests/test_reshape_rectangular_array.py)

Run this exercise: `python -m unittest tests.test_reshape_rectangular_array -v`
