# Rearrange an array into alternating non-strict peaks and valleys

Scan neighboring pairs and swap whenever the current <= or >= requirement is violated. Swapping puts the appropriate extremum at the shared position, preserving the already established relation to its left. Non-strict inequalities make duplicates harmless.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/wiggle_sort_non_strict.py)
- [Tests](../tests/test_wiggle_sort_non_strict.py)

Run this exercise: `python -m unittest tests.test_wiggle_sort_non_strict -v`
