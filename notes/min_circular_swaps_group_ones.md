# Fewest arbitrary swaps to group ones around a circle

A circular group containing all ones has width equal to the total number of ones. Count zeros in every such circular window; each zero can be exchanged with one outside it. Slide using modular indices without duplicating the array.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/min_circular_swaps_group_ones.py)
- [Tests](../tests/test_min_circular_swaps_group_ones.py)

Run this exercise: `python -m unittest tests.test_min_circular_swaps_group_ones -v`
