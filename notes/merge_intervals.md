# Merge overlapping closed intervals

Sort interval pairs by their start. Extend the last merged interval whenever the next start is at most its end. Touching endpoints overlap; adjacent integer intervals with a real gap do not.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/merge_intervals.py)
- [Tests](../tests/test_merge_intervals.py)

Run this exercise: `python -m unittest tests.test_merge_intervals -v`
