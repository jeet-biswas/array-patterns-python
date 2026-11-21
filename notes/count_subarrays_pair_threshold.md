# Count subarrays containing enough equal-value pairs

Adding a value creates as many pairs as its current frequency. Shrink qualifying windows until the pair count falls below the threshold; the number of removed starting positions is exactly the number of valid subarrays ending here.

Complexity: Expected O(n) time, O(n) space.

- [Implementation](../arrays/count_subarrays_pair_threshold.py)
- [Tests](../tests/test_count_subarrays_pair_threshold.py)

Run this exercise: `python -m unittest tests.test_count_subarrays_pair_threshold -v`
