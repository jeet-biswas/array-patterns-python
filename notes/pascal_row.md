# Generate one row of Pascal triangle

Start with the zeroth row and update coefficients right to left. Descending updates preserve both previous-row values needed for each sum, using one array throughout.

Complexity: O(n squared) arithmetic operations, O(n) space.

- [Implementation](../arrays/pascal_row.py)
- [Tests](../tests/test_pascal_row.py)

Run this exercise: `python -m unittest tests.test_pascal_row -v`
