# Longest strict mountain subarray

Track lengths of the current strict ascent and descent. A plateau breaks a mountain; a new ascent after a descent starts another candidate. Only runs with both sides qualify.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/longest_mountain.py)
- [Tests](../tests/test_longest_mountain.py)

Run this exercise: `python -m unittest tests.test_longest_mountain -v`
