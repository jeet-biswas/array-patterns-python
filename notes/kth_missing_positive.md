# Kth missing positive integer in a sorted array

At index i, values[i]-i-1 positive integers are missing before that value. Binary-search the first position where this count reaches k; adding k to that position gives the missing value.

Complexity: O(log(n + 1)) time, O(1) space.

- [Implementation](../arrays/kth_missing_positive.py)
- [Tests](../tests/test_kth_missing_positive.py)

Run this exercise: `python -m unittest tests.test_kth_missing_positive -v`
