# Partition an array into equal-sum subsets

An equal partition requires a subset totaling half the overall sum. Maintain attainable sums no greater than that target, updating from the previous state so each index is used at most once. Odd totals are impossible.

Complexity: O(nT) time, O(T) space.

- [Implementation](../arrays/can_partition_equal_subset.py)
- [Tests](../tests/test_can_partition_equal_subset.py)

Run this exercise: `python -m unittest tests.test_can_partition_equal_subset -v`
