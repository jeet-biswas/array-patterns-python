# Count subarrays with a specified least common multiple

Group suffixes by their LCM and discard any LCM that does not divide the target: further extension cannot repair it. Values not dividing the target reset the states. Retained LCMs form a divisibility chain bounded by the target; arithmetic operation costs depend on integer width.

Complexity: O(n log(target + 1)) LCM operations, O(log(target + 1)) states.

- [Implementation](../arrays/count_subarray_lcm.py)
- [Tests](../tests/test_count_subarray_lcm.py)

Run this exercise: `python -m unittest tests.test_count_subarray_lcm -v`
