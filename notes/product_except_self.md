# Product of all other elements

Store prefix products in the result, then multiply by a running suffix product. No division is needed, so zeros are handled naturally. Python integer multiplication cost grows with integer size.

Complexity: O(n) arithmetic operations, O(n) output space.

- [Implementation](../arrays/product_except_self.py)
- [Tests](../tests/test_product_except_self.py)

Run this exercise: `python -m unittest tests.test_product_except_self -v`
