# Count ordered sequences of reusable array values with a target sum

Process target amounts in increasing order. For each possible last value, append it to every sequence attaining the preceding amount. Unlike coin multisets, different orders count separately. n is input length, d distinct value count and T the target; exact integer arithmetic may grow with the result.

Complexity: O(n + d log d + dT + T) time, O(d + T) space.

- [Implementation](../arrays/count_ordered_target_sums.py)
- [Tests](../tests/test_count_ordered_target_sums.py)

Run this exercise: `python -m unittest tests.test_count_ordered_target_sums -v`
