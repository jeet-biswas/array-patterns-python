# Count subarrays with product below a threshold

With strictly positive integers, a product window can only grow when extended. Shrink it while the product reaches the threshold; every suffix of the resulting window qualifies. Integer division removes outgoing factors exactly.

Complexity: O(n) arithmetic operations, O(1) space.

- [Implementation](../arrays/count_product_below.py)
- [Tests](../tests/test_count_product_below.py)

Run this exercise: `python -m unittest tests.test_count_product_below -v`
