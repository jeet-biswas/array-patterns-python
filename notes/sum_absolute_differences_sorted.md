# Sum absolute differences from each sorted array value

Sorted order removes the absolute-value signs: left contributions are count times current value minus left sum, and right contributions reverse that subtraction. A running prefix sum and the total sum compute every answer in one pass.

Complexity: O(n) time, O(n) output space.

- [Implementation](../arrays/sum_absolute_differences_sorted.py)
- [Tests](../tests/test_sum_absolute_differences_sorted.py)

Run this exercise: `python -m unittest tests.test_sum_absolute_differences_sorted -v`
