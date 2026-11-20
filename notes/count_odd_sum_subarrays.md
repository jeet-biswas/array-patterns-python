# Count contiguous subarrays with odd sum

A subarray sum is odd when its two bounding prefixes have different parity. Track only even and odd prefix counts, querying the opposite parity before recording each new prefix.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_odd_sum_subarrays.py)
- [Tests](../tests/test_count_odd_sum_subarrays.py)

Run this exercise: `python -m unittest tests.test_count_odd_sum_subarrays -v`
