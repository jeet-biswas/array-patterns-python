# Multiset intersection of sorted arrays

Advance the smaller current value; when values match, consume both and emit one copy. Duplicates appear as many times as the smaller of their two multiplicities.

Complexity: O(n + m) time, O(min(n, m)) output space.

- [Implementation](../arrays/intersect_sorted.py)
- [Tests](../tests/test_intersect_sorted.py)

Run this exercise: `python -m unittest tests.test_intersect_sorted -v`
