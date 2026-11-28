# Sum XOR results over every index subset

For any bit present in at least one element, exactly half of all index subsets have that XOR bit set: toggling one element carrying the bit pairs subsets with opposite parity. Multiply the OR of all values by 2^(n-1). Integer bit costs depend on input and result width.

Complexity: O(n) bitwise operations, O(1) auxiliary integer slots.

- [Implementation](../arrays/sum_subset_xors.py)
- [Tests](../tests/test_sum_subset_xors.py)

Run this exercise: `python -m unittest tests.test_sum_subset_xors -v`
