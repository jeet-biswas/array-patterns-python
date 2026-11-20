# Count products meeting a threshold for each query value

Sort the second array once. For each positive first-array value, ceiling division gives the minimum partner value needed; a lower-bound search counts all successful partners. Handle zero values and a zero threshold explicitly.

Complexity: O(m log m + n log(m + 1)) time, O(n + m) space.

- [Implementation](../arrays/successful_product_pairs.py)
- [Tests](../tests/test_successful_product_pairs.py)

Run this exercise: `python -m unittest tests.test_successful_product_pairs -v`
