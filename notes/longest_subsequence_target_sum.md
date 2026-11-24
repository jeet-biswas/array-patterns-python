# Longest subsequence with an exact signed sum

Map each reachable sum to the longest subsequence attaining it. Copy the previous map before adding the new element so an index cannot be reused. Unlike a positive-only table, this representation supports negative values and zero; R is the number of reachable sums.

Complexity: Expected O(nR) time, O(R) space.

- [Implementation](../arrays/longest_subsequence_target_sum.py)
- [Tests](../tests/test_longest_subsequence_target_sum.py)

Run this exercise: `python -m unittest tests.test_longest_subsequence_target_sum -v`
