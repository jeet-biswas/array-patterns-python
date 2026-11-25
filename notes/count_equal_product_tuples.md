# Count ordered four-index tuples with equal pair products

Group unordered index pairs by product. Distinct positive values ensure two different pairs with equal products cannot share an index. Every pair of pairs gives eight ordered arrangements, accounting for pair exchange and the order inside each pair.

Complexity: Expected O(n squared) time, O(n squared) space.

- [Implementation](../arrays/count_equal_product_tuples.py)
- [Tests](../tests/test_count_equal_product_tuples.py)

Run this exercise: `python -m unittest tests.test_count_equal_product_tuples -v`
