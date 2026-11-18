# Shortest removal making the remaining sum divisible

The removed segment must have the same remainder as the total array sum. Track the latest position of each prefix remainder to minimize the removed length. Removing the entire array is disallowed, while removing nothing is valid.

Complexity: Expected O(n) time, O(min(n, p)) space.

- [Implementation](../arrays/min_removal_divisible.py)
- [Tests](../tests/test_min_removal_divisible.py)

Run this exercise: `python -m unittest tests.test_min_removal_divisible -v`
