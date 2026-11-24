# Sum distances to matching values at every index

Collect total count and index sum for each value. During a second pass, maintain the count and index sum of earlier occurrences. The left and right distance totals then follow from two count-times-index formulas.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/equal_value_index_distances.py)
- [Tests](../tests/test_equal_value_index_distances.py)

Run this exercise: `python -m unittest tests.test_equal_value_index_distances -v`
