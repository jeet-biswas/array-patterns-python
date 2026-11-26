# Count splits into three nonempty equal-sum array parts

If the total is divisible by three, valid first boundaries have prefix sum one third and second boundaries have prefix sum two thirds. Count earlier first boundaries before processing the current one, which prevents empty middle parts even when the target sum is zero.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_three_equal_sum_partitions.py)
- [Tests](../tests/test_count_three_equal_sum_partitions.py)

Run this exercise: `python -m unittest tests.test_count_three_equal_sum_partitions -v`
