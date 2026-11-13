# First equilibrium index

Compute the total once. Before visiting an element, subtract it from the remaining right sum, compare left and right, then include it in the left sum. The pivot itself belongs to neither side.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/pivot_index.py)
- [Tests](../tests/test_pivot_index.py)

Run this exercise: `python -m unittest tests.test_pivot_index -v`
