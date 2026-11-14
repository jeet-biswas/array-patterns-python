# Longest ones window after limited flips

Track zeros inside a sliding window. Whenever its zero count exceeds the available flips, advance the left edge until the window is feasible again. The input is inspected but not flipped.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/longest_ones_after_flips.py)
- [Tests](../tests/test_longest_ones_after_flips.py)

Run this exercise: `python -m unittest tests.test_longest_ones_after_flips -v`
