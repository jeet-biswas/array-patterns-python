# Transform one array into another with unit interval additions

Split the required difference at each position into its positive and negative demands. Count new layers whenever either demand rises above its preceding value. Operations can extend across compatible positions, but positive and negative demands need separate layers. An optimal solution exists without overshooting a position.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/minimum_signed_range_operations.py)
- [Tests](../tests/test_minimum_signed_range_operations.py)

Run this exercise: `python -m unittest tests.test_minimum_signed_range_operations -v`
