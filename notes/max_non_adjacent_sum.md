# Maximum sum of nonadjacent elements

Track the best sums for prefixes ending one and two positions earlier. Either skip the current element or take it with the best prefix that excludes its neighbor. The empty selection is permitted.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/max_non_adjacent_sum.py)
- [Tests](../tests/test_max_non_adjacent_sum.py)

Run this exercise: `python -m unittest tests.test_max_non_adjacent_sum -v`
