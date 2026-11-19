# Enumerate the smallest pairs from two sorted arrays

Treat each left value as a sorted row of pair sums with the right array. A min-heap merges row fronts, advancing only the row just emitted. Initialize at most k rows because later rows cannot be needed before k smaller-or-equal pairs.

Complexity: O(r + t log(r + 1)) time, O(r) space plus output.

- [Implementation](../arrays/smallest_pair_sums.py)
- [Tests](../tests/test_smallest_pair_sums.py)

Run this exercise: `python -m unittest tests.test_smallest_pair_sums -v`
