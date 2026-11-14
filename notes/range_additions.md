# Apply many range increments with a difference array

Record each half-open update as a positive difference at its start and a negative difference at its stop. One prefix-sum pass reconstructs the final array. Updates may overlap and deltas may be negative.

Complexity: O(n + q) time, O(n) space.

- [Implementation](../arrays/range_additions.py)
- [Tests](../tests/test_range_additions.py)

Run this exercise: `python -m unittest tests.test_range_additions -v`
