# Mutable range sums with a Fenwick array

Each one-based tree slot stores a block ending at that index, whose length is its lowest set bit. Linear construction forwards each block to its parent; updates and prefix queries follow these block boundaries.

Complexity: O(n) build/space, O(log(n + 1)) updates and queries.

- [Implementation](../arrays/fenwick_range_sum.py)
- [Tests](../tests/test_fenwick_range_sum.py)

Run this exercise: `python -m unittest tests.test_fenwick_range_sum -v`
