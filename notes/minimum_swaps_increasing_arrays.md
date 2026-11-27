# Fewest same-index swaps making both arrays strictly increasing

At each position retain the best cost with or without swapping its two values. Compare both possible previous orientations with each current orientation; only transitions preserving strict increase in both arrays are allowed. None marks unreachable states.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/minimum_swaps_increasing_arrays.py)
- [Tests](../tests/test_minimum_swaps_increasing_arrays.py)

Run this exercise: `python -m unittest tests.test_minimum_swaps_increasing_arrays -v`
