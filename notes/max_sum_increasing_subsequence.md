# Maximum sum strictly increasing subsequence

For each endpoint, start a nonempty subsequence there or extend any smaller previous value's best sum. Tracking sums instead of lengths allows a shorter, higher-valued subsequence to win.

Complexity: O(n squared) time, O(n) space.

- [Implementation](../arrays/max_sum_increasing_subsequence.py)
- [Tests](../tests/test_max_sum_increasing_subsequence.py)

Run this exercise: `python -m unittest tests.test_max_sum_increasing_subsequence -v`
