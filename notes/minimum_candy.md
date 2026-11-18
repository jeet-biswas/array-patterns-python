# Minimum candies respecting adjacent ratings

Give everyone one candy, then enforce increasing ratings from left to right. A reverse pass enforces right-neighbor comparisons while preserving earlier requirements by taking the maximum.

Complexity: O(n) time, O(n) space.

- [Implementation](../arrays/minimum_candy.py)
- [Tests](../tests/test_minimum_candy.py)

Run this exercise: `python -m unittest tests.test_minimum_candy -v`
