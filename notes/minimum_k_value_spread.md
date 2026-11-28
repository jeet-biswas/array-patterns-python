# Choose k array elements with the smallest value range

After sorting, a best group can be chosen as k consecutive values: skipping an interior value cannot improve its endpoints. Examine every width-k window and minimize its endpoint difference. Empty and singleton selections have zero spread.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/minimum_k_value_spread.py)
- [Tests](../tests/test_minimum_k_value_spread.py)

Run this exercise: `python -m unittest tests.test_minimum_k_value_spread -v`
