# Longest subarray with positive product

Track the lengths of positive-product and negative-product suffixes. A negative value exchanges their roles; zero discards both. This avoids computing potentially enormous products.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/longest_positive_product.py)
- [Tests](../tests/test_longest_positive_product.py)

Run this exercise: `python -m unittest tests.test_longest_positive_product -v`
