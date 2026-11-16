# Minimize the largest contiguous partition sum

Binary-search the allowed maximum segment sum. For nonnegative values, greedily filling each segment minimizes the number of segments needed. Feasibility with at most k segments implies exactly k when k does not exceed n, because segments can be subdivided.

Complexity: O(n log(S + 1)) time, O(1) space.

- [Implementation](../arrays/split_array_min_largest_sum.py)
- [Tests](../tests/test_split_array_min_largest_sum.py)

Run this exercise: `python -m unittest tests.test_split_array_min_largest_sum -v`
