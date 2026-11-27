# Count subarrays whose lower median is a given distinct value

Anchor every candidate at the unique target position. Map smaller values to -1 and larger ones to +1. A subarray has the target as its lower median precisely when the total balance is zero or one. Count left balances and match them with right balances.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/count_subarrays_median_value.py)
- [Tests](../tests/test_count_subarrays_median_value.py)

Run this exercise: `python -m unittest tests.test_count_subarrays_median_value -v`
