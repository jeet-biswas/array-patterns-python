# Minimum adjacent swaps to group all ones

Record each one's position minus its rank among the ones. This removes the spacing needed inside the final block. A median of these adjusted positions minimizes the total movement; unlike arbitrary swaps, movement distance matters.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/min_adjacent_swaps_ones.py)
- [Tests](../tests/test_min_adjacent_swaps_ones.py)

Run this exercise: `python -m unittest tests.test_min_adjacent_swaps_ones -v`
