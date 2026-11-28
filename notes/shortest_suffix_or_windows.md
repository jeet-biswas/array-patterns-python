# Shortest window at each index attaining its entire suffix OR

Scan backward and remember the nearest occurrence of each set bit. To collect every bit present in the suffix, a window must reach the furthest of those nearest occurrences. For an all-zero suffix, a single element already attains the maximum OR. B is at least one and otherwise the maximum value bit width.

Complexity: O(nB) bit operations, O(B) auxiliary space plus output.

- [Implementation](../arrays/shortest_suffix_or_windows.py)
- [Tests](../tests/test_shortest_suffix_or_windows.py)

Run this exercise: `python -m unittest tests.test_shortest_suffix_or_windows -v`
