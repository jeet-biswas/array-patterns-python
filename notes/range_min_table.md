# Static range minimum sparse table

Precompute minima for intervals of power-of-two lengths. A query uses two overlapping blocks of the largest fitting length; overlap is safe because taking a minimum is idempotent. Updates are intentionally unsupported.

Complexity: O(n log(n + 1)) build/space, O(1) queries.

- [Implementation](../arrays/range_min_table.py)
- [Tests](../tests/test_range_min_table.py)

Run this exercise: `python -m unittest tests.test_range_min_table -v`
