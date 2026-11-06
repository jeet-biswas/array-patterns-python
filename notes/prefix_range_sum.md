# Immutable prefix sums for range queries

Store the sum before each index. The sum over a half-open interval [start, stop) is the difference of two prefix entries. Build a snapshot so later input mutations do not affect queries.

Complexity: O(n) build/space, O(1) per query.

- [Implementation](../arrays/prefix_range_sum.py)
- [Tests](../tests/test_prefix_range_sum.py)

Run this exercise: `python -m unittest tests.test_prefix_range_sum -v`
