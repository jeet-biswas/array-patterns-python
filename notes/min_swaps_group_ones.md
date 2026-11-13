# Minimum arbitrary swaps to group ones

A contiguous block containing all ones must have width equal to their total count. Slide a window of that width: the number of zeros inside it equals the number of arbitrary swaps needed to bring outside ones in. This is linear, not circular, grouping.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/min_swaps_group_ones.py)
- [Tests](../tests/test_min_swaps_group_ones.py)

Run this exercise: `python -m unittest tests.test_min_swaps_group_ones -v`
