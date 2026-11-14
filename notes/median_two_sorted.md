# Median of two sorted arrays

Binary-search a partition in the shorter array; the complementary partition fixes the combined left-half size. When both left maxima are no greater than the opposite right minima, the central value(s) determine the median without merging.

Complexity: O(log(min(n, m) + 1)) time, O(1) space.

- [Implementation](../arrays/median_two_sorted.py)
- [Tests](../tests/test_median_two_sorted.py)

Run this exercise: `python -m unittest tests.test_median_two_sorted -v`
