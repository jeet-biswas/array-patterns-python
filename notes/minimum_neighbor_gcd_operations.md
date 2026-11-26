# Fewest neighbor-GCD replacements to make every value one

Existing ones can spread to every other position in one operation each. Otherwise find the shortest contiguous interval with GCD one: reducing it creates the first one in length-minus-one operations, then spreading it needs n-minus-one more. GCD bit costs depend on the values.

Complexity: O(n squared) GCD operations, O(1) auxiliary space.

- [Implementation](../arrays/minimum_neighbor_gcd_operations.py)
- [Tests](../tests/test_minimum_neighbor_gcd_operations.py)

Run this exercise: `python -m unittest tests.test_minimum_neighbor_gcd_operations -v`
