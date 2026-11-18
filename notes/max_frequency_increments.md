# Maximum frequency after limited increments

Sort a copy and maintain a window whose values can all be raised to its rightmost value within budget. The required cost is window length times that value minus the window sum. Remove the smallest values when the budget is exceeded.

Complexity: O(n log n) time, O(n) space.

- [Implementation](../arrays/max_frequency_increments.py)
- [Tests](../tests/test_max_frequency_increments.py)

Run this exercise: `python -m unittest tests.test_max_frequency_increments -v`
