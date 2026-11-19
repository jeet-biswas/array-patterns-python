# Batch distinct-value counts for array ranges

Bucket queries by their exclusive right endpoint. As the array is swept, keep one Fenwick marker at each value's latest occurrence, removing its older marker. A range sum then counts exactly the distinct values in that range.

Complexity: Expected O((n + q) log(n + 2)) time, O(n + q) space.

- [Implementation](../arrays/offline_distinct_queries.py)
- [Tests](../tests/test_offline_distinct_queries.py)

Run this exercise: `python -m unittest tests.test_offline_distinct_queries -v`
