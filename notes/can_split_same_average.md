# Split an array into two nonempty groups with equal averages

A subset of size k must sum to total*k/n. Consider only sizes at most n/2 because the complementary group gives the same split. Descending size updates track reachable sums without reusing indices. R bounds the number of sums reachable at any one size; it can grow exponentially for unrestricted integers.

Complexity: Expected O(n squared R) time, O(nR) space.

- [Implementation](../arrays/can_split_same_average.py)
- [Tests](../tests/test_can_split_same_average.py)

Run this exercise: `python -m unittest tests.test_can_split_same_average -v`
