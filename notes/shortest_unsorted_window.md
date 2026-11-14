# Shortest window that needs sorting

A forward scan marks the last value smaller than an earlier maximum. A backward scan marks the first value larger than a later minimum. Sorting exactly between these boundaries sorts the whole array.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/shortest_unsorted_window.py)
- [Tests](../tests/test_shortest_unsorted_window.py)

Run this exercise: `python -m unittest tests.test_shortest_unsorted_window -v`
