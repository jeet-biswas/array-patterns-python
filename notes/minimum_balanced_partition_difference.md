# Partition into equal-sized groups with minimum sum difference

Enumerate subset sums of each half, grouped by selected count. Pair a left group with the right count needed to select exactly half the original indices. Binary-search near half the total using integer ceiling division, keeping arbitrarily large signed sums exact.

Complexity: O(n 2^(n/2)) time, O(2^(n/2)) space.

- [Implementation](../arrays/minimum_balanced_partition_difference.py)
- [Tests](../tests/test_minimum_balanced_partition_difference.py)

Run this exercise: `python -m unittest tests.test_minimum_balanced_partition_difference -v`
