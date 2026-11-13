# Maximum product subarray

Keep both the maximum and minimum products ending at the current index: multiplying by a negative swaps their roles. Zeros naturally reset candidate products. Integer bit cost grows with product magnitude.

Complexity: O(n) arithmetic operations, O(1) space.

- [Implementation](../arrays/max_product_subarray.py)
- [Tests](../tests/test_max_product_subarray.py)

Run this exercise: `python -m unittest tests.test_max_product_subarray -v`
