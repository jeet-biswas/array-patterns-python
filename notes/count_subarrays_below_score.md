# Count windows whose sum times length is below a limit

For nonnegative values, removing a left endpoint never increases sum-times-length. Maintain the longest valid suffix at every right endpoint; all its shorter suffixes also qualify. A nonpositive limit admits no windows.

Complexity: O(n) time, O(1) space.

- [Implementation](../arrays/count_subarrays_below_score.py)
- [Tests](../tests/test_count_subarrays_below_score.py)

Run this exercise: `python -m unittest tests.test_count_subarrays_below_score -v`
