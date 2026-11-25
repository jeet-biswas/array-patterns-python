# Fastest synchronous neighbor copying on a circular array

For a chosen final value, its occurrences spread in both directions at one position per second. The largest circular gap between occurrences needs floor(gap/2) seconds. Minimize that delay over all values present initially.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/minimum_circular_equalization_seconds.py)
- [Tests](../tests/test_minimum_circular_equalization_seconds.py)

Run this exercise: `python -m unittest tests.test_minimum_circular_equalization_seconds -v`
