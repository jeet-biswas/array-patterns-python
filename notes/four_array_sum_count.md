# Count target-sum choices from four separate arrays

Count sums formed by the first two arrays, then look up the required complement for every pair from the last two. Array lengths a, b, c and d can differ; equal values at different indices remain distinct choices.

Complexity: Expected O(ab + cd) time, O(ab) space.

- [Implementation](../arrays/four_array_sum_count.py)
- [Tests](../tests/test_four_array_sum_count.py)

Run this exercise: `python -m unittest tests.test_four_array_sum_count -v`
