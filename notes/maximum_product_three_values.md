# Largest product of three distinct-index array elements

Track the largest three values and the smallest two. An optimal product uses either the three largest, or the largest with two sufficiently negative values. Exactly three indices are required, so negative optima are retained rather than replaced by zero.

Complexity: O(n) time, O(1) auxiliary space.

- [Implementation](../arrays/maximum_product_three_values.py)
- [Tests](../tests/test_maximum_product_three_values.py)

Run this exercise: `python -m unittest tests.test_maximum_product_three_values -v`
