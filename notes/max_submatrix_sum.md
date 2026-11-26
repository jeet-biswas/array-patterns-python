# Maximum sum of a nonempty rectangular submatrix

Compress each pair of row boundaries into column sums and apply the nonempty maximum-subarray recurrence. Initialize from actual cells so an all-negative matrix cannot incorrectly select an empty rectangle.

Complexity: O(r + r squared c) time, O(c) auxiliary space.

- [Implementation](../arrays/max_submatrix_sum.py)
- [Tests](../tests/test_max_submatrix_sum.py)

Run this exercise: `python -m unittest tests.test_max_submatrix_sum -v`
