# Pair two arrays to minimize total absolute difference

Sort both arrays and pair corresponding values. If two pairings cross in sorted order, uncrossing them cannot increase total absolute difference. Repeating that exchange yields the sorted matching and proves its optimality.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/minimum_absolute_pairing_cost.py)
- [Tests](../tests/test_minimum_absolute_pairing_cost.py)

Run this exercise: `python -m unittest tests.test_minimum_absolute_pairing_cost -v`
