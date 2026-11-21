# Maximum score when adjacent values are forbidden

Aggregate equal values into one score. Process sorted distinct values with take/skip states; only consecutive values conflict. Here u is the number of distinct values. Empty selection is allowed.

Complexity: O(n + u log u) time, O(u) space.

- [Implementation](../arrays/delete_and_earn.py)
- [Tests](../tests/test_delete_and_earn.py)

Run this exercise: `python -m unittest tests.test_delete_and_earn -v`
