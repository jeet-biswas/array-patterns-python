# Shortest window containing a required multiset of values

Track how many required copies remain missing as the right boundary advances. Once every copy is present, shrink from the left until one becomes missing again. Only required values need counters. Ties keep the earliest start; u counts distinct required values.

Complexity: Expected O(n + m) time, O(u) auxiliary space.

- [Implementation](../arrays/minimum_multiset_cover_window.py)
- [Tests](../tests/test_minimum_multiset_cover_window.py)

Run this exercise: `python -m unittest tests.test_minimum_multiset_cover_window -v`
